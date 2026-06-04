import pandas as pd

df = pd.read_parquet(
    "data/processed_taxi_data.parquet"
)

print(df[
    [
        "trip_duration_min",
        "pickup_hour",
        "pickup_day",
        "pickup_month"
    ]
].head())