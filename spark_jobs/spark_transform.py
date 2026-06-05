from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    hour,
    unix_timestamp
)

spark = (
    SparkSession.builder
    .appName("TaxiSparkTransform")
    .getOrCreate()
)

# Load Data

df = spark.read.parquet(
    "data/yellow_tripdata_2025-01.parquet"
)

print(f"Original Rows: {df.count()}")

# ------------------
# Data Cleaning
# ------------------

df = df.filter(
    col("trip_distance") > 0
)

df = df.filter(
    col("fare_amount") > 0
)

print(f"Rows After Cleaning: {df.count()}")

# ------------------
# Feature Engineering
# ------------------

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

print("\nSchema After Transformation")

df.printSchema()

print("\nSample Rows")

df.select(
    "pickup_hour",
    "trip_duration_min",
    "fare_amount"
).show(5)

spark.stop()