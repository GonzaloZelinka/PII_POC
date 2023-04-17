import pandas as pd

# read the input CSV file into a DataFrame
df = pd.read_csv("testing-data/output_test_data_pii_filtered.csv")

# specify the column name or index to drop
column_to_drop = "ENTITIES"  # or 2 for the 3rd column

# drop the specified column and save the result to a new CSV file
df.drop(column_to_drop, axis=1).to_csv(
    "testing-data/output_test_data_pii_filtered_cleaned.csv", index=False
)
