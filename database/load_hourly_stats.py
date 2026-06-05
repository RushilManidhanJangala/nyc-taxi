import pandas as pd
import psycopg2

# Read CSV
df = pd.read_csv("data/hourly_stats.csv")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="nyc_taxi_db",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

# Clear old data
cursor.execute("DELETE FROM hourly_stats")

# Insert rows
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO hourly_stats
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            int(row["pickup_hour"]),
            int(row["total_trips"]),
            float(row["avg_fare"]),
            float(row["avg_distance"]),
            float(row["total_revenue"])
        )
    )

conn.commit()

print(f"{len(df)} rows inserted successfully.")

cursor.close()
conn.close()