
# ==========================================
# BRONZE LAYER - READ CUSTOMER DATA
# ==========================================

# 1. Import SparkSession
from pyspark.sql import SparkSession

# 2. Create Spark session
spark = SparkSession.builder \
    .appName("Customer Bronze Pipeline") \
    .getOrCreate()

# 3. Read customer CSV file
df = spark.read.csv(
    "data/landing/customers.csv",
    header=True,
    inferSchema=True
)

# 4. Display original customer data
print("Original customer data:")
df.show(truncate=False)

# 5. Display schema
print("Customer data schema:")
df.printSchema()

# 6. Count customers
print("Total customers:", df.count())

# 7. Write raw data to Bronze layer
df.write \
    .format("parquet") \
    .mode("overwrite") \
    .save("data/bronze/customers")

print("Bronze layer created successfully!")

# 8. Stop Spark session
spark.stop()
