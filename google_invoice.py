from pathlib import Path
import pandas as pd
import csv
# from mysql import connector
from sqlalchemy import create_engine, select, MetaData, Table
import os
import yaml

file_name = 'secrets.yaml'
directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, file_name)

conf = {}
with open(file_path, "r") as stream:
    try:
        conf = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        conf = {}

# conf = yaml.safe_load(os.path.expanduser(file_path).read_text())

db_username = conf['DB_USERNAME']
db_password = conf['DB_PASSWORD']
db_ip = conf['DB_IP']
db_name = conf['DB_NAME']

db_engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                          format(db_username, db_password,
                                 db_ip, db_name))


def get_data():
    # print("get_data called")
    sql = "SELECT * FROM GOOGLE_INVOICE;"
    df = pd.read_sql(sql, con=db_engine)
    return df.to_json(orient='records')


# pp = get_data()
# print(pp)
