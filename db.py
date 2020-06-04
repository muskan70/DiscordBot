import sqlite3

"""
Database class is implemented to connect sqlite3 db with bot.
It takes name of db as argument.
It contains two functions insertDb and queryDb.
"""
class DataBase:
    #Make table HISTORY if not exists
    def __init__(self, db):
        self.db = db
        try:
            self.conn = sqlite3.connect(self.db)
            self.conn.execute('''CREATE TABLE IF NOT EXISTS HISTORY
                    (USERNAME           VARCHAR    NOT NULL,
                    KEYWORD            VARCHAR     NOT NULL,
                    PRIMARY KEY (USERNAME,KEYWORD));''')
            self.conn.close()        
        except Exception as e:
            print(e)
        print("database connection established")

    #Insert in table,takes two arguments user,searchWord 
    def insertDb(self,user,searchWord):  
        conn = sqlite3.connect(self.db)
        query="INSERT INTO HISTORY (USERNAME,KEYWORD) VALUES ('" + user + "','" + searchWord + "')"
        try:
            conn.execute(query);
        except :
            print("Unable to insert in database")   
        conn.commit()
        conn.close() 

    #Query history of that user related to that particular word
    # takes two arguments user,searchWord and return all the past search topics related to that searchword
    def queryDb(self,user,searchWord):
        conn = sqlite3.connect(self.db)
        query= "SELECT KEYWORD from HISTORY WHERE USERNAME = '" + user +"' and KEYWORD LIKE '%" + searchWord +"%'"
        try:
            cursor = conn.execute(query)
        except:
            return "Unable to process query"    

        ans=[i[0] for i in cursor]
        conn.close()
        return ','.join(ans)

