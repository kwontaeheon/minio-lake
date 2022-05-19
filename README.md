# Usage

## Requirements
```
Docker with Docker-compose version  >= 1.29.2
$ docker-compose -v    
docker-compose version 1.29.2,
```

## start MinIO-lake
```bash
$ git clone https://github.com/kwontaeheon/minio-lake.git
$ cd minio-lake 
$ docker-compose up -d
```

## Start Airflow
```bash
$ cd airflow && ./run.sh
```

# minio-lake
Docker compose PoC Data lake on MinIO Storage Layer, including hive metastore, Spark or Trino with iceberg feature for Bigdata ACID features.

* This repository was forked from trino-minio-docker github repository and modified to include minio as a docker container and jupyter, including iceberg feature.
* airflow folder was forked from  airflow docker github repository.
