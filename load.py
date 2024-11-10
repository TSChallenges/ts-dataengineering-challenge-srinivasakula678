# data_engineering/load.py

import sqlite3
import pandas as pd

def load_data(data, db_name, table_name):
    """
    Loads transformed data into a SQLite database.

    Parameters:
    - df (pd.DataFrame): Transformed data.
    - db_name (str): Name of the SQLite database file.
    - table_name (str): Name of the table to insert data into.

    Returns:
    - None
    """
    if data.empty:
        print("Empty DataFrame received. No data to load.")
        return

    try:
        # Connect to SQLite database (creates the database if it doesn't exist)
               #TODO
               conn = sqlite3.connect(db_name)
               cursor = conn.cursor()

        # Create a table if it doesn't exist
               #TODO
               create_table_query = f"""CREATE TABLE IF NOT EXISTS 
               {table_name} 
               (
            customerid INTEGER,
            age INTEGER,
            "transaction" REAL,
            balance REAL
        );"""
               cursor.execute(create_table_query)
        # Insert data into the table
               #TODO
               data.to_sql(table_name, conn, if_exists='append', index=False)
        #load_data(/workspaces/ts-dataengineering-challenge-srinivasakula678/data/bank_transactions_dataset.csv, transaction.db, bank_transactions_dataset)
          
       
        # Commit and close the connection
              #TODO
               conn.commit()
               conn.close()
    except sqlite3.Error as e:
     print(f"SQLite error: {e}")

csv_file = 'data/bank_transactions_dataset.csv'
db_name = 'etl_database.db'
table_name = 'cleaned_data'

# Load the CSV file into a DataFrame
data = pd.read_csv(csv_file)

# Call the function to load data into the database
load_data(data, db_name, table_name)
print(data)