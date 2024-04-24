from .Connect_DB  import connect, close_connection

def inDB(cursor, table: str, dictionary_wID : dict) -> bool:
    query = f"SELECT id FROM {table} WHERE id = %s"
    cursor.execute(query, (dictionary_wID['id'],))
    
    res = cursor.fetchone()
    if res:
        return True
    else:
        return False


class Movies():
    def __init__(self, id : str, name: str, thumbnail : str, mp4_480p : str, mp4_max : str, 
                 webm_480p : str, webm_max : str, game_ID : str):
        self.Insert_dict = {
            "id" : id,
            "name" : name,
            "thumbnail" : thumbnail,
            "mp4_480p" : mp4_480p,
            "mp4_max" : mp4_max,
            "webm_480p" : webm_480p,
            "webm_max" : webm_max,
            "game_ID" : game_ID
        }

        self.columns = ["id", "name", "thumbnail", "mp4_480p", "mp4_max", "webm_480p", "webm_max", "game_ID"]

        self.insert()
        
    def insert(self):
        connection = connect()
        cursor = connection.cursor()

        if inDB(cursor, "Games", {'id' : self.Insert_dict["game_ID"]}):
            print("Foreign key is in the database games")
            print(self.Insert_dict["game_ID"])
        else:
            # print("Fullgame is not in the Games database")
            close_connection(connection=connection, cursor=cursor)
            return
        

        if inDB(cursor, "Movies", self.Insert_dict):
            print("Already inserted into the table")
            close_connection(connection=connection, cursor=cursor)
            return
        
        Insert_query = f"""
        INSERT INTO Movies 
        ({', '.join(self.columns)}) 
        VALUES
        (
            %(id)s,
            %(name)s,
            %(thumbnail)s,
            %(mp4_480p)s,
            %(mp4_max)s,
            %(webm_480p)s,
            %(webm_max)s,
            %(game_ID)s
        );
        """

        cursor.execute(Insert_query, self.Insert_dict)
        connection.commit()  # Commit changes to the database

        close_connection(connection=connection, cursor=cursor)


class Games():
    def __init__(self, id : str, name : str, support_info : str, dlc : str, Base_price : int, Current_price : int, Developer : str, Publisher,
                 Genre : str, Coming_soon : bool, Release_Date : str, Required_age : int, Controller_support : str, Website : str, Short_desc : str,
                 Detailed_desc : str, Supported_languages : str, windows : bool, linux : bool, mac : bool, Header_image : str):
        self.Insert_dict = {
            'id': id,
            'Name': name,
            'support_info': support_info if support_info != '' else None,
            'DLC': dlc,
            'Base_price': Base_price,
            'Current_price': Current_price,
            'Developer' : Developer,
            'Publisher' : Publisher,
            'Genre' : Genre,
            'Coming_soon': Coming_soon,
            'Release_Date' : Release_Date,
            'Required_age' : Required_age,
            'Controller_Support' : Controller_support,
            'Website' : Website,
            'Short_description' : Short_desc,
            'Detailed_description': Detailed_desc,
            'Supported_languages': Supported_languages,
            'windows': windows,
            'linux': linux,
            'mac': mac,
            'Header_image': Header_image
        }

        # Explicitly list the columns in the INSERT statement
        self.columns = ["id", "Name", "support_info", "DLC", "Base_price", "Current_price", "Developer", "Publisher",
                        "Genre", "Coming_soon", "Release_Date", "Required_age", "Controller_Support", "Website",
                        "Short_description", "Detailed_description", "Supported_languages", "windows", "linux", "mac", "Header_image"]

        self.insert()
    
    def insert(self):

        connection = connect()
        cursor = connection.cursor()

        if inDB(cursor, "Games", self.Insert_dict):
            # print("Already inserted into the table")
            close_connection(connection=connection, cursor=cursor)
            return
        

        Insert_query = f"""
        INSERT INTO Games 
        ({', '.join(self.columns)}) 
        VALUES
        (
        %(id)s,
        %(Name)s,
        %(support_info)s,
        %(DLC)s,
        %(Base_price)s,
        %(Current_price)s,
        %(Developer)s,
        %(Publisher)s,
        %(Genre)s,
        %(Coming_soon)s,
        %(Release_Date)s,
        %(Required_age)s,
        %(Controller_Support)s,
        %(Website)s,
        %(Short_description)s,
        %(Detailed_description)s,
        %(Supported_languages)s,
        %(windows)s,
        %(linux)s,
        %(mac)s,
        %(Header_image)s
        );
        """

        cursor.execute(Insert_query, self.Insert_dict)
        connection.commit()  # Commit changes to the database

        close_connection(connection=connection, cursor=cursor)

class DLC():
    def __init__(self, id : str, name : str, support_info : str, Base_price : int, Current_price : int, Developer : str, Publisher,
                 Genre : str, Coming_soon : bool, Release_Date : str, Required_age : int, Controller_support : str, Website : str, Short_desc : str,
                 Detailed_desc : str, Supported_languages : str, windows : bool, linux : bool, mac : bool, Header_image : str, Fullgame_id : str):
        
        self.Insert_dict = {
            'id': id,
            'Name': name,
            'support_info': support_info if support_info != '' else None,
            'Base_price': Base_price,
            'Current_price': Current_price,
            'Developer' : Developer,
            'Publisher' : Publisher,
            'Genre' : Genre,
            'Coming_soon': Coming_soon,
            'Release_Date' : Release_Date,
            'Required_age' : Required_age,
            'Controller_Support' : Controller_support,
            'Website' : Website,
            'Short_description' : Short_desc,
            'Detailed_description': Detailed_desc,
            'Supported_languages': Supported_languages,
            'windows': windows,
            'linux': linux,
            'mac': mac,
            'Header_image': Header_image,
            "Fullgame_id" : Fullgame_id,
        }


        # Explicitly list the columns in the INSERT statement
        self.columns = ["id", "Name", "support_info", "Base_price", "Current_price", "Developer", "Publisher",
                        "Genre", "Coming_soon", "Release_Date", "Required_age", "Controller_Support", "Website",
                        "Short_description", "Detailed_description", "Supported_languages", "windows", "linux", "mac", "Header_image", "Fullgame_id"]

        self.insert()
    
    def insert(self):

        connection = connect()
        cursor = connection.cursor()

        if inDB(cursor, "Games", {'id' : self.Insert_dict["Fullgame_id"]}):
            print("Foreign key is in the database games")
            print(self.Insert_dict["Fullgame_id"])
        else:
            # print("Fullgame is not in the Games database")
            close_connection(connection=connection, cursor=cursor)
            return
        

        if inDB(cursor, "dlc", self.Insert_dict):
            print("Already inserted into the table")
            close_connection(connection=connection, cursor=cursor)
            return
        

        Insert_query = f"""
        INSERT INTO dlc 
        ({', '.join(self.columns)}) 
        VALUES
        (
        %(id)s,
        %(Name)s,
        %(support_info)s,
        %(Base_price)s,
        %(Current_price)s,
        %(Developer)s,
        %(Publisher)s,
        %(Genre)s,
        %(Coming_soon)s,
        %(Release_Date)s,
        %(Required_age)s,
        %(Controller_Support)s,
        %(Website)s,
        %(Short_description)s,
        %(Detailed_description)s,
        %(Supported_languages)s,
        %(windows)s,
        %(linux)s,
        %(mac)s,
        %(Header_image)s,
        %(Fullgame_id)s
        );
        """

        cursor.execute(Insert_query, self.Insert_dict)
        connection.commit()  # Commit changes to the database

        close_connection(connection=connection, cursor=cursor)


class Music():
    def __init__(self, id : str, name : str, support_info : str, Base_price : int, Current_price : int, Developer : str, Publisher,
                Coming_soon : bool, Release_Date : str, Required_age : int, Controller_support : str, Website : str, Short_desc : str,
                 Detailed_desc : str, Supported_languages : str, windows : bool, linux : bool, mac : bool, Header_image : str, Fullgame_id : str):
        self.Insert_dict = {
            'id': id,
            'Name': name,
            'support_info': support_info if support_info != '' else None,
            'Base_price': Base_price,
            'Current_price': Current_price,
            'Developer' : Developer,
            'Publisher' : Publisher,
            'Coming_soon': Coming_soon,
            'Release_Date' : Release_Date,
            'Required_age' : Required_age,
            'Controller_Support' : True if Controller_support else False,
            'Website' : Website,
            'Short_description' : Short_desc,
            'Detailed_description': Detailed_desc,
            'Supported_languages': Supported_languages,
            'windows': windows,
            'linux': linux,
            'mac': mac,
            'Header_image' : Header_image,
            "Fullgame_id" : Fullgame_id,
        }

        self.columns = ["id", "Name", "support_info", "Base_price", "Current_price", "Developer", "Publisher",
                        "Coming_soon", "Release_Date", "Required_age", "Controller_Support", "Website",
                        "Short_description", "Detailed_description", "Supported_languages", "windows", "linux", "mac", "Header_image", "Fullgame_id"]

        self.insert()

        

    def insert(self):

        connection = connect()
        cursor = connection.cursor()

        if inDB(cursor, "Games", {'id' : self.Insert_dict["Fullgame_id"]}):
            print("Foreign key is in the database games")
            print(self.Insert_dict["Fullgame_id"])
        else:
            # print("Fullgame is not in the Games database")
            close_connection(connection=connection, cursor=cursor)
            return
        

        if inDB(cursor, "Music", self.Insert_dict):
            print("Already inserted into the table")
            close_connection(connection=connection, cursor=cursor)
            return
        

        Insert_query = f"""
        INSERT INTO Music 
        ({', '.join(self.columns)}) 
        VALUES
        (
        %(id)s,
        %(Name)s,
        %(support_info)s,
        %(Base_price)s,
        %(Current_price)s,
        %(Developer)s,
        %(Publisher)s,
        %(Coming_soon)s,
        %(Release_Date)s,
        %(Required_age)s,
        %(Controller_Support)s,
        %(Website)s,
        %(Short_description)s,
        %(Detailed_description)s,
        %(Supported_languages)s,
        %(windows)s,
        %(linux)s,
        %(mac)s,
        %(Header_image)s,
        %(Fullgame_id)s
        );
        """

        cursor.execute(Insert_query, self.Insert_dict)
        connection.commit()  # Commit changes to the database

        close_connection(connection=connection, cursor=cursor)


class Demo():
    def __init__(self, id : str, name : str, support_info : str, Developer : str, Publisher,
                 Genre : str, Release_Date : str, Required_age : int, Controller_support : str, Website : str, Short_desc : str,
                 Detailed_desc : str, Supported_languages : str, windows : bool, linux : bool, mac : bool, Header_image : str, Fullgame_id : str):
        
        self.Insert_dict = {
            'id': id,
            'Name': name,
            'support_info': support_info if support_info != '' else None,
            'Developer' : Developer,
            'Publisher' : Publisher,
            'Genre' : Genre,
            'Release_Date' : Release_Date,
            'Required_age' : Required_age,
            'Controller_Support' : Controller_support,
            'Website' : Website,
            'Short_description' : Short_desc,
            'Detailed_description': Detailed_desc,
            'Supported_languages': Supported_languages,
            'windows': windows,
            'linux': linux,
            'mac': mac,
            'Header_image': Header_image,
            "Fullgame_id" : Fullgame_id,
        }


        # Explicitly list the columns in the INSERT statement
        self.columns = ["id", "Name", "support_info", "Developer", "Publisher",
                        "Genre","Release_Date", "Required_age", "Controller_Support", "Website",
                        "Short_description", "Detailed_description", "Supported_languages", "windows", "linux", "mac", "Header_image", "Fullgame_id"]

        self.insert()
    
    def insert(self):

        connection = connect()
        cursor = connection.cursor()

        if inDB(cursor, "Games", {'id' : self.Insert_dict["Fullgame_id"]}):
            print("Foreign key is in the database games")
            print(self.Insert_dict["Fullgame_id"])
        else:
            # print("Fullgame is not in the Games database")
            close_connection(connection=connection, cursor=cursor)
            return
        

        if inDB(cursor, "Demo", self.Insert_dict):
            print("Already inserted into the table")
            close_connection(connection=connection, cursor=cursor)
            return
        

        Insert_query = f"""
        INSERT INTO Demo 
        ({', '.join(self.columns)}) 
        VALUES
        (
        %(id)s,
        %(Name)s,
        %(support_info)s,
        %(Developer)s,
        %(Publisher)s,
        %(Genre)s,
        %(Release_Date)s,
        %(Required_age)s,
        %(Controller_Support)s,
        %(Website)s,
        %(Short_description)s,
        %(Detailed_description)s,
        %(Supported_languages)s,
        %(windows)s,
        %(linux)s,
        %(mac)s,
        %(Header_image)s,
        %(Fullgame_id)s
        );
        """

        print(Insert_query)

        cursor.execute(Insert_query, self.Insert_dict)
        connection.commit()  # Commit changes to the database

        close_connection(connection=connection, cursor=cursor)