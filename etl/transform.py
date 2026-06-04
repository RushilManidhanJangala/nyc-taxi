import pandas as pd

# Load dataset
df = pd.read_parquet(
    "data/yellow_tripdata_2025-01.parquet"
)

print(f"Original Rows: {len(df)}")

# Remove invalid trips
df = df[df["trip_distance"] > 0]

df = df[df["fare_amount"] > 0]

print(f"Rows After Cleaning: {len(df)}")

# Save cleaned dataset
df.to_parquet(
    "data/cleaned_taxi_data.parquet",
    index=False
)

print("Cleaned dataset saved successfully.")