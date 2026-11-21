API Processing Project

Project Overview

This project demonstrates an end-to-end API data extraction and
processing workflow using six endpoints from the DummyJSON public API.
The goal is to retrieve JSON data, transform it into structured tabular
data, normalize nested fields, and load the resulting tables into
Databricks as Delta tables.

Data Sources

The project extracts data from these DummyJSON endpoints:

-   Products: https://dummyjson.com/products
-   Users: https://dummyjson.com/users
-   Carts: https://dummyjson.com/carts
-   Posts: https://dummyjson.com/posts
-   Comments: https://dummyjson.com/comments
-   Todos: https://dummyjson.com/todos

Processing Workflow

1.  API extraction
    -   Send HTTP GET requests to the six API endpoints using Python’s
        requests library.
    -   Read the JSON responses and convert the records into Pandas
        DataFrames.
2.  Data preparation and normalization
    -   Organize the source DataFrames for processing.
    -   Rename the comments identifier to comment_id to make its purpose
        clear.
    -   Flatten nested dictionary fields into regular columns.
    -   Identify list-valued fields and split their elements into
        separate child DataFrames.
    -   Flatten nested dictionaries found in those child DataFrames.
    -   Retain parent identifiers in child tables so that the related
        records can be connected.
3.  Load into Databricks
    -   Load the processed DataFrames into Databricks.
    -   Store the resulting tables in the workspace.API_TABLES
        schema/catalog location as Delta tables.
4.  Data validation
    -   Compare the row counts of the processed Pandas DataFrames with
        the corresponding Databricks tables.
    -   Confirm that the loaded tables contain the expected number of
        rows.
