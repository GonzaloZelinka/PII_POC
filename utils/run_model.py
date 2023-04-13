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
    for batch in pd.read_csv(input_path, encoding="ISO-8859-1",header=0, names=Config.columns, chunksize=Config.chunksize):
      with open(output_path, "a", encoding="ISO-8859-1") as fp:
        # Extract the review column
        all_values = batch.values.tolist()
        data_list = batch.iloc[:, Config.number_column_review].tolist()
        print(f"getting results for the ner model and presidio. Progressively writing the results in {output_path}...")
        # Process the texts as batch for improved performance
        nlp_artifacts_batch: Iterator[
            Tuple[str, NlpArtifacts]
        ] = analyzer_engine.nlp_engine.process_batch(
            texts=data_list, language="en"
        )

        anonymizer = Anonymizer()
        for i, (text, nlp_artifacts) in tqdm(enumerate(nlp_artifacts_batch), total=len(data_list)):
          results = analyzer.analyze(
            text=str(text), nlp_artifacts=nlp_artifacts, language="en", entities=Config.entities, score_threshold=Config.threshold
          )
          result = []
          if Config.check_overlaps:
                text_anon = anonymizer.anonymize(data_list[i], results)
                text_anon = sorted(text_anon.items, key=lambda x: x.start)
                for i, res in enumerate(text_anon):
                    result.append({"start": res.start, "end": res.end, "entity": res.entity_type, "text": res.text})
          else:
              result = create_obj(result, data_list[i])
          final_result = {"SITE_URL": all_values[i][0],"PVID": all_values[i][1], "TEXT": data_list[i], "ENTITIES": result}
          json.dump(final_result, fp)
      
      # fp=open(output_path,'a', encoding="ISO-8859-1") # output file
      # json.dump(final_result, fp) 
    print("Done!") 