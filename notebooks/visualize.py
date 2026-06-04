import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/hourly_stats.csv"
)

# Trips by Hour

plt.figure(figsize=(10,5))

plt.plot(
    df["pickup_hour"],
    df["total_trips"]
)

plt.title("Trips by Hour")
plt.xlabel("Hour")
plt.ylabel("Total Trips")

plt.savefig(
    "reports/trips_by_hour.png"
)

plt.close()

# Revenue by Hour

plt.figure(figsize=(10,5))

plt.plot(
    df["pickup_hour"],
    df["total_revenue"]
)

plt.title("Revenue by Hour")
plt.xlabel("Hour")
plt.ylabel("Revenue")

plt.savefig(
    "reports/revenue_by_hour.png"
)

plt.close()

print("Charts saved successfully.")