import pandas as pd
import csv
import sqlalchemy
import os
import yaml
from pathlib import Path


__data_file_name = 'invoice_sheet_aug1_techprofusecom.csv'
__sec_file_name = 'secrets.yaml'
directory = os.path.dirname(os.path.abspath(__file__))
__conf_file_path = os.path.join(directory, __sec_file_name)

conf = yaml.safe_load(Path(__conf_file_path).read_text())


file_path = os.path.join(directory, "Data", __data_file_name)

db_username = conf['DB_USERNAME']
db_password = conf['DB_PASSWORD']
db_ip = conf['DB_IP']
db_name = conf['DB_NAME']
database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(db_username, db_password,
                                                      db_ip, db_name))


def read_csv_file():
    header = []
    data = []
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        c = 0
        for row in reader:
            if len(row) >= 3:
                c = c+1
                if c == 1:
                    header = row
                else:
                    data.append(row)
    df_data = pd.DataFrame(data, columns=header)
    df_data.drop(df_data.index[-1], inplace=True)
    # df_meta_data = pd.read_csv(file_path,
    #                            delimiter=",", on_bad_lines='skip', header=None)
    # df_meta_data = pd.read_csv(file_path,
    #                            delimiter=",", error_bad_lines=False, header=None)
    # for x in df_meta_data.values:
    #     df_data[x[0]] = x[1]
    return df_data


def df_to_sql():
    df = read_csv_file()
    df['Amount'] = df['Amount'].str.replace(",", '').astype(float)
    print("data read", len(df), df.columns, sum(df['Amount']))
    df.to_sql(con=database_connection,
              name='GOOGLE_INVOICE', if_exists='replace')


df_to_sql()
