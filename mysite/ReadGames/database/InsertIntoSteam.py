from .Connect_DB import connect, close_connection

from .Connect_DB import connect, close_connection

class Games():
    def __init__(self, id : str, name : str, support_info : str, dlc : str, Base_price : int, Current_price : int, Developer : str, Publisher,
                 Genre : str, Coming_soon : bool, Release_Date : str, Required_age : int, Controller_support : str, Website : str, Short_desc : str,
                 Detailed_desc : str, Supported_languages : str, windows : bool, linux : bool, mac : bool, Header_image : str):
        self.Insert_dict = {
            'id': id,
            'Name': name,
            'support_info': support_info,
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
            'Header_image' : Header_image
        }

        # Explicitly list the columns in the INSERT statement
        self.columns = ["id", "Name", "support_info", "DLC", "Base_price", "Current_price", "Developer", "Publisher",
                        "Genre", "Coming_soon", "Release_Date", "Required_age", "Controller_Support", "Website",
                        "Short_description", "Detailed_description", "Supported_languages", "windows", "linux", "mac", "Header_image"]

        self.insert()

    def insert(self):
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

        connection = connect()
        cursor = connection.cursor()

        cursor.execute(Insert_query, self.Insert_dict)
        connection.commit()  # Commit changes to the database

    # ... (other methods)

# If you have a specific table name for each class, you can pass it in the constructor.
# Example: super().__init__("Games", self.columns, self.insert_statement, self.values)
# This allows you to use the same class for multiple tables.


        # Modeling the DB
        # self.id = id
        # self.name = name
        # self.short_desc = short_description
        # self.min_req = minimum_req
        # self.rec_req = recommend_req

# if __name__ == '__main':
#     Games()



# class DLC(SteamTables):
#     def __init__(self, id, name, short_description, minimum_req, recommend_req):
#         self.id = id
#         self.name = name
#         self.short_desc = short_description
#         self.min_req = minimum_req
#         self.rec_req = recommend_req

#         self.Insert_dict = {
#             'id' : self.id,
#             'name' : self.name,
#             'short_desc' : self.short_desc,
#             'min_req' : self.min_req,
#             'rec_req' : self.rec_req,
#         }


#         self.insert_statement = """
#         INSERT INTO Games 
#         (id, name, short_desc, min_requirments, rec_requirements) 
#         VALUES (%(id)s, %(name)s, %(short_desc)s, %(min_req)s, %(rec_req)s); 
#         """



# class Demo():
#     def __init__(self, id, name, short_description, minimum_req, recommend_req):
#         self.id = id
#         self.name = name
#         self.short_desc = short_description
#         self.min_req = minimum_req
#         self.rec_req = recommend_req

#         self.Insert_dict = {
#             'id' : self.id,
#             'name' : self.name,
#             'short_desc' : self.short_desc,
#             'min_req' : self.min_req,
#             'rec_req' : self.rec_req,
#         }


#         self.insert_statement = """
#         INSERT INTO Games 
#         (id, name, short_desc, min_requirments, rec_requirements) 
#         VALUES (%(id)s, %(name)s, %(short_desc)s, %(min_req)s, %(rec_req)s); 
#         """
    


# class Music():
#     def __init__(self, id, name, short_description, minimum_req, recommend_req):
#         self.id = id
#         self.name = name
#         self.short_desc = short_description
#         self.min_req = minimum_req
#         self.rec_req = recommend_req

#         self.Insert_dict = {
#             'id' : self.id,
#             'name' : self.name,
#             'short_desc' : self.short_desc,
#             'min_req' : self.min_req,
#             'rec_req' : self.rec_req,
#         }


#         self.insert_statement = """
#         INSERT INTO Games 
#         (id, name, short_desc, min_requirments, rec_requirements) 
#         VALUES (%(id)s, %(name)s, %(short_desc)s, %(min_req)s, %(rec_req)s); 
#         """
   


# class Movies():
#     def __init__(self, id, name, short_description, minimum_req, recommend_req):
#         self.id = id
#         self.name = name
#         self.short_desc = short_description
#         self.min_req = minimum_req
#         self.rec_req = recommend_req

#         self.Insert_dict = {
#             'id' : self.id,
#             'name' : self.name,
#             'short_desc' : self.short_desc,
#             'min_req' : self.min_req,
#             'rec_req' : self.rec_req,
#         }


#         self.insert_statement = """
#         INSERT INTO Games 
#         (id, name, short_desc, min_requirments, rec_requirements) 
#         VALUES (%(id)s, %(name)s, %(short_desc)s, %(min_req)s, %(rec_req)s); 
#         """