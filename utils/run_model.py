import csv
import os
import sys
import warnings
import pandas as pd
from tqdm import tqdm
from fix_entities_model import fix_entities

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from transformers_rec import Analyzer, Anonymizer


def create_obj(an_r, text):
    """Show results of analyze() in a dataframe."""
    ents = []
    for r in an_r:
        info = r.to_dict()
        ent = {
            "start": info["start"],
            "end": info["end"],
            "confidence": info["score"],
            "entity": info["entity_type"],
            "text": text[info["start"] : info["end"]],
        }
        ents.append(ent)
    return ents


def model_results(
    analyzer: Analyzer,
    input_path,
    output_path,
    batch_size=10,
    columns=["SITE_URL", "ITEM_GROUP_ID", "PVIDS", "REVIEW"],
    threshold={
        "PERSON": 0.9,
        "CREDIT_CARD": 0.5,
        "US_SSN": 0.5,
        "EMAIL_ADDRESS": 0.5,
        "PHONE_NUMBER": 0.4,
        "LOCATION": 0.7,
    },
    check_overlaps=True,
    entities=[
        "PERSON",
        "LOCATION",
        "PHONE_NUMBER",
        "EMAIL_ADDRESS",
        "CREDIT_CARD",
        "US_SSN",
    ],
):
    """
    Runs a Presidio model with improved n-calls, reading input data from a CSV file and writing output data to another CSV file.

    Arguments:
    :param analyzer: -- Analyzer: the BatchAnalyzer class from transformers_rec.
    :param  input_path: -- str: the path to the input CSV file, which should have the following columns:
        - SITE_URL: str
        - ITEM_GROUP_ID: int or str
        - PVIDS: list of str, the list should be inside a str -
            Example: "[
              ""test.com!1"",
              ""test.com!2"",
              ""test.com!3"",
              ""test.com!4"",
              ""test.com!5""
            ]"
        - REVIEW: str

    :param output_path: -- str: the path to the output CSV file.
    :param batch_size: -- int: the number of rows to read from the input CSV file at a time.
    :param columns: -- list of str: the names of the columns in the input CSV file.
    :param threshold: -- float: the minimum score for an entity to be returned.
    :param check_overlaps: -- bool: if True, the model will not recognize overlapping entities. If False, the model will recognize overlapping entities and return all of entities and the precision/score for each entity.
    :param entities: -- list of str: the entities to recognize.
    Returns:
    None
    """
    #
    # get the total number of rows in the CSV file
    total_rows = pd.read_csv(input_path, usecols=[0]).shape[0]
    print(
        f"getting results for the ner model and presidio. Progressively writing the results in {output_path}..."
    )
    progress_bar = tqdm(total=total_rows)
    with open(output_path, "a", encoding="ISO-8859-1") as fp:
        writer = csv.writer(fp)
        # Write the header row
        writer.writerow(["SITE_URL", "ITEM_GROUP_ID", "PVIDS", "MODEL_OUTPUT"])
        anonymizer = Anonymizer(type="batch")
        for batch in pd.read_csv(
            input_path,
            encoding="ISO-8859-1",
            chunksize=batch_size,
            names=columns,
            header=0,
        ):
            batch_dict = batch.to_dict(orient="list")
            analyzer_results = analyzer.analyze(
                input_dict=batch_dict,
                language="en",
                entities=entities,
                score_threshold=threshold,
                keys_to_skip=["SITE_URL", "ITEM_GROUP_ID", "PVIDS"],
                progress_bar=progress_bar,
            )
            analyzer_results = list(analyzer_results)
            if check_overlaps:
                anonymizer_results = anonymizer.anonymize(
                    analyze_results=analyzer_results
                )
                fixed_entities = fix_entities(anonymizer_results)
            # else:
            # TO-DO: convert create_obj to a function that can be used with dicts of reviews.
            # fixed_entities = create_obj(analyzer_results, batch_dict["REVIEW"])
            results = pd.DataFrame(fixed_entities)

            results.to_csv(fp, header=False, index=False)
    print("\nDone!")


# because we use n-calls, the warning is annoying as it repeats itself all the time
analyze_batch = Analyzer("bert-base-cased", type="batch")
warnings.filterwarnings(
    "ignore", message="You seem to be using the pipelines sequentially on GPU."
)
model_results(
    analyze_batch,
    input_path="testing-data/cleaned_sentences_from_db3.csv",
    output_path="testing-data/output_from_db3.csv",
)
