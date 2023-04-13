from Config import Config
from general_functions import anonymize, analyzer_engine



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

def process_review2(value):
    analyzer = analyzer_engine("obi/deid_roberta_i2b2") # "en_core_web_lg" or "obi/deid_roberta_i2b2"
    review = value[Config.number_column_review]
    final_result = []
    results = analyzer.analyze(
        text=str(review), language="en", entities=Config.entities, score_threshold=Config.threshold
    )
    result = []
    if Config.check_overlaps:
        text_anon = anonymize(review, results)
        text_anon = sorted(text_anon.items, key=lambda x: x.start)
        for res in enumerate(text_anon):
          if hasattr(res, "entity_type"):
            result.append({"start": res.start, "end": res.end, "entity": res.entity_type, "text": res.text})
    else:
        result = create_obj(result, review)
    final_result.append({"SITE_URL": value[0],"PVID": value[1], "TEXT": review, "ENTITIES": result})
    return final_result