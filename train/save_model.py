from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification, pipeline
import torch

ner_labels = [
    "O",
    "B-PER",
    "I-PER",
    "B-PHO",
    "I-PHO",
    "B-ADDR",
    "I-ADDR",
    "B-CITY",
    "I-CITY",
    "B-COUNTRY",
    "I-COUNTRY",
    "B-EMA",
    "I-EMA",
]
# labels and respective ids are required to
# support inference API on huggingFace website

id2label = {str(i): label for i, label in enumerate(ner_labels)}
label2id = {value: key for key, value in id2label.items()}

model_checkpoint = "gonzazelinka/custom-bert-model-PII"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForTokenClassification.from_pretrained(
    model_checkpoint, num_labels=len(ner_labels), id2label=id2label, label2id=label2id
)
device = 0 if torch.cuda.is_available() else -1
pipeline = pipeline(
    "ner",
    model=AutoModelForTokenClassification.from_pretrained(model_checkpoint),
    tokenizer=AutoTokenizer.from_pretrained(model_checkpoint),
    # Will attempt to group sub-entities to word level
    aggregation_strategy="simple",
    device=device,
    framework="pt",
)
model_max_length = pipeline.tokenizer.model_max_length
print(model_max_length)
# repo_name = "custom-bert-model-PII"
# model.save_pretrained(repo_name, push_to_hub=True)
# tokenizer.push_to_hub(repo_name)
