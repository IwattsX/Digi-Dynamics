from .models import select
import re

import mysql.connector.errors
from pprint import pprint

from .ReadGames.database.generate_pass import gen_pass
from .ReadGames.database.Connect_DB import connect, close_connection

from .ReadGames.database.InsertIntoSteam import inDB

def dislike_function(username, id, table):
    cnx = connect()
    cursor = cnx.cursor()

    try:
        sql_query = f"""
        DELETE FROM {table} WHERE username = %s and games_id = %s; 

    """
        print(sql_query, (username, id))
        cursor.execute(sql_query, (username, id))
        cnx.commit()

    except mysql.connector.Error as err:
        print("Error:", err)
        cnx.rollback()  # Rollback the transaction if an error occurs
    
    finally:
        close_connection(cursor=cursor, connection=cnx)




def insert_into_LikedGames(username, games_id):
    cnx = connect()
    cursor = cnx.cursor(dictionary=True)
    
    try:
        sql_query = "SELECT username, games_id FROM LikedGames WHERE games_id = %s AND username = %s"
        cursor.execute(sql_query, (games_id, username))
        
        already_liked = cursor.fetchone()  # Fetch one row from the result set
        
        if already_liked:
            print(f"The game id {games_id} is already liked by {username}")
        else:
            sql_query = "INSERT INTO LikedGames (username, games_id) VALUES (%s, %s)"
            print(f"{sql_query} is getting executed")
            cursor.execute(sql_query, (username, games_id))
        
        cnx.commit()  # Commit the transaction
        
    except mysql.connector.Error as err:
        print("Error:", err)
        cnx.rollback()  # Rollback the transaction if an error occurs
    
    finally:
        close_connection(cursor=cursor, connection=cnx)



def liked_games(username):
    action_res = select("Games, LikedGames", columns="Games.id", whereClause="Games.id = LikedGames.games_id AND LikedGames.username = '{}'".format(username))
    pprint(action_res)
    
    res = { e["id"] : True for e in action_res }

    pprint(res)
    return res


def login_Handler(username, password):
    res = False
    cnx = connect()
    cursor = cnx.cursor(dictionary=True)

    query = "SELECT * FROM user WHERE username = %s AND pass = %s"
    generated_pass = gen_pass(password)
    if not generated_pass is None: 
        cursor.execute(query, (username, generated_pass[0]))
        res = cursor.fetchone()
    close_connection(cursor=cursor, connection=cnx)
    if res:
        return True
    else:
        return False



def likedHistory(response, liked_table):
    res = []
    cnx = connect()
    cursor = cnx.cursor(dictionary=True)
    sql_query = ""
    if liked_table == "LikedGames":
        sql_query = "SELECT LikedGames.username as username, Games.name, Games.id FROM LikedGames INNER JOIN Games ON Games.id = LikedGames.games_id WHERE username = '{}'".format(response.session.get("session_id"))
        print(sql_query)
        cursor.execute(sql_query)
        res = cursor.fetchall()
    
    close_connection(cursor=cursor, connection=cnx)
    return res




def searchHander(response, table_name : str, searchBy : str, Append_list : list):
    if searchBy == 'name':
        name = response.GET.get('name', None)
        
        # This doesn't display anything and doesn't do the name REGEXP '' that will always be true
        if name is None or name == "":
            return
        Games_res = select(table_name, columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date", 
        whereClause=f"Name REGEXP '{name}'")
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            Append_list.append(row)
    
    elif searchBy == "genre":
        genres = response.GET.getlist('genres', None)

        # Same thing, we want input there
        if genres is None or len(genres) == 0:
            return
        
        genres_regex = ""
        for i, genre in enumerate(genres):
            genres_regex += f"{genre}"
            if i == len(genres) - 1:
                break
            genres_regex += "|"

        # print(genres_regex)

        Games_res = select(table_name, columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                           whereClause=f"Genre REGEXP '{genres_regex}'")
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            Append_list.append(row)

    elif searchBy == 'publisher':
        publisher = response.GET.get('name', None)
        if publisher is None or publisher == "":
            return
        
        Games_res = select(table_name,columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                            whereClause=f"Publisher LIKE '%{publisher}%'")
        
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            Append_list.append(row)

    elif searchBy == 'developer':
        developer = response.GET.get('name', None)
        if developer is None or developer == "":
            return
        Games_res = select(table_name,columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                        whereClause=f"Developer LIKE '%{developer}%'")
        
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            Append_list.append(row)


    elif searchBy == 'price':
        priceStr = response.GET.get('price', None)
        if priceStr is None or priceStr == "":
            return
        

        price = float(priceStr) * 100


        Games_res = select(table_name,columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                    whereClause=f"Current_price < {price}")
        
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            Append_list.append(row)


    elif searchBy == 'dateyear':
        date = response.GET.get('year', None)
        if date is None or date == "":
            return
        
        year = int(date)

        Games_res = select(table_name,columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                    whereClause=f"Release_Date REGEXP '\\\\d{{4}}'")
        
        for row in Games_res:
            regex_year = "(\\d{4})"
            release_str = row["Release_Date"]
            temp = re.search(regex_year, release_str)

            release_year = int(temp.group(1))
            if year == release_year:
                # print(f"Year {year} release_year = {release_year}")
                if not row.get("Base_price") is None:
                    row["Base_price"] = row["Base_price"]/100
                if not row.get("Current_price") is None:
                    row["Current_price"] = row["Current_price"]/100
                Append_list.append(row)
    