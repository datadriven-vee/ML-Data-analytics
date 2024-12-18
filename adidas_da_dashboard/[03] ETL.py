import pandas as pd
import pyodbc
from sqlalchemy import create_engine
import urllib

df = pd.read_csv(r'adidas_sales_dataset.csv')

# drop Unnamed: 0 column
df.drop('Unnamed: 0', axis=1, inplace=True)

server = 'LAPTOP-68P3K4HH\SQLEXPRESS'
database = 'Adidas'
username = 'your_username'
password = 'your_password'

# Create a connection string
connection_string = f"mssql+pyodbc://{username}:{urllib.parse.quote_plus(password)}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(connection_string)

try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")

table_name = 'sales'
try:
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print("Data loaded successfully!")
except Exception as e:
    print(f"Data load failed: {e}")
