#!/bin/bash

docker-compose up airflow-init
docker-compose down
docker-compose up -d
docker network connect minio-lake_trino-network airflow_airflow-worker_1
docker network connect minio-lake_trino-network airflow_airflow-scheduler_1
docker network connect minio-lake_trino-network airflow_flower_1
docker network connect minio-lake_trino-network airflow_airflow-webserver_1
docker network connect minio-lake_trino-network  airflow_airflow-triggerer_1
docker network connect minio-lake_trino-network airflow_postgres_1
docker network connect minio-lake_trino-network airflow_redis_1
