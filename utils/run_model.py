
import csv
import json
import os
import sys

import pandas as pd
from tqdm import tqdm

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from transformers_rec import Analyzer, Anonymizer


def create_obj(an_r, text):
    """Show results of analyze() in a dataframe."""
    ents = []
    for r in an_r:
      info = r.to_dict()
      ent ={ "start": info["start"], 
              "end": info['end'], 
              "confidence": info['score'], 
              "entity": info['entity_type'], 
              "text": text[info["start"]:info["end"]]} 
      ents.append(ent)
    return ents


def model_results(input_path, output_path, batch_size=2000, columns=["SITE_URL","ITEM_GROUP_ID","PVID","REVIEW"], threshold=0.5, check_overlaps=True, entities=["PERSON", "LOCATION", "PHONE_NUMBER", "EMAIL_ADDRESS","CREDIT_CARD", "US_SSN"]):
    """
    Runs a Presidio model with n_calls, reading input data from a CSV file and writing output data to another CSV file.

    Arguments:
    input_path -- str: the path to the input CSV file, which should have the following columns:
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
    output_path -- str: the path to the output CSV file.
    batch_size -- int: the number of rows to read from the input CSV file at a time.
    columns -- list of str: the names of the columns in the input CSV file.
    threshold -- float: the minimum score for an entity to be returned.
    check_overlaps -- bool: if True, the model will not recognize overlapping entities. If False, the model will recognize overlapping entities and return all of entities and the precision/score for each entity.
    entities -- list of str: the entities to recognize.
    Returns:
    None
    """
    analyzer = Analyzer("obi/deid_roberta_i2b2") # "en_core_web_lg" or "obi/deid_roberta_i2b2"

    # get the total number of rows in the CSV file
    total_rows = pd.read_csv(input_path, usecols=[0]).shape[0]
    print(f"getting results for the ner model and presidio. Progressively writing the results in {output_path}...")
    progress_bar = tqdm(total=total_rows)
    with open(output_path, "a", encoding="ISO-8859-1") as fp:
      writer = csv.writer(fp)
       # Write the header row
      writer.writerow(['SITE_URL', 'ITEM_GROUP_ID', 'PVID', 'TEXT', 'ENTITIES'])
      anonymizer = Anonymizer()

      for batch in pd.read_csv(input_path, encoding="ISO-8859-1", chunksize=batch_size, names=columns, header=0):
         for row in batch.iterrows():
          site_url = row[1]['SITE_URL']
          item_group_id = row[1]['ITEM_GROUP_ID']
          pvids = row[1]['PVID']
          review = row[1]['REVIEW']

          results = analyzer.analyze(
            text=str(review), language="en", entities=entities, score_threshold=threshold
          )
          result = []
          if check_overlaps:
                text_anon = anonymizer.anonymize(str(review), results)
                text_anon = sorted(text_anon.items, key=lambda x: x.start)
                for res in text_anon:
                    result.append({"start": res.start, "end": res.end, "entity": res.entity_type, "text": res.text})
          else:
              result = create_obj(result, review)
          row = [site_url, item_group_id, eval(pvids), review, json.dumps(result)]
          writer.writerow(row)
          progress_bar.update(1)
    print("\nDone!") 
