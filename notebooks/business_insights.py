import pandas as pd

df = pd.read_csv(
    "data/hourly_stats.csv"
)

print("\n========== PEAK DEMAND HOUR ==========")

peak_hour = (
    df.sort_values(
        "total_trips",
        ascending=False
    )
    .head(1)
)

print(peak_hour)

print("\n========== HIGHEST REVENUE HOUR ==========")

revenue_hour = (
    df.sort_values(
        "total_revenue",
        ascending=False
    )
    .head(1)
)

print(revenue_hour)

print("\n========== HIGHEST AVERAGE FARE ==========")

fare_hour = (
    df.sort_values(
        "avg_fare",
        ascending=False
    )
    .head(1)
)

print(fare_hour)