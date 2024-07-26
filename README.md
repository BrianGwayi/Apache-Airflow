# Big Impact Project
# Project 1 - Apache-Airflow

![Banner](assets/imgs/afbanner.png)

Apache Airflow® is an open-source platform for developing, scheduling, and monitoring batch-oriented workflows. Airflow’s extensible Python framework enables you to build workflows connecting with virtually any technology. A web interface helps manage the state of your workflows. Airflow is deployable in many ways, varying from a single process on your laptop to a distributed setup to support even the biggest workflows.  
Tech Stack: PostgreSQL Database, Python, Apache Airflow, AWS

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
