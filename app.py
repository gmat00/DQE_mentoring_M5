"""
Connect to a SQL Database using pyodbc
"""

import pyodbc
from Config import SERVER, DATABASE, USERNAME, PASSWORD, PORT


# Function to connect to the database
def connect_to_db(server_name=SERVER, database_name=DATABASE):
    connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server_name};DATABASE={database_name};' \
                       f'Encrypt=no;Trusted_connection=yes'


    # connection_string = f'DRIVER={{Devart ODBC Driver for MySQL}};User ID={user_name};Password={password};Server={
    # server_name};Database={database_name};Port={port}' 'DRIVER={Devart ODBC Driver for MySQL};User
    # ID=myuserid;Password=mypassword;Server=myserver;Database=mydatabase;Port=myport;String Types=Unicode'

    conn = pyodbc.connect(connection_string)

    return conn.cursor()


CURSOR = connect_to_db()

def feature_2345():
    pass
















