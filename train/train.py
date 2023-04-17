from datasets import load_dataset, load_metric
from transformers import (
    AutoTokenizer,
    DataCollatorForTokenClassification,
    AutoModelForTokenClassification,
    TrainingArguments,
    Trainer,
)
import numpy as np


def align_labels_and_tokens(word_ids, labels):
    """Aligns tokens and their respective labels

    Args:
        word_ids (list): word ids of tokens after subword tokenization.
        labels (list): original labels irrespective of subword tokenization.

    Returns:
        updated_labels (list): labels aligned with respective tokens.

    """

    updated_labels = []
    current_word = None
    for word_id in word_ids:
        if word_id != current_word:
            current_word = word_id
            updated_labels.append(-100 if word_id is None else labels[word_id])
        elif word_id is None:
            updated_labels.append(-100)
        else:
            label = labels[word_id]
            # B-XXX to I-XXX for subwords (Inner entities)
            if label % 2 == 1:
                label += 1
            updated_labels.append(label)
    return updated_labels


def tokenize_and_align_labels(dataset):
    """Performs tokenization and aligns all tokens and labels
        in the dataset.

    Args:
        dataset (DatasetDict): dataset containing tokens and labels.

    Returns:
        tokenized_data (dict): contains input_ids, attention_mask, token_type_ids, labels

    """
    dataset["tokens"] = [eval(tokens) for tokens in dataset["tokens"]]
    dataset["ner_tags"] = [eval(tags) for tags in dataset["ner_tags"]]
    tokenized_data = tokenizer(
        dataset["tokens"], truncation=True, is_split_into_words=True
    )
    all_labels = dataset["ner_tags"]
    updated_labels = []
    for i, labels in enumerate(all_labels):
        updated_labels.append(
            align_labels_and_tokens(tokenized_data.word_ids(i), labels)
        )
    tokenized_data["labels"] = updated_labels
    return tokenized_data


def compute_metrics(p):
    """Computes and returns metrics during training.

    Args:
        p (tuple): tuple containing predictions, labels as lists.

    Returns:
        dict: Dictionary containing precision, recall, f1 score, accuracy.

    """

    predictions, labels = p
    predictions = np.argmax(predictions, axis=2)
    true_predictions = [
        [ner_labels[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_labels = [
        [ner_labels[l] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    metrics = metric.compute(predictions=true_predictions, references=true_labels)

    return {
        "precision": metrics["overall_precision"],
        "recall": metrics["overall_recall"],
        "f1": metrics["overall_f1"],
        "accuracy": metrics["overall_accuracy"],
    }


data_files = {
    "train": "train/train.csv",
    "validation": "train/validation.csv",
}
raw_dataset = load_dataset("csv", encoding="ISO-8859-1", data_files=data_files)

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

id2label = {str(i): label for i, label in enumerate(ner_labels)}
label2id = {value: key for key, value in id2label.items()}

model_checkpoint = "bert-base-cased"

tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)


tokenized_dataset = raw_dataset.map(
    tokenize_and_align_labels,
    batched=True,
    remove_columns=raw_dataset["train"].column_names,
)


data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)

model = AutoModelForTokenClassification.from_pretrained(
    model_checkpoint, num_labels=len(ner_labels), id2label=id2label, label2id=label2id
)

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

metric = load_metric("seqeval")

trainer = Trainer(
    model,
    args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
)

trainer.train()  # Fine-tunes model on downstream task
