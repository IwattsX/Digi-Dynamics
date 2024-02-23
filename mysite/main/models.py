from django.db import models
from .ReadGames.database.Connect_DB import connect, close_connection

# Create your models here.

# Use this to model everything in the databases
# NOTE: May not use django.db since we are using mySQL instead with mysql-connector

def close(cursor, connection):
    close_connection(cursor=cursor, connection=connection)

def select(table, columns='*', whereClause=None, limits=20):
    if isinstance(columns, list):
        # Change columns to string type
        columns = ", ".join(columns)

    sql_query = ""
    if whereClause:
        sql_query = f"""
            SELECT {columns} FROM {table}
            WHERE {whereClause} LIMIT {limits};
        """
    else:
        sql_query = f"""
            SELECT {columns} FROM {table} LIMIT {limits};
        """
    
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(sql_query)

    res = cursor.fetchall()
    close(cursor=cursor, connection=connection)
    return res


class Games_Model():
    # Using an init to assign the self
    def __init__(self,  id : str, name : str, support_info : str, dlc : str, Base_price : int, Current_price : int, Developer : str, Publisher,
                 Genre : str, Coming_soon : bool, Release_Date : str, Required_age : int, Controller_support : str, Website : str, Short_desc : str,
                 Detailed_desc : str, Supported_languages : str, windows : bool, linux : bool, mac : bool, Header_image : str):
        self.name = name


# Example here
# class Games(models.Model):
#     steamAppID = models.IntegerField