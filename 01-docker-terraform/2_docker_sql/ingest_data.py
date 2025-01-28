#!/usr/bin/env python
# coding: utf-8

#get_ipython().system('pip install psycopg2')
#get_ipython().system('pip install sqlalchemy')
#get_ipython().system('pip install pandas')
#get_ipython().system('pip install pyarrow')

import pandas as pd
import argparse
from time import time
from sqlalchemy import create_engine
import os


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    csv_name = 'output.csv'

    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    df_iter = pd.read_csv(url, iterator = True, chunksize=100000)

    df = next(df_iter)

    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    # send columns to postgres
    df.head(0).to_sql(name = table_name, con=engine, if_exists='replace')

    i = 1
    while True:
        t_start = time()

        df = next(df_iter)

        df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
        df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

        df.to_sql(name = table_name, con=engine, if_exists='append')
        
        t_end = time()

        print('inserted chunk ', i, ' , took', t_end-t_start , ' seconds.')
        i += 1


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of the table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()
    
    main(args)