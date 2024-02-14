from .Connect_DB import connect, close_connection


class Games():
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
    def InDB(self, cursor):
        id = (self.Insert_dict["id"])
        SQL_Select_Query = """
        SELECT id FROM Games where id = %s"""
        cursor.execute(SQL_Select_Query, id)
        res = cursor.fetchone()

        if res:
            return True
        else:
            return False

    def insert_Into_Games(self, *args):
        if self.InDB():
            print("Won't insert, already in the Games table")
            return
        
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(self.insert_statement, args)

        # Commit changes to the DB
        connection.commit()

        print("Successfully inserted Game data into the table")

        self.close()


    def close(self, connection, cursor):
        close_connection(cursor=cursor, connection=connection)



