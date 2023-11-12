from pathlib import Path

import os
import pandas as pd

DATA_DIR = Path(__file__).parent.parent / "data"

def main():
    print("Running pipeline 🚀")

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    csv_files = os.listdir(DATA_DIR)
    master_df = pd.DataFrame()
    for file_name in csv_files:
        file_name_only=file_name
        file_name = str(DATA_DIR) + "\\" + str(file_name)
        df = pd.read_csv(file_name)
        df['file_name']=file_name_only
        master_df = pd.concat([master_df, df])
        result_df = master_df[master_df['transaction_status'] == 'Success']
        result_df.to_csv('filtered_records.csv')

    #columns = df.columns
    #print(columns)
    #print(df['transaction_id']+"---"+df['transaction_status']+"---"+df['merchant_id'])
    #print("******************************after filtering******************************")
    #print(result_df['transaction_id']+"---"+result_df['transaction_status']+"---"+result_df['merchant_id'])

if __name__ == "__main__":
    main()
