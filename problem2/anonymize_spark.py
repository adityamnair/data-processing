from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import hashlib

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("CSV Anonymization") \
    .config("spark.master", "local[*]") \
    .getOrCreate()

# Define anonymization functions
def anonymize_text(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

anonymize_udf = udf(anonymize_text, StringType())

# Read large CSV file into Spark DataFrame
df = spark.read.option("header", "true").csv("input.csv")

# Anonymize specified columns
df_anonymized = df.withColumn("first_name", anonymize_udf("first_name")) \
                 .withColumn("last_name", anonymize_udf("last_name")) \
                 .withColumn("address", anonymize_udf("address"))

# Write anonymized DataFrame to new CSV file
df_anonymized.coalesce(1).write.option("header", "true").csv("output.csv")

# Stop SparkSession
spark.stop()
