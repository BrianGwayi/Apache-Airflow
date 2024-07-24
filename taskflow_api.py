from airflow.decorators import dag, task
from datetime import datetime
import requests
import xmltodict
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

@dag(
        schedule=None,
        start_date=datetime(2024, 7, 20),
        catchup=False,
        tags=['taskflow'],
        )

def _taskflow_api_():

    @task
    def extract():
        response = requests.get("https://www.myjobmag.co.ke/aggregate_feed.xml")
        xml_feed = xmltodict.parse(response.text)
        return xml_feed['rss']['channel']['item']
        
    @task
    def transform(val):
        #response = ti.xcom_pull(task_ids="extract")
        #logging.info(response)
        #print(val)
        tf = pd.DataFrame(val)
        return tf.astype({'id':'int64','pubDate':'datetime64[ns]'})

    @task
    def load(new_val):
        # Establish a connection to your PostgreSQL database
        conn = psycopg2.connect(
            database='jobs_pipelines',
            user='postgres',
            password='p@ssword',
            host='127.0.0.1',
            port='5432'
            )
        with conn.cursor() as cursor:
            x = new_val.to_dict(orient="records")
            execute_values(conn, new_val, 'listing')
              
            conn.commit()
            print(new_val)

    

    #extract() >> transform() >> load()
    val = extract()
    new_val = transform(val)
    load_val = load(new_val)
    #val >> new_val >> load_val 
_taskflow_api_ = _taskflow_api_()