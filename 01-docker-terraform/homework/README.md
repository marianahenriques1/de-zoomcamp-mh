# Homework

## Question 1

docker run -it --entrypoint bash python:3.12.8
pip --version

Answer: The version of pip is 24.3.1

## Question 2

Hostname = the service name of the postgres database defined in the docker-compose.yaml = db.
Port = the container's internal port for postgres = 5432

Answer: db:5432

## Question 3 set up

run on the terminal: docker-compose up

then go to: http://localhost:8080/browser/ and add new server with hostname: pgdatabase and user/pass: root/root

then on the terminal run:

python ingest_data.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=green_trip_data \
  --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz"
  
python ingest_data.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=taxi_zone_data \
  --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"


### Question 3 query

SELECT
    CASE
        WHEN trip_distance <= 1 THEN 'Up to 1 mile'
        WHEN trip_distance > 1 AND trip_distance <= 3 THEN 'In between 1 (exclusive) and 3 miles (inclusive)'
        WHEN trip_distance > 3 AND trip_distance <= 7 THEN 'In between 3 (exclusive) and 7 miles (inclusive)'
        WHEN trip_distance > 7 AND trip_distance <= 10 THEN 'In between 7 (exclusive) and 10 miles (inclusive)'
        ELSE 'Over 10 miles'
    END AS distance_range,
    COUNT(*) AS trip_count
FROM green_trip_data
WHERE lpep_pickup_datetime >= '2019-10-01'
AND lpep_dropoff_datetime < '2019-11-01'
GROUP BY distance_range
ORDER BY trip_count DESC;

Answer: 104,802; 198,924; 109,603; 27,678; 35,189

### Question 4 query

SELECT DATE(lpep_pickup_datetime) as day
FROM public.green_trip_data
WHERE trip_distance = (
    SELECT MAX(trip_distance)
    FROM public.green_trip_data
);

Answer: 2019-10-31

### Question 5 query




## Question 7

Answer: terraform init, terraform apply -auto-approve, terraform destroy


