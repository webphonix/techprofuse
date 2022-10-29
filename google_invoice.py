import pandas as pd
import csv
from sqlalchemy import create_engine, select, MetaData, Table
import os

db_username = 'webphoni_guru'
db_password = 'Hyderabad51#'
db_ip = '168.119.43.146'
db_name = 'webphoni_techprofuse'
db_engine = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                          format(db_username, db_password,
                                 db_ip, db_name))


def get_data():
    sql = "SELECT * FROM GOOGLE_INVOICE;"
    df = pd.read_sql(sql, con=db_engine)
    return df.head().to_json()


get_data()
