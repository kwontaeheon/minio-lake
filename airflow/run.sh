#!/bin/bash

docker-compose up airflow-init
docker-compose down
docker-compose up -d
docker network connect minio-lake_trino-network airflow_airflow-worker_1
