import mysql.connector
from dotenv import load_dotenv
import os


from sqlalchemy import create_engine

load_dotenv()



# Replace these values with your MySQL credentials
def connect():
    host = "localhost"
    user = os.getenv("uname")
    password = os.getenv("pass")
    database = os.getenv("database")

# Establish a connection
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
    
    return engine
