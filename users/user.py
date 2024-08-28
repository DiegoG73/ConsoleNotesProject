import mysql.connector
import datetime
import hashlib
#* 👆 Importing the MySQL module and connect with the data base


#! Creating the data base variable for connection

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "console_notes",
    port = 3306
)

#! Creating the cursor to can make consults
#* REMEMBER: the buffered=True parameter is to could use the the cursor multiple times
cursor = database.cursor(buffered=True)

print(database)

class User:
    
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
    
    #! Here, we can put a getter & setter method, but, we will work with properties directly (inside the class)
    
    def register(self):
        date = datetime.datetime.now()
        
        #* Así ciframos la contraseña:
        encode = hashlib.sha256()
        encode.update(self.password.encode('utf8'))
        
        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.surname, self.email, encode.hexdigest(), date)
        
        try:
            cursor.execute(sql, user)
            database.commit()    
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result
        
    def identify(self):
        return self.name