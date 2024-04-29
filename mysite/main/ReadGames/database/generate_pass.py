from .Connect_DB import connect, close_connection

def gen_pass(password):
    if password is None or not isinstance(password, str):
        return None
    cnx = connect()
    cursor = cnx.cursor()
    query = "SELECT SHA2(%s, 256);"
    
    cursor.execute(query, (password,))
    
    res = cursor.fetchone()

    close_connection(cursor=cursor, connection=cnx)

    return res

# if __name__ == '__main__':
#     test = ['qwerty', '1234', 0, 12.2, '', None]
#     for t in test:
#         print(t)
#         print(gen_pass(t))