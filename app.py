"""
Connect to a SQL Database using pyodbc
"""

import pyodbc
from Config import SERVER, DATABASE, USERNAME, PASSWORD, PORT


# Function to connect to the database
def connect_to_db(server_name=SERVER, database_name=DATABASE, user_name=USERNAME, password=PASSWORD, port=PORT):
    connection_string = f'DRIVER={{Devart ODBC Driver for MySQL}};SERVER={server_name};DATABASE={database_name};' \
                       f'Encrypt=no;Trusted_connection=yes'
    # connection_string = f'DRIVER={{Devart ODBC Driver for MySQL}};User ID={user_name};Password={password};Server={
    # server_name};Database={database_name};Port={port}' 'DRIVER={Devart ODBC Driver for MySQL};User
    # ID=myuserid;Password=mypassword;Server=myserver;Database=mydatabase;Port=myport;String Types=Unicode'

    conn = pyodbc.connect(connection_string)

    return conn.cursor()


CURSOR = connect_to_db()

print(CURSOR.execute('select * from Document d ').fetchall())

















