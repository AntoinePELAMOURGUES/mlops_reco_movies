#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "airflow" <<-EOSQL
    CREATE DATABASE bd_reco_raw;
    CREATE DATABASE bd_reco_processed;
    CREATE USER antoine WITH PASSWORD 'pela1';
    GRANT ALL PRIVILEGES ON DATABASE bd_reco_raw TO antoine;
    GRANT CONNECT ON DATABASE bd_reco_processed TO antoine;
EOSQL
