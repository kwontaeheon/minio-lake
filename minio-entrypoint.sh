#!/usr/bin/bash

/usr/bin/docker-entrypoint.sh 



echo "making bucket.. hive" 
/data/mc mb /data/hive
echo "making bucket.. delta" 
/data/mc mb /data/delta

minio server /data
