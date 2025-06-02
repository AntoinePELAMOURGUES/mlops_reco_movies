from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime

with DAG(
    dag_id="init_movie_datasets",
    start_date=datetime(2025, 6, 1),
    schedule=None,
    catchup=False,
    template_searchpath="/opt/airflow/dags/sql",
) as dag:

    create_movies_table = SQLExecuteQueryOperator(
        task_id="create_movies_table",
        conn_id="postgres_movie_datasets",
        sql="create_table_movies.sql",
    )

    create_links_table = SQLExecuteQueryOperator(
        task_id="create_links_table",
        conn_id="postgres_movie_datasets",
        sql="create_table_links.sql",
    )

    create_ratings_table = SQLExecuteQueryOperator(
        task_id="create_ratings_table",
        conn_id="postgres_movie_datasets",
        sql="create_table_ratings.sql",
    )

    create_movies_table >> [create_links_table, create_ratings_table]
