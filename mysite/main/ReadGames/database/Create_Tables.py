from Connect_DB import connect, close_connection

def create_Table(create_table_query: str):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(create_table_query)

    # Finished with Executing queries
    close_connection(cursor=cursor, connection=connection)

# MAY CHANGE Release_Date to DATE type
# Platform may be split between 3 boolean fields
# windows, linux, mac
# Did not include Price overview for demo since it should always be 0.

table_Queries = [
    """
    CREATE TABLE IF NOT EXISTS Games(
    id CHAR(7) PRIMARY KEY, 
    Name VARCHAR(255),
    support_info VARCHAR(255),
    DLC TEXT,
    Base_price INT,
    Current_price INT,
    Developer VARCHAR(255),
    Publisher VARCHAR(255),
    Genre VARCHAR(255),
    Coming_soon Bit(1), 
    Release_Date VARCHAR(255),
    Required_age INT, 
    Controller_Support VARCHAR(255),
    Website VARCHAR(255),
    Short_description TEXT,
    Detailed_description TEXT,
    Supported_languages TEXT,
    windows Bit(1),
    linux Bit(1),
    mac Bit(1),
    Header_image VARCHAR(255)
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS DLC(
    id CHAR(7) PRIMARY KEY
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS Demo(
    id CHAR(7) PRIMARY KEY,
    Name VARCHAR(255),
    Support_Info VARCHAR(255),
    Developer VARCHAR(255),
    Publisher VARCHAR(255),
    Release_Date VARCHAR(255),
    Required_Age INT,
    Controller_Support Bit(1),
    Website VARCHAR(255),
    Short_description VARCHAR(255),
    Detailed_description TEXT,
    Supported_languages VARCHAR(255),
    PLATFORM VARCHAR(255),
    Header_image VARCHAR(255),
    Fullgame_id char(7),
    FOREIGN KEY (Fullgame_id) REFERENCES Games(id)
    )
    """,

    """
    CREATE TABLE IF NOT EXISTS Movies(
    id CHAR(7) PRIMARY KEY
    );
    """,

    """
    CREATE TABLE IF NOT EXISTS Music(
    id CHAR(7) PRIMARY KEY, 
    Name VARCHAR(255),
    support_info VARCHAR(255),
    Base_price INT,
    Current_price INT,
    Developer VARCHAR(255),
    Publisher VARCHAR(255),
    Coming_soon Bit(1), 
    Release_Date VARCHAR(255),
    Required_age INT, 
    Controller_Support VARCHAR(255),
    Website VARCHAR(255),
    Short_description TEXT,
    Detailed_description TEXT,
    Supported_languages TEXT,
    windows Bit(1),
    linux Bit(1),
    mac Bit(1),
    Header_image VARCHAR(255),
    Fullgame_id char(7),
    FOREIGN KEY (Fullgame_id) REFERENCES Games(id)
    );
    """
]

for table_query in table_Queries:
    create_Table(table_query)