#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


# [START tutorial]
# [START import_module]
import json

import pendulum

from airflow.decorators import dag, task
from trino.dbapi import connect
# [END import_module]


# [START instantiate_dag]
@dag(
    start_date=pendulum.datetime(2022, 5, 19, tz="Asia/Seoul"),
    catchup=False,
    schedule_interval='*/55 * * * *',
    default_args={'depends_on_past': True},
    tags=['dag1'],
)
def crawl_nft_info():
    """
    ### crawl_nft_info
    """
    # [END instantiate_dag]

    # [START extract]
    @task.virtualenv(
            use_dill=True,
            system_site_packages=True,
            requirements=[''],
        )
    def extract():
        """
        #### Extract task
        A simple Extract task to get data ready for the rest of the data
        pipeline. In this case, getting data is simulated by reading from a
        hardcoded JSON string.
        """
        print('connecting..')
        conn = connect(
            host="minio-lake_trino_1",
            port=8080,
            user="trino",
            catalog="iceberg",
            schema="hive",
        )
        print('connected')
        import json
        cur = conn.cursor()
        cur.execute("select * from iceberg_trino1")
        rows = cur.fetchall()
        print(rows)
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'

        order_data_dict = json.loads(data_string)
        return order_data_dict

    # [END extract]

    # [START transform]
    @task(multiple_outputs=True)
    def transform(order_data_dict: dict):
        """
        #### Transform task
        A simple Transform task which takes in the collection of order data and
        computes the total order value.
        """
        total_order_value = 0

        for value in order_data_dict.values():
            total_order_value += value

        return {"total_order_value": total_order_value}

    # [END transform]

    # [START load]
    @task()
    def load(total_order_value: float):
        """
        #### Load task
        A simple Load task which takes in the result of the Transform task and
        instead of saving it to end user review, just prints it out.
        """

        print(f"Total order value is: {total_order_value:.2f}")

    # [END load]

    # [START main_flow]
    order_data = extract()
    order_summary = transform(order_data)
    load(order_summary["total_order_value"])
    # [END main_flow]


# [START dag_invocation]
crawl_nft_info_dag = crawl_nft_info()
# [END dag_invocation]

# [END tutorial]