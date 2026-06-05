from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("TaxiAnalytics")
    .getOrCreate()
)

df = spark.read.parquet(
    "data/yellow_tripdata_2025-01.parquet"
)

print("\nSchema:")
df.printSchema()

print("\nTotal Rows:")
print(df.count())

print("\nFirst 5 Rows:")
df.show(5)

spark.stop()