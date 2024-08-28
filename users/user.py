import users.connection as connection
import datetime
import hashlib
#* 👆 Importing the MySQL module and connect with the data base


connect = connection.connect()
database = connect[0]
cursor = connect[1]

class User:
    
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
    
    #! Here, we can put a getter & setter method, but, we will work with properties directly (inside the class)
    
    def register(self):
        date = datetime.datetime.now()
        
        #* This is how we can encode the password
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
        #! This is to comprobe that the user exists
        sql = "SELECT * FROM users  WHERE email = %s AND password = %s"
        
        
        #* This is how we can encode the password
        encode = hashlib.sha256()
        encode.update(self.password.encode('utf8'))
        
        #! Data for consultation
        user = (self.email, encode.hexdigest())
        
        cursor.execute(sql, user)
        result = cursor.fetchone()
        
        return result