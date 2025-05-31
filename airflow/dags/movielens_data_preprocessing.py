######### DATA PROCESSING DES DONNEES MOVIELENS #########
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from airflow.utils.dates import days_ago
from airflow.models import Variable
import os
