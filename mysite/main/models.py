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
    cursor = connection.cursor(dictionary=True)

    print(f"Executing {sql_query}")

    cursor.execute(sql_query)

    res = cursor.fetchall()
    close(cursor=cursor, connection=connection)
    return res


# class Games_Model():
#     # Using an init to assign the self
#     def __init__(self,  id : str, name : str, support_info : str, dlc : str, Base_price : int, Current_price : int, Developer : str, Publisher,
#                  Genre : str, Coming_soon : bool, Release_Date : str, Required_age : int, Controller_support : str, Website : str, Short_desc : str,
#                  Detailed_desc : str, Supported_languages : str, windows : bool, linux : bool, mac : bool, Header_image : str):
#         self.id = id
#         self.name = name
#         self.support_info = support_info
#         self.dlc = dlc

#         # Price info
#         if not Current_price is None:
#             self.Current_price = Current_price/100
#         else:
#             self.Current_price = Current_price
        
#         if not Base_price is None:
#             self.Base_price = Base_price/100
#         else:
#             self.Base_price = Base_price

#         # Dev and pub INFO
#         self.Developers = Developer
#         self.Publishers = Publisher

#         self.Genre = Genre

#         # Release Information
#         self.Coming_soon = Coming_soon
#         self.Release_Date = Release_Date

#         self.Required_age = Required_age
#         self.Controller_support = Controller_support
#         self.Website = Website

#         #Descriptions
#         self.short_desc = Short_desc
#         self.Detailed_desc = Detailed_desc

#         self.Supported_languages = Supported_languages

#         # Platforms
#         self.windows = windows
#         self.linux = linux
#         self.mac = mac

#         self.Header_image = Header_image


# Example here
# class Games(models.Model):
#     steamAppID = models.IntegerField