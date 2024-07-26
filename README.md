# Big Impact Project
# Project 1 - Apache-Airflow
![Banner](assets/imgs/banner.png)

### Instatiate a DAG
```
default_args={
  ‘Owner’ : ‘gwayi’
  'retires' : 2,
  'retry_delay': 3,
  }

@dag(
dag_id=”jobs_listing”, # unique identifier
default_args=default_args, # default arguments
schedule=@daily, # how often the dag runs
start_date=datetime(2024, 7, 20), # start date for the dag
catchup=False, # run/not run missed intervals
tags=['Team A'], # to categorize and filter dags in UI
)
```
[.pycode ETL code](etl.py)
