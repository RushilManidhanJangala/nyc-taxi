from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "rushil"
}

with DAG(
    dag_id="nyc_taxi_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["nyc", "etl"]
) as dag:

    transform_data = BashOperator(
        task_id="transform_data",
        bash_command="python /opt/airflow/project/etl/transform.py"
    )

    aggregate_data = BashOperator(
        task_id="aggregate_data",
        bash_command="python /opt/airflow/project/etl/aggregate.py"
    )

    load_postgres = BashOperator(
        task_id="load_postgres",
        bash_command="python /opt/airflow/project/database/load_hourly_stats.py"
    )

    transform_data >> aggregate_data >> load_postgres