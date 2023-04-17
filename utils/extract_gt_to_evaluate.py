import json
import re
from typing import List

import pandas as pd


def get_span_indx(labels: List[str], words: List[str], sentence: str) -> List[tuple]:
    """Gets span starts and ends for Spacy spancat component.

    Returns list of tuples where the first element of the
    tuple is the span start, the second element of the tuple
    is the span end and the third element of the tuple is
    the span category.
    """
    # gets list of indices corresponding to labelled words
    label_indx = []
    temp_list = []

    for i, l in enumerate(labels):
        if l != "O":
            temp_list.append(i)
        else:
            label_indx.append(temp_list)
            temp_list = []
        if i == len(labels) - 1:
            label_indx.append(temp_list)

    clean_label_indx = [x for x in label_indx if len(x) > 0]

    spans = []
    for indx in clean_label_indx:
        if len(indx) == 1:
            span = words[indx[0]]
            label = labels[indx[0]].upper()
        else:
            span = " ".join([words[i] for i in indx])
            label = [labels[i].upper() for i in indx][0]
        # remove punctuation and strip whitespace for spans
        span_clean = span.strip()
        for m in re.finditer(re.escape(span_clean), sentence):
            spans.append(
                {"start": m.start(), "end": m.end(), "entity": label, "text": m.group()}
            )

    return spans


def transform_csv_annotated_to_json(input_path, output_path=None):
    """
    Transforms csv file with annotated data to json file for training spacy spancat component.
    Arguments:
    input_path -- str: the path to the input CSV file, which should have the following columns:

        - Review # : int or str
        - Word : str
        - Tag : str

    Example: https://www.kaggle.com/datasets/debasisdotcom/name-entity-recognition-ner-dataset

    output_path -- str: the path to the output JSON file.

    Returns:
    list of str: list of {"TEXT": sentence, "ENTITIES": span_ents}
        - Example:
        [{ "TEXT": "I live in Argentina",
            "ENTITIES": [
                {
                    "start": 10,
                    "end": 19,
                    "entity": "LOC",
                    "text": "Argentina"
                }
            ]
        }]
    """
    DATA = []
    data = pd.read_csv(input_path, encoding="ISO-8859-1").fillna(method="ffill")
    for sent, sent_info in data.groupby("Review #"):
        words = list(sent_info["Word"])
        # convert words to sentence and get rid of spaces between punctuation characters
        sentence = re.sub(r'\s([?.!"](?:\s|$))', r"\1", " ".join(words))
        # get labels
        labels = list(sent_info["Tag"])
        # identify token span start, span ends and span category
        span_ents = get_span_indx(labels, words, sentence)
        DATA.append({"TEXT": sentence, "ENTITIES": span_ents})
    if output_path:
        with open(output_path, "w") as fp:
            json.dump(DATA, fp)
    return DATA
