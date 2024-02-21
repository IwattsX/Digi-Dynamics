from Connect_DB import connect, close_connection




class SteamTables():
    def __init__(self, table : str, columns : list, insert_dict):
        self.table = table
        self.columns = ','.join(columns)

        self.Insert_dict = insert_dict
    
    
    def InDB(self, cursor):
        id = (self.Insert_dict["id"])
        SQL_Select_Query = """
        SELECT id FROM {} where id = %s""".format(self.table)

        cursor.execute(SQL_Select_Query, id)
        res = cursor.fetchone()

        if res:
            return True
        else:
            return False

    def insert(self, *args):
        if len(args) != len(self.columns.split(',')):
            print("INVALID insert")
            return
        if self.InDB():
            print("Won't insert, already in the Games table")
            return
        
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(self.Insert_dict, args)

        # Commit changes to the DB
        connection.commit()

        print("Successfully inserted Game data into the table")

        self.close()

    def select(self,columns = "*", whereClause = None):
        query = ''
        if whereClause:
            query = f"SELECT {columns} FROM {self.table} WHERE {whereClause}"
        else:
            # SELECT ALL
            query = f"SELECT {columns} FROM {self.table}"
        
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query)

        res = cursor.fetchall()

        self.close()
        return res


    def close(self, connection, cursor):
        close_connection(cursor=cursor, connection=connection)


class Games(SteamTables):
    def __init__(self, id, name, short_description, minimum_req, recommend_req):
        self.Insert_dict = {
            'id' : self.id,
            'name' : self.name,
            'short_desc' : self.short_desc,
            'min_req' : self.min_req,
            'rec_req' : self.rec_req,
        }
        super().__init__("Games", ["id", "name"], self.Insert_dict)
    
        self.id = id
        self.name = name
        self.short_desc = short_description
        self.min_req = minimum_req
        self.rec_req = recommend_req




        self.insert_statement = """
        INSERT INTO Games 
        (id, name, short_desc, min_requirments, rec_requirements) 
        VALUES (%(id)s, %(name)s, %(short_desc)s, %(min_req)s, %(rec_req)s); 
        """




class DLC(SteamTables):
    def __init__(self, id, name, short_description, minimum_req, recommend_req):
        self.id = id
        self.name = name
        self.short_desc = short_description
        self.min_req = minimum_req
        self.rec_req = recommend_req

        self.Insert_dict = {
            'id' : self.id,
            'name' : self.name,
            'short_desc' : self.short_desc,
            'min_req' : self.min_req,
            'rec_req' : self.rec_req,
        }


        self.insert_statement = """
        INSERT INTO Games 
        (id, name, short_desc, min_requirments, rec_requirements) 
        VALUES (%(id)s, %(name)s, %(short_desc)s, %(min_req)s, %(rec_req)s); 
        """



class Demo():
    def __init__(self, id, name, short_description, minimum_req, recommend_req):
        self.id = id
        self.name = name
        self.short_desc = short_description
        self.min_req = minimum_req
        self.rec_req = recommend_req

        self.Insert_dict = {
            'id' : self.id,
            'name' : self.name,
            'short_desc' : self.short_desc,
            'min_req' : self.min_req,
            'rec_req' : self.rec_req,
        }


        self.insert_statement = """
        INSERT INTO Games 
        (id, name, short_desc, min_requirments, rec_requirements) 
        VALUES (%(id)s, %(name)s, %(short_desc)s, %(min_req)s, %(rec_req)s); 
        """
    


class Music():
    def __init__(self, id, name, short_description, minimum_req, recommend_req):
        self.id = id
        self.name = name
        self.short_desc = short_description
        self.min_req = minimum_req
        self.rec_req = recommend_req

        self.Insert_dict = {
            'id' : self.id,
            'name' : self.name,
            'short_desc' : self.short_desc,
            'min_req' : self.min_req,
            'rec_req' : self.rec_req,
        }


        self.insert_statement = """
        INSERT INTO Games 
        (id, name, short_desc, min_requirments, rec_requirements) 
        VALUES (%(id)s, %(name)s, %(short_desc)s, %(min_req)s, %(rec_req)s); 
        """
   


class Movies():
    def __init__(self, id, name, short_description, minimum_req, recommend_req):
        self.id = id
        self.name = name
        self.short_desc = short_description
        self.min_req = minimum_req
        self.rec_req = recommend_req

        self.Insert_dict = {
            'id' : self.id,
            'name' : self.name,
            'short_desc' : self.short_desc,
            'min_req' : self.min_req,
            'rec_req' : self.rec_req,
        }


        self.insert_statement = """
        INSERT INTO Games 
        (id, name, short_desc, min_requirments, rec_requirements) 
        VALUES (%(id)s, %(name)s, %(short_desc)s, %(min_req)s, %(rec_req)s); 
        """