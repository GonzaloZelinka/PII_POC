
import csv
import json
from typing import Iterator, Tuple

import pandas as pd
from presidio_analyzer.nlp_engine import NlpArtifacts
from tqdm import tqdm

from Config import Config
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


def model_results(input_path, output_path):
    analyzer = Analyzer("obi/deid_roberta_i2b2") # "en_core_web_lg" or "obi/deid_roberta_i2b2"
    analyzer_engine = analyzer.get_engine()

    final_result = []

    # get the total number of rows in the CSV file
    total_rows = pd.read_csv(input_path, usecols=[0]).shape[0]
    print(f"getting results for the ner model and presidio. Progressively writing the results in {output_path}...")
    progress_bar = tqdm(total=total_rows)
    for batch in pd.read_csv(input_path, encoding="ISO-8859-1", chunksize=Config.BATCH_SIZE):
      with open(output_path, "a", encoding="ISO-8859-1") as fp:
        writer = csv.writer(fp)
        # Write the header row
        writer.writerow(['SITE_URL', 'ITEM_GROUP_ID', 'PVID', 'TEXT', 'ENTITIES'])
        # Process the texts as batch for improved performance
        nlp_artifacts_batch: Iterator[
            Tuple[str, NlpArtifacts]
        ] = analyzer_engine.nlp_engine.process_batch(
            texts=batch, language="en"
        )

        anonymizer = Anonymizer()
        # for i, (text, nlp_artifacts) in tqdm(enumerate(nlp_artifacts_batch), total=len(data_list)):
        for i, (text, nlp_artifacts) in enumerate(nlp_artifacts_batch):
          new_text = text.split('[,]')
          results = analyzer.analyze(
            text=str(new_text[3]), nlp_artifacts=nlp_artifacts, language="en", entities=Config.entities, score_threshold=Config.threshold
          )
          result = []
          if Config.check_overlaps:
                text_anon = anonymizer.anonymize(new_text[3], results)
                text_anon = sorted(text_anon.items, key=lambda x: x.start)
                for i, res in enumerate(text_anon):
                    result.append({"start": res.start, "end": res.end, "entity": res.entity_type, "text": res.text})
          else:
              result = create_obj(result, new_text[3])
          row = [new_text[0], new_text[1], eval(new_text[2]), new_text[3], json.dumps(result)]
          # final_result = {"SITE_URL": new_text[0], "ITEM_GROUP_ID":new_text[1], "PVID": eval(new_text[2]), "TEXT": text[3], "ENTITIES": result}
          writer.writerow(row)
          progress_bar.update(1)
      # fp=open(output_path,'a', encoding="ISO-8859-1") # output file
      # json.dump(final_result, fp) 
    print("Done!") 