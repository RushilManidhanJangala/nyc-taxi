import pandas as pd

# Load dataset
df = pd.read_parquet(
    "/opt/airflow/project/data/yellow_tripdata_2025-01.parquet"
)

print(f"Original Rows: {len(df)}")

# Data Cleaning
df = df[df["trip_distance"] > 0]
df = df[df["fare_amount"] > 0]

print(f"Rows After Cleaning: {len(df)}")

# ---------------------------
# Feature Engineering
# ---------------------------

# Trip Duration in Minutes
df["trip_duration_min"] = (
    df["tpep_dropoff_datetime"]
    -
    df["tpep_pickup_datetime"]
).dt.total_seconds() / 60

# Pickup Hour
df["pickup_hour"] = (
    df["tpep_pickup_datetime"]
).dt.hour

# Pickup Day Name
df["pickup_day"] = (
    df["tpep_pickup_datetime"]
).dt.day_name()

# Pickup Month
df["pickup_month"] = (
    df["tpep_pickup_datetime"]
).dt.month

print("\nNew Columns Added:")
print([
    "trip_duration_min",
    "pickup_hour",
    "pickup_day",
    "pickup_month"
])

# Save processed data
df.to_parquet(
    "/opt/airflow/project/data/processed_taxi_data.parquet"
)

print("\nProcessed dataset saved.")