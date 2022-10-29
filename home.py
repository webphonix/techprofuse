# import pandas as pd
# import csv
# import sqlalchemy
# import os


# file_name = 'invoice_sheet_aug1_techprofusecom.csv'
# directory = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(directory, "Data", file_name)

# database_username = 'webphoni_guru'
# database_password = 'Hyderabad51#'
# database_ip = '168.119.43.146'
# database_name = 'webphoni_techprofuse'
# database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
#                                                format(database_username, database_password,
#                                                       database_ip, database_name))

# df_data = pd.dataframe()


# def read_csv():
#     header = []
#     data = []
#     with open(file_path, newline='') as f:
#         reader = csv.reader(f)
#         c = 0
#         for row in reader:
#             if len(row) >= 3:
#                 c = c+1
#                 if c == 1:
#                     header = row
#                 else:
#                     data.append(row)
#     df_data = pd.DataFrame(data, columns=header)
#     df_data.drop(df_data.index[-1], inplace=True)
#     df_meta_data = pd.read_csv(file_path,
#                                delimiter=",", on_bad_lines='skip', header=None)
#     for x in df_meta_data.values:
#         df_data[x[0]] = x[1]


# def df_to_sql():
#     df_data.to_sql(con=database_connection,
#                    name='GOOGLE_INVOICE', if_exists='replace')
