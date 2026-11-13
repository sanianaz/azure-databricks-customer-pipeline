# Azure Databricks Customer Data Pipeline

## 1. Project Overview

This project demonstrates a customer data pipeline built using Python, PySpark and Apache Spark.

The pipeline reads customer data from a CSV file, processes it through three data layers (Bronze, Silver and Gold), and creates a business summary showing the number of customers in each country.

The project is currently developed and tested locally. Azure services and Databricks integration are planned future enhancements.

## 2. Project Architecture

The pipeline follows the Medallion Architecture:

**Landing → Bronze → Silver → Gold**

- **Landing:** Stores the original customer CSV file.
- **Bronze:** Stores the raw customer data in Parquet format.
- **Silver:** Removes duplicate customer IDs and creates a full_name column.
- **Gold:** Groups customers by country and calculates the customer count.

## 3. Technologies Used

- Python
- PySpark
- Apache Spark
- Parquet
- Git and GitHub

## 4. Project Structure

```text
azure-databricks-customer-pipeline/
├── data/
│   ├── landing/
│   │   └── customers.csv
│   └── README.md
├── notebooks/
│   ├── 01_read_customers.py
│   ├── 02_clean_customers.py
│   └── 03_create_gold.py
├── README.md
└── .gitignore
```
Note: The Bronze, Silver and Gold folders are generated locally when the pipeline runs. They are excluded from GitHub using .gitignore.

## 5. How to Run the Project

Activate the Python virtual environment and install PySpark:

```bash
python -m pip install pyspark==4.3.0
```

Run the pipeline scripts in this order:

```bash
python notebooks/01_read_customers.py
python notebooks/02_clean_customers.py
python notebooks/03_create_gold.py
```

## 6. Gold Layer Output

The Gold layer provides the following customer summary:

| Country | Customer Count |
|---|---:|
| UK | 3 |
| Sweden | 2 |
| France | 2 |
| USA | 1 |

Total customers: 8

## 7. Future Enhancements

- Integrate Azure Data Lake Storage Gen2.
- Run data processing using Azure Databricks.
- Use Azure Data Factory to orchestrate the pipeline.
- Implement data quality checks.
- Explore Delta Lake and Unity Catalog.
- Add automated deployment and CI/CD.
