# Usage

## Requirements
```
Docker with Docker-compose version  >= 1.29.2
$ docker-compose -v    
docker-compose version 1.29.2,
```
``` 
Docker에서 가용한 4코어 이상의 CPU와 10GB 수준의 Memory
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

* 로컬 Docker-compose기반 서비스목록


|서비스|웹접속 URl|ID|PW|
|--|--|--|--|
|(DB) trino|localhost:8080|trino|-|
|(스키마 DB) hive metastore (mariadb)|localhost:3306|hive|#2203sdf|
|(스키마 관리) hive metastore|localhost:9083|hive|#202203sdf|
|(Storage-Layer) MinIO|localhost:9000|hive|#202203sdf|
|(Workflow MGMT) Airflow|localhost:8180|airflow|airflow|
|(대시보드 및 CronJob) Zeppelin|localhost:8800|admin|password1|


## Zeppelin Docker 환경에서 Trino jdbc 접근시 라이브러리 변경사항

https://issues.apache.org/jira/browse/ZEPPELIN-5551
