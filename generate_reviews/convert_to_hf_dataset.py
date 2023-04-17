import pandas as pd
import datasets

# Load the CSV file using pandas
df = pd.read_csv(
    "generate_reviews/dataset/product_reviews10.csv", encoding="ISO-8859-1"
)

# Define the label classes
label_classes = [
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

# Define the dataset features
features = {
    "id": datasets.Value("string"),
    "tokens": datasets.Sequence(datasets.Value("string")),
    "ner_tags": datasets.Sequence(
        datasets.features.ClassLabel(
            names=[
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
        )
    ),
}

# Convert the pandas DataFrame to Hugging Face's Dataset format
dataset = datasets.from_pandas(df, features=features)

# Print the first few examples to check if the conversion was successful
print(dataset["train"][:5])
