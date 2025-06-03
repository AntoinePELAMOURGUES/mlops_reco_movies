from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime, timedelta

today = datetime.now()
start_date = today - timedelta(days=1)

with DAG(
    dag_id="init_movie_datasets_raw",
    description="Create the tables in the database for the raw movie datasets",
    tags=["docker", "reco_movies", "dataset"],
    default_args={
        "owner": "antoine",
        "start_date": start_date,
    },
    catchup=False,
    template_searchpath="/opt/airflow/dags/sql/create_tables_raw/",
) as dag:

    create_movies_table_raw = SQLExecuteQueryOperator(
        task_id="create_movies_table_raw",
        conn_id="postgres_bd_reco_raw",
        sql="create_table_movies_raw.sql",
        database="bd_reco_raw",
        retries=3,
        retry_delay=timedelta(minutes=1)
    )

    create_links_table_raw = SQLExecuteQueryOperator(
        task_id="create_links_table_raw",
        conn_id="postgres_bd_reco_raw",
        sql="create_table_links_raw.sql",
        database="bd_reco_raw",
        retries=3,
        retry_delay=timedelta(minutes=1)
    )

    create_ratings_table_raw = SQLExecuteQueryOperator(
        task_id="create_ratings_table_raw",
        conn_id="postgres_bd_reco_raw",
        sql="create_table_ratings_raw.sql",
        database="bd_reco_raw",
        retries=3,
        retry_delay=timedelta(minutes=1)
    )

    create_genome_tags_table_raw = SQLExecuteQueryOperator(
        task_id="create_genome_tags_table_raw",
        conn_id="postgres_bd_reco_raw",
        sql="create_table_genome_tags_raw.sql",
        database="bd_reco_raw",
        retries=3,
        retry_delay=timedelta(minutes=1)
    )

    create_genome_scores_table_raw = SQLExecuteQueryOperator(
        task_id="create_genome_scores_table_raw",
        conn_id="postgres_bd_reco_raw",
        sql="create_table_genome_scores_raw.sql",
        database="bd_reco_raw",
        retries=3,
        retry_delay=timedelta(minutes=1)
    )

    create_movies_table_raw >> [create_links_table_raw, create_ratings_table_raw]
    create_genome_tags_table_raw >> create_genome_scores_table_raw
