
# ==========================================
# GOLD LAYER - CUSTOMER SUMMARY
# ==========================================

# 1. Import SparkSession
from pyspark.sql import SparkSession

# 2. Create Spark session
spark = SparkSession.builder \
    .appName("Customer Gold Pipeline") \
    .getOrCreate()

# 3. Read data from Silver layer
df = spark.read.parquet("data/silver/customers")

# 4. Count customers in each country
gold_df = df.groupBy("country").count()

# 5. Display the summary
gold_df.show()

# 6. Save the summary to Gold layer
gold_df.write \
    .format("parquet") \
    .mode("overwrite") \
    .save("data/gold/customers_by_country")

# 7. Stop Spark session
spark.stop()
