from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

with DAG(
    dag_id="init_movie_datasets",
    start_date=datetime(2025, 6, 1),
    schedule_interval=None,
    catchup=False,
    template_searchpath="/opt/airflow/dags/sql",
) as dag:

    create_movies_table = PostgresOperator(
        task_id="create_movies_table",
        postgres_conn_id="postgres_movie_datasets",
        sql="create_movies.sql",
    )

    create_links_table = PostgresOperator(
        task_id="create_links_table",
        postgres_conn_id="postgres_movie_datasets",
        sql="create_links.sql",
    )

    create_ratings_table = PostgresOperator(
        task_id="create_ratings_table",
        postgres_conn_id="postgres_movie_datasets",
        sql="create_ratings.sql",
    )

    create_movies_table >> [create_links_table, create_ratings_table]
