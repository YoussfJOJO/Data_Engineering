In this project I did the next:

- Developed a data processing pipeline using PySpark in Databricks to process multiple retail datasets, including customers, orders, products, and order items.

- Implemented dynamic schema handling by reading column definitions from a JSON metadata file and automatically assigning column names based on column positions.

- Loaded raw CSV datasets, inferred data types using Spark's inferSchema option, and transformed the data into structured Spark DataFrames.

- Exported processed datasets to Parquet format using PySpark, enabling efficient columnar storage for downstream analytics.

- Performed data analysis using Spark DataFrame operations, including grouping, aggregation, and sorting to summarize order counts by order status.

- Utilized Databricks Unity Catalog Volumes to organize and access source data and store processed datasets.
