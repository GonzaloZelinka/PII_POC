import matplotlib
import numpy as np
import pandas as pd
from datasets import load_dataset
from transformers import (AutoModelForTokenClassification, AutoTokenizer,
                          DataCollatorForTokenClassification, Trainer,
                          TrainingArguments)

# Loading helper function to compute metrics
metric = load_metric("seqeval")

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

model_checkpoint = "train/checkpoint-4500"

model = AutoModelForTokenClassification.from_pretrained(
    model_checkpoint, num_labels=len(ner_labels)
)

# Specifying training arguments

batch_size = 32

args = TrainingArguments(
    model_checkpoint,
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    num_train_epochs=5,
    weight_decay=0.01,
)


trainer = Trainer(
    model,
    args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

predictions, labels, _ = trainer.predict(tokenized_dataset["validation"])
predictions = np.argmax(predictions, axis=2)

true_predictions = [
    [ner_labels[p] for (p, l) in zip(prediction, label) if l != -100]
    for prediction, label in zip(predictions, labels)
]
true_labels = [
    [ner_labels[l] for (p, l) in zip(prediction, label) if l != -100]
    for prediction, label in zip(predictions, labels)
]

results = metric.compute(predictions=true_predictions, references=true_labels)


results_df = pd.DataFrame(
    {
        "PHO": results["PHO"],
        "ADDR": results["ADDR"],
        "CITY": results["CITY"],
        "COUNTRY": results["COUNTRY"],
        "EMA": results["EMA"],
        "PER": results["PER"],
    }
).drop("number", axis=0)

print(results_df)


results_df.plot(kind="bar", rot=0, figsize=(12, 8))
matplotlib.pyplot.title("Performance on Evaluate data")
matplotlib.pyplot.show()

