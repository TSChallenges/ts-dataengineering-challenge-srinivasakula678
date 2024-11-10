# data_engineering/extract.py

import pandas as pd

def extract_data(file_path):
    """
    Extracts data from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Extracted data.
    """
    """TODO"""
data = pd.read_csv('/workspaces/ts-dataengineering-challenge-srinivasakula678/data/bank_transactions_dataset.csv')
print(data.isnull().sum())
print(data.head())
print(data.tail())
print(data.describe())
