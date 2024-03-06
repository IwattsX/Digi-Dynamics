from .Connect_DB  import connect, close_connection

def update(tableName : str, SetClause : str, WhereClause : str):
    sql_query = f"""
        UPDATE {tableName}
        SET {SetClause}
        WHERE {WhereClause};
    """
    cnx = connect()
    cursor = cnx.cursor()
    cursor.execute(sql_query)
    close_connection(cursor=cursor, connection=cnx)
