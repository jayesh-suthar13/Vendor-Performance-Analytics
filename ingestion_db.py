import pandas as pd
import numpy as np
import os 
import logging
import time 
from sqlalchemy import create_engine
 
logging.basicConfig(
    filename= "logs/ingestion_db.log",
    level= logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filemode= "a"
)

engine= create_engine('sqlite:///inventory_db')

def ingest_db(df,table_name,engine):
    "this function will ingest the dataframe into database table"
    df.to_sql(table_name, con=engine,if_exists='replace',index=False)

def load_raw_data():
    "this function will load csv's as dataframes & ingest into db"
    start=time.time()
    for file in os.listdir ('Data project 1'):
        if '.csv' in file:
            df= pd.read_csv('Data project 1/'+file)
            logging.info(f'Ingestion{file} in db')
            ingest_db(df,file[:-4],engine)
    end=time.time()
    total_time=(end-start)/60
    logging.info("-----------Ingestion completed-----------")
    logging.info(f'\n Total time taken: {total_time} minutes')

if __name__ == "__main__":
    load_raw_data()
