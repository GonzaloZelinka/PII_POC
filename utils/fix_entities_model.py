import json

def fix_entities_to_eval(input_path, output_path):
    # Read the input JSON file
    with open(input_path, "r", encoding="ISO-8859-1") as f:
        json_data = f.read()
    # Load the JSON data into a Python list
    data_to_check = json.loads(json_data)
    # Loop over each item in the list
    for js in data_to_check:
        # Remove entities with "O" entity value
        js["ENTITIES"] = [ent for ent in js["ENTITIES"] if ent["entity"] != "O"]

        # Fix overlapping entities and combine entities with a single character distance
        entities_clean = []
        i = 0 
        # Loop over each entity in the current item
        # print("js[ENTITIES]: ", js["ENTITIES"])
        while i < len(js["ENTITIES"]):
            j = i + 1
            new_entity = js["ENTITIES"][i]
            # Combine adjacent entities that have the same type and are next to each other
            while j < len(js["ENTITIES"]):
                if (js["ENTITIES"][j]['entity'] != js["ENTITIES"][i]['entity'] 
                    or int(js["ENTITIES"][j]["start"]) - int(js["ENTITIES"][i]["end"]) > 1):
                    # If the next entity is not the same type or is not adjacent, stop combining entities
                    break
                new_entity["end"] = int(js["ENTITIES"][j]["end"])
                # print("new_entity end: ", new_entity["end"])
                new_entity["text"] = new_entity["text"] + " " + js["ENTITIES"][j]["text"]
                # print("new_entity text: ", new_entity["text"])
                j += 1

            entities_clean.append(new_entity)
            i = j
        # Update the current item with the cleaned entities
        # print("entities_clean final: ", entities_clean)
        js["ENTITIES"] = entities_clean
    # Write the updated JSON data to the output file
    with open(output_path, 'w', encoding="ISO-8859-1") as fp:
        json.dump(data_to_check, fp)