import pandas as pd

# Load processed data
df = pd.read_parquet(
    "data/processed_taxi_data.parquet"
)

# Aggregate metrics by pickup hour
hourly_stats = (
    df.groupby("pickup_hour")
    .agg(
        total_trips=("pickup_hour", "count"),
        avg_fare=("fare_amount", "mean"),
        avg_distance=("trip_distance", "mean"),
        total_revenue=("total_amount", "sum")
    )
    .reset_index()
)

# Round values
hourly_stats["avg_fare"] = (
    hourly_stats["avg_fare"]
    .round(2)
)

hourly_stats["avg_distance"] = (
    hourly_stats["avg_distance"]
    .round(2)
)

hourly_stats["total_revenue"] = (
    hourly_stats["total_revenue"]
    .round(2)
)

print(hourly_stats)

# Save results
hourly_stats.to_csv(
    "data/hourly_stats.csv",
    index=False
)

print("\nHourly analytics saved.")