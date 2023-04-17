from typing import Dict


def fix_entities(data: Dict):
    """
    Fixes entities in the JSON file to evaluate the model, merging consecutive entities which should be considered as one entity as one, removing entities with "O" entity value.
    Arguments:
    :param data: -- Dict: The REVIEW element must have the following format:
        - REVIEW: str. Represent a review. Whit this format:
        [{
            "text": I live in Argentina.
            "entities": [
                {'start': 10, 'end': 19, 'label': 'LOCATION', 'text': 'Argentina'},
            ]
        }]


    Returns:
    Dict"""
    for js in data["REVIEW"]:
        if isinstance(js, Dict) and len(js["entities"]) > 0:
            # Remove entities with "O" entity value
            js["entities"] = [ent for ent in js["entities"] if ent["label"] != "O"]

            # Fix overlapping entities and combine entities with a single character distance
            entities_clean = []
            i = 0
            # Loop over each entity in the current item
            while i < len(js["entities"]):
                j = i + 1
                new_entity = js["entities"][i]
                # Combine adjacent entities that have the same type and are next to each other
                while j < len(js["entities"]):
                    if (
                        js["entities"][j]["label"] != js["entities"][i]["label"]
                        or int(js["entities"][j]["start"])
                        - int(js["entities"][i]["end"])
                        > 1
                    ):
                        # If the next entity is not the same type or is not adjacent, stop combining entities
                        break
                    new_entity["end"] = int(js["entities"][j]["end"])
                    new_entity["text"] = (
                        new_entity["text"] + " " + js["entities"][j]["text"]
                    )
                    j += 1
                if len(new_entity["text"]) > 3:
                    entities_clean.append(new_entity)
                i = j
            # Update the current item with the cleaned entities
            js["entities"] = entities_clean
    return data
