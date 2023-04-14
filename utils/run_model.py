
import csv
import json
from typing import Iterator, Tuple

import pandas as pd
from presidio_analyzer.nlp_engine import NlpArtifacts
from tqdm import tqdm

from Config import Config
import os
import sys
import warnings
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from transformers_rec import (Analyzer, Anonymizer)


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

    # get the total number of rows in the CSV file
    total_rows = pd.read_csv(input_path, usecols=[0]).shape[0]
    print(f"getting results for the ner model and presidio. Progressively writing the results in {output_path}...")
    progress_bar = tqdm(total=total_rows)
    with open(output_path, "a", encoding="ISO-8859-1") as fp:
      writer = csv.writer(fp)
       # Write the header row
      writer.writerow(['SITE_URL', 'ITEM_GROUP_ID', 'PVID', 'TEXT', 'ENTITIES'])
      anonymizer = Anonymizer()

      for batch in pd.read_csv(input_path, encoding="ISO-8859-1", chunksize=Config.BATCH_SIZE, names=Config.columns, header=0):
         for row in batch.iterrows():
          site_url = row[1]['SITE_URL']
          item_group_id = row[1]['ITEM_GROUP_ID']
          pvids = row[1]['PVID']
          review = row[1]['REVIEW']

          results = analyzer.analyze(
            text=str(review), language="en", entities=Config.entities, score_threshold=Config.threshold
          )
          result = []
          if Config.check_overlaps:
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

warnings.filterwarnings("ignore", message="You seem to be using the pipelines sequentially on GPU.")
model_results(input_path="testing-data/cleaned_sentences_from_db2.csv", output_path="testing-data/output_from_db2.csv")