from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("TaxiProject")
    .getOrCreate()
)

print("Spark Session Created Successfully!")

spark.stop()