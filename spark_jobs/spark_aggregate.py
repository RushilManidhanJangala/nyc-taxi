from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    hour,
    unix_timestamp,
    count,
    avg,
    sum
)

spark = (
    SparkSession.builder
    .appName("TaxiSparkAggregation")
    .getOrCreate()
)

# Load Data
df = spark.read.parquet(
    "data/yellow_tripdata_2025-01.parquet"
)

# Cleaning
df = df.filter(col("trip_distance") > 0)
df = df.filter(col("fare_amount") > 0)

# Feature Engineering
df = df.withColumn(
    "pickup_hour",
    hour("tpep_pickup_datetime")
)

df = df.withColumn(
    "trip_duration_min",
    (
        unix_timestamp("tpep_dropoff_datetime")
        -
        unix_timestamp("tpep_pickup_datetime")
    ) / 60
)

# Aggregation
hourly_stats = (
    df.groupBy("pickup_hour")
      .agg(
          count("*").alias("total_trips"),
          avg("fare_amount").alias("avg_fare"),
          avg("trip_distance").alias("avg_distance"),
          sum("total_amount").alias("total_revenue")
      )
      .orderBy("pickup_hour")
)

print("\nHourly Analytics")

hourly_stats.show(24)
print("Spark aggregation completed successfully.")
spark.stop()