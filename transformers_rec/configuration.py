BERT_DEID_CONFIGURATION = {
    "PRESIDIO_SUPPORTED_ENTITIES": [
        "LOCATION",
        "PERSON",
        "PHONE_NUMBER",
        "EMAIL",
        "ZIP",
    ],
    "DEFAULT_MODEL_PATH": "obi/deid_roberta_i2b2",
    "LABELS_TO_IGNORE": ["O"],
    "DEFAULT_EXPLANATION": "Identified as {} by the obi/deid_roberta_i2b2 NER model",
    "SUB_WORD_AGGREGATION": "simple",
    "DATASET_TO_PRESIDIO_MAPPING": {
        "DATE": "DATE_TIME",
        "DOCTOR": "PERSON",
        "PATIENT": "PERSON",
        "HOSPITAL": "O",
        "MEDICALRECORD": "O",
        "IDNUM": "O",
        "ORGANIZATION": "O",
        "ZIP": "O",
        "PHONE": "PHONE_NUMBER",
        "USERNAME": "",
        "STREET": "LOCATION",
        "PROFESSION": "PROFESSION",
        "COUNTRY": "LOCATION",
        "LOCATION-OTHER": "LOCATION",
        "FAX": "PHONE_NUMBER",
        "EMAIL": "EMAIL",
        "STATE": "LOCATION",
        "DEVICE": "O",
        "ORG": "O",
        "AGE": "AGE",
    },
    "MODEL_TO_PRESIDIO_MAPPING": {
        "PER": "PERSON",
        "LOC": "LOCATION",
        "ORG": "O",
        "AGE": "O",
        "ID": "O",
        "EMAIL": "EMAIL",
        "PATIENT": "PERSON",
        "STAFF": "PERSON",
        "HOSP": "O",
        "PATORG": "O",
        "DATE": "O",
        "PHONE": "PHONE_NUMBER",
    },
    "CHUNK_OVERLAP_SIZE": 40,
    "CHUNK_SIZE": 600,
}