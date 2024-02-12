from Connect_DB import connect, close_connection

def create_Table(create_table_query: str):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(create_table_query)

    # Finished with Executing queries
    close_connection(cursor=cursor, connection=connection)

table_Queries = [
    """
    CREATE TABLE IF NOT EXISTS Games(
    id CHAR(7) PRIMARY KEY
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS DLC(
    id CHAR(7) PRIMARY KEY
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS Demo(
    id CHAR(7) PRIMARY KEY
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS Movies(
    id CHAR(7) PRIMARY KEY
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS Music(
    id CHAR(7) PRIMARY KEY
    );
    """
]

for table_query in table_Queries:
    create_Table(table_query)
