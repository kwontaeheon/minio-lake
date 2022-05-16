CREATE USER if not exists 'hive'@'%' identified by '#2203sdf';

create database if not exists metastore_db;

grant all PRIVILEGES on metastore_db.* to hive@'%';

flush privileges;


