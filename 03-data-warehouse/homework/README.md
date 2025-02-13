# Homework

## Question 1

Upload files from 2024-01 to 2024-06 to GCS.

Run on bigquery:

CREATE OR REPLACE EXTERNAL TABLE `careful-striker-450021-n5.nytaxi.external_yellow_tripdata_2024`
OPTIONS (
  format = 'parquet',
  uris = ['gs://kestra-de-zoomcamp-bucket-mh/yellow_tripdata_2024-*.parquet']
);

SELECT count(*) FROM `careful-striker-450021-n5.nytaxi.external_yellow_tripdata_2024`

Answer: 20332093

## Question 2

Run on bigquery:

CREATE OR REPLACE TABLE careful-striker-450021-n5.nytaxi.yellow_tripdata_2024 AS
SELECT * FROM careful-striker-450021-n5.nytaxi.external_yellow_tripdata_2024;

SELECT COUNT(distinct PULocationID) FROM careful-striker-450021-n5.nytaxi.yellow_tripdata_2024;

SELECT COUNT(distinct PULocationID) FROM careful-striker-450021-n5.nytaxi.external_yellow_tripdata_2024;

Answer: 0 MB for the External Table and 155.12 MB for the Materialized Table

## Question 3

Answer: BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

## Question 4

Run on bigquery;

SELECT COUNT(*) FROM careful-striker-450021-n5.nytaxi.yellow_tripdata_2024
WHERE fare_amount = 0 

Answer: 8333

## Question 5

Answer: Partition by tpep_dropoff_datetime and Cluster on VendorID

## Question 6

Answer: 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

## Question 7

Answer: GCP Bucket

## Question 8

Answer: False






