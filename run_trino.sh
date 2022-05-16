
docker-compose up -d


docker exec -it trino-minio-docker_mariadb_1 mysql -uroot -p

drop user hive;
CREATE USER if not exists 'hive'@'%' identified by '#2203sdf';
create database if not exists metastore_db;
grant all PRIVILEGES on metastore_db.* to hive@'%';
flush privileges;

# docker exec -it trino-minio-docker_trino_1 trino
# docker exec -it minio-lake_trino_1 trino --catalog iceberg --schema default
docker exec -it trino-minio-docker_trino_1 trino --catalog minio  --schema default

CREATE SCHEMA IF NOT EXISTS minio.hive
WITH (location = 's3a://hive/');

USE MINIO.HIVE;

CREATE TABLE TEST(id varchar);


CREATE SCHEMA IF NOT EXISTS delta.hive
WITH (location = 's3a://hive/');

USE DELTA.HIVE;

CREATE TABLE trinodelta2(id varchar);
insert into trinodelta2 values '1','2','3','4','5';

update trinodelta2  set id='100' where id='1';

select * from trinodelta2;
 id
-----
 100
 2
 3
 4
 5
(5 rows)


create schema if not exists iceberg.hive with (location='s3a://hive/');

use iceberg.hive;

create table iceberg_trino1(id varchar);
insert into iceberg_trino1 values '1', '2', '3', '4', '5';
delete from iceberg_trino1 where id='1';

select * from iceberg_trino1;
 id
----
 2
 3
 4
 5
(4 rows)
