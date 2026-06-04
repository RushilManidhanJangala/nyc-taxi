import pandas as pd

# Load dataset
df = pd.read_parquet(
    "data/yellow_tripdata_2025-01.parquet"
)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMNS =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)