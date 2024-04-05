import mysql.connector
from decouple import config


# Replace these values with your MySQL credentials
def connect():
    host = "localhost"
    user = config("uname")
    password = config("pass")
    database = config("database")

# Establish a connection
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )
    
    return connection

def close_connection(cursor, connection):
    cursor.close()
    connection.close()
