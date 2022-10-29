
import os


file_name = 'invoice_sheet_aug1_techprofusecom.csv'
# file_path = os.path.join(os.path.dirname())
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         "Data", file_name)
print(file_path)
