# CHARGEMENT DES FICHIERS SUR MOVIELENS
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

today = datetime.now()
start_date = today - timedelta(days=1)

with DAG(
    dag_id="get_movielens_dataset",
    description="Get the movielens dataset",
    tags=["docker", "reco_movies", "dataset"],
    default_args={
        "owner": "airflow",
        "start_date": start_date,
    },
    catchup=False,
) as dag:

    get_datasets = DockerOperator(
        task_id="get_movielens_dataset",
        image="antoinepela/projet_reco_movies:get-datasets-latest",
        command=["python", "/app/get_movielens_datasets.py"],
        mount_tmp_dir=False,
        mounts=[
            Mount(
                source="/home/antoine/workspace/mlops_reco_movies/airflow/data",  # Chemin ABSOLU sur l'hôte
                target="/opt/airflow/data",  # Chemin dans le conteneur
                type="bind",
            )
        ],
        auto_remove="force",  # Supprime le conteneur après exécution
        docker_url="unix://var/run/docker.sock",
    )

    get_datasets.doc_md = "Get the movielens dataset from AWS and save it in the data folder"
