import mysql.connector
from decouple import config


# Replace these values with your MySQL credentials
host = "localhost"
user = config("uname")
password = config("pass")
database = config("database")

# Establish a connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
)

# Create a cursor
cursor = connection.cursor()

# Execute SQL queries

# # Example: create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS your_table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT
);
"""
# create_table_games = """
# CREATE TABLE IF NOT EXISTS games (
#     appID INT PRIMARY_KEY,
#     name VARCHAR(255),
#     windows BOOL,
# );
# """
cursor.execute(create_table_query)

# Example: insert data
insert_data_query = """
INSERT INTO your_table_name (name, age) VALUES ('Jane Doe', 12);
"""
cursor.execute(insert_data_query)

# Commit the changes
connection.commit()

cursor.execute("select * from your_table_name;")
result = cursor.fetchall()  # or cursor.fetchone() or iterate through cursor


print(result)

# Close the cursor and connection
cursor.close()
connection.close()
