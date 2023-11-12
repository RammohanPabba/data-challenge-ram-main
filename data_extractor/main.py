from pathlib import Path

import os
import pandas as pd

DATA_DIR = Path(__file__).parent.parent / "data"

def main():
    print("Running pipeline 🚀")

    # Setting the maximum length for data frames. Useful while printing the df on console
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    csv_files = os.listdir(DATA_DIR)
    master_df = pd.DataFrame()
    #Read all file names from a DATA_DIR
    for file_name in csv_files:
        file_name_only=file_name
        file_name = str(DATA_DIR) + "\\" + str(file_name)

        #Reading the data from file into pandas dataframe
        df = pd.read_csv(file_name)

        #Append new column file name which has file name as a value
        df['file_name']=file_name_only

        #Concatenate all files data into single dataframe
        master_df = pd.concat([master_df, df])

        #Filtering the Success Records into Result dataframe
        result_df = master_df[master_df['transaction_status'] == 'Success']

        #Writing the output into either parquet or csv
        result_df.to_parquet('filtered_records.parquet', engine='fastparquet')
        #result_df.to_csv('filtered_records_csv.csv')

if __name__ == "__main__":
    main()