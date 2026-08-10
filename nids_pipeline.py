import pandas as pd
import glob
import os

# Path to dataset folder
DATASET_PATH = "dataset"

# Get all parquet files
files = glob.glob(os.path.join(DATASET_PATH, "*.parquet"))

print("Number of files found:", len(files))
print()

dataframes = []

for file in files:
    print("Loading:", file)

    df = pd.read_parquet(file)

    print("Shape:", df.shape)

    dataframes.append(df)

print("\nMerging all datasets...")

# Merging
data = pd.concat(dataframes, ignore_index=True)

print("\nFinal Dataset Shape:", data.shape)

print("\nColumns in Dataset:")
print(data.columns)

print("\nSample Data:")
print(data.head())

print("\nChecking Label Distribution...\n")

label_counts = data["Label"].value_counts()

print(label_counts)

print("\nPercentage Distribution:\n")

label_percentage = (label_counts / len(data)) * 100

print(label_percentage)