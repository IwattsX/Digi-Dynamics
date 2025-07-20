from Connect_DB import connect
from sqlalchemy import text

def gen_pass(password):
    if password is None or not isinstance(password, str):
        return None
    engine = connect()
    query = None
    with engine.connect() as connection:
        query = connection.execute(text("SELECT SHA2(:password, 256);"), 
                                   {
                                       'password':password
                                   })
    if query is None:
        return query
    return list(query)[0]

# if __name__ == '__main__':
#     test = ['qwerty', '1234', 0, 12.2, '', None]
#     for t in test:
#         print(t)
#         print(gen_pass(t))