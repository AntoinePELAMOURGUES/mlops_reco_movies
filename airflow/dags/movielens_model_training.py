####### ENTRAINEMENT DU MODELE MOVIELENS ##########
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from airflow.utils.dates import days_ago
from airflow.models import Variable
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import os
from sqlalchemy import create_engine
