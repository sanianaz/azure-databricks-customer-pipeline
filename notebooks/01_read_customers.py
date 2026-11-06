# Import PySpark functions
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \
    .appName("Customer Data Pipeline") \
    .getOrCreate()

# Read customer CSV file
df = spark.read.csv(
    "data/landing/customers.csv",
    header=True,
    inferSchema=True
)

# Display customer data
df.show()

# Display column names
print(df.columns)

# Display data types
df.printSchema()
