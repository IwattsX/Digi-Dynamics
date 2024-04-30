from .models import select
import re

import mysql.connector.errors
from pprint import pprint

from .ReadGames.database.generate_pass import gen_pass
from .ReadGames.database.Connect_DB import connect, close_connection



def insert_into_liked_tables(table, games_id : str, username : str, id_col : str):
    cnx = connect()
    cursor = cnx.cursor(dictionary=True)
    
    try:
        sql_query = f"SELECT username, {id_col} FROM {table} WHERE {id_col} = %s AND username = %s"
        cursor.execute(sql_query, (games_id, username))
        
        already_liked = cursor.fetchone()  # Fetch one row from the result set
        
        if already_liked:
            print(f"The game id {games_id} is already liked by {username}")
        else:
            sql_query = f"INSERT INTO {table} (username, {id_col}) VALUES (%s, %s)"
            print(f"{sql_query} is getting executed")
            cursor.execute(sql_query, (username, games_id))
        cnx.commit()  # Commit the transaction
        
    except mysql.connector.Error as err:
        print("Error:", err)
        cnx.rollback()  # Rollback the transaction if an error occurs
    
    finally:
        close_connection(cursor=cursor, connection=cnx)



def insert_into_user(username, password, alert_msg):
    cnx = connect()
    cursor = cnx.cursor()

    cursor.execute("Select username from user where username = %s", (username,))
    res = cursor.fetchone()
    
    if res:
        alert_msg = "Try another username"
        return alert_msg


    try:
        sql_query = """
            INSERT INTO user (username, pass) VALUES (%s, SHA2(%s, 256));
        """

        cursor.execute(sql_query, (username, password))
        cnx.commit()

    except mysql.connector.Error as err:
        print("Error:", err)
        cnx.rollback()  # Rollback the transaction if an error occurs
    
    finally:
        close_connection(cursor=cursor, connection=cnx)
        alert_msg = "User saved successfully"
        return alert_msg


# TODO: implement dislike after I implement like for these
def dislike_DLC(username, id, table):
    pass

def dislike_demo(username, id, table):
    pass

def dislike_music(username, id, table):
    pass



def dislike_game(username, id, table, title_id):
    cnx = connect()
    cursor = cnx.cursor()

    try:
        sql_query = f"""
        DELETE FROM {table} WHERE username = %s and {title_id} = %s; 

    """
        print(sql_query, (username, id))
        cursor.execute(sql_query, (username, id))
        cnx.commit()

    except mysql.connector.Error as err:
        print("Error:", err)
        cnx.rollback()  # Rollback the transaction if an error occurs
    
    finally:
        close_connection(cursor=cursor, connection=cnx)


def liked_games(username, tables):
    action_res = select(tables, columns="Games.id", whereClause="Games.id = LikedGames.games_id AND LikedGames.username = '{}'".format(username))
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

    try:
        sql_query = ""
        if liked_table == "LikedGames":
            sql_query = "SELECT LikedGames.username as username, Games.name, Games.id FROM LikedGames INNER JOIN Games ON Games.id = LikedGames.games_id WHERE username = '{}'".format(response.session.get("session_id"))
        
        if liked_table == "LikedDLC":
            sql_query = "SELECT LikedDLC.username as username, DLC.name, DLC.id FROM LikedDLC INNER JOIN DLC ON DLC.id = LikedDLC.DLC_id WHERE username = '{}'".format(response.session.get("session_id"))

        if liked_table == "LikedMusic":
            sql_query = "SELECT LikedMusic.username as username, Music.name, Music.id FROM LikedMusic INNER JOIN Music ON Music.id = LikedMusic.id WHERE username = '{}'".format(response.session.get("session_id"))

        if liked_table == "LikedDemo":
            sql_query = "SELECT LikedDemo.username as username, Demo.name, Demo.id FROM LikedDemo INNER JOIN Demo ON Demo.id = LikedDemo.id WHERE username = '{}'".format(response.session.get("session_id"))

        print(sql_query)

        cursor.execute(sql_query)
        res = cursor.fetchall()
        close_connection(cursor=cursor, connection=cnx)
    except mysql.connector.Error as err:
        print("Error:", err)
        cnx.rollback()  # Rollback the transaction if an error occurs
    return res


def searchHander_demo(response, table_name : str, searchBy : str, Append_list:list):
    if searchBy == 'name':
        name = response.GET.get('name', None)
        
        # This doesn't display anything and doesn't do the name REGEXP '' that will always be true
        if name is None or name == "":
            return
        Games_res = select(table_name, columns="*", 
        whereClause=f"Name REGEXP '{name}'")
        for row in Games_res:
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

        Games_res = select(table_name, columns="*",
                           whereClause=f"Genre REGEXP '{genres_regex}'")
        for row in Games_res:
            Append_list.append(row)

    elif searchBy == 'publisher':
        publisher = response.GET.get('name', None)
        if publisher is None or publisher == "":
            return
        
        Games_res = select(table_name,columns="*",
                            whereClause=f"Publisher LIKE '%{publisher}%'")
        
        for row in Games_res:
            Append_list.append(row)

    elif searchBy == 'developer':
        developer = response.GET.get('name', None)
        if developer is None or developer == "":
            return
        Games_res = select(table_name,columns="*",
                        whereClause=f"Developer LIKE '%{developer}%'")
        
        for row in Games_res:
            Append_list.append(row)


    elif searchBy == 'price':
        priceStr = response.GET.get('price', None)
        if priceStr is None or priceStr == "":
            return
        

        price = float(priceStr) * 100


        Games_res = select(table_name,columns="*",
                    whereClause=f"Current_price < {price}")
        
        for row in Games_res:
            Append_list.append(row)


    elif searchBy == 'dateyear':
        date = response.GET.get('year', None)
        if date is None or date == "":
            return
        
        year = int(date)

        Games_res = select(table_name,columns="*",
                    whereClause=f"Release_Date REGEXP '\\\\d{{4}}'")
        
        for row in Games_res:
            regex_year = "(\\d{4})"
            release_str = row["Release_Date"]
            temp = re.search(regex_year, release_str)

            release_year = int(temp.group(1))
            if year == release_year:
                # print(f"Year {year} release_year = {release_year}")
                Append_list.append(row)



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
    