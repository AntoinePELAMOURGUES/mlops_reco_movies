# CHARGEMENT DES FICHIERS SUR MOVIELENS
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import os
from airflow.utils.dates import days_ago
