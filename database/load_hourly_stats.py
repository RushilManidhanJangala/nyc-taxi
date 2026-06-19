import pandas as pd
import psycopg2

# Read hourly stats CSV
df = pd.read_csv(
    "/opt/airflow/project/data/hourly_stats.csv"
)

# Connect to PostgreSQL container
conn = psycopg2.connect(
    host="postgres",
    database="nyc_taxi_db",
    user="airflow",
    password="airflow"
)

cursor = conn.cursor()

# Clear existing rows
cursor.execute("DELETE FROM hourly_stats")

# Insert data row by row
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO hourly_stats
        (
            pickup_hour,
            total_trips,
            avg_fare,
            avg_distance,
            total_revenue
        )
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

# Commit changes
conn.commit()

print(f"{len(df)} rows inserted successfully.")

# Close connections
cursor.close()
conn.close()