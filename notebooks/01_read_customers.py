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

# Select required columns
selected_df = df.select(
    "customer_id",
    "first_name",
    "last_name",
    "email",
    "city",
    "country"
)

selected_df.show()

# Filter customers from Sweden
sweden_df = df.filter(df.country == "Sweden")

sweden_df.show()

from pyspark.sql.functions import concat_ws

# Create full_name column
df = df.withColumn(
    "full_name",
    concat_ws(" ", df.first_name, df.last_name)
)

df.show()

# Remove duplicate customer IDs
cleaned_df = df.dropDuplicates(["customer_id"])

cleaned_df.show()

# Count total customers
print("Total customers:", cleaned_df.count())
