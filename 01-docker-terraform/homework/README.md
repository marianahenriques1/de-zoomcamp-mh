# Homework

## Question 1

Run on the terminal:
```
docker run -it --entrypoint bash python:3.12.8
pip --version
```

Answer: The version of pip is 24.3.1

## Question 2

Hostname = the service name of the postgres database defined in the docker-compose.yaml = db

Port = the container's internal port for postgres = 5432

Answer: db:5432

## Question 3

Run on the terminal: docker-compose up

Then go to: http://localhost:8080/browser/ and add new server with hostname: pgdatabase and user/pass: root/root

After this run on the terminal:
```
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
```

```
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
```
Answer: 104,802; 198,924; 109,603; 27,678; 35,189

## Question 4
```
SELECT DATE(lpep_pickup_datetime) as day
FROM public.green_trip_data
WHERE trip_distance = (
    SELECT MAX(trip_distance)
    FROM public.green_trip_data
);
```

Answer: 2019-10-31

## Question 5
```
SELECT tz."Zone", SUM(total_amount) as daily_amount
FROM public.green_trip_data as gt
LEFT JOIN public.taxi_zone_data as tz
ON gt."PULocationID" = tz."LocationID"
WHERE DATE(lpep_pickup_datetime) = DATE('2019-10-18')
GROUP BY tz."Zone"
ORDER BY SUM(total_amount) DESC
```
Answer: East Harlem North, East Harlem South, Morningside Heights

## Question 6
```
SELECT 
    gt."DOLocationID",
    tz_2."Zone" AS DOZone,
    MAX(gt.tip_amount) AS max_tip_amount
FROM public.green_trip_data AS gt
LEFT JOIN public.taxi_zone_data AS tz_1
    ON gt."PULocationID" = tz_1."LocationID"
LEFT JOIN public.taxi_zone_data AS tz_2
    ON gt."DOLocationID" = tz_2."LocationID"
WHERE tz_1."Zone" = 'East Harlem North'
  AND DATE(gt.lpep_pickup_datetime) BETWEEN DATE('2019-10-01') AND DATE('2019-10-31')
GROUP BY gt."DOLocationID", tz_2."Zone"
ORDER BY max_tip_amount DESC
```

Answer: JFK Airport

## Question 7

Answer: terraform init, terraform apply -auto-approve, terraform destroy


