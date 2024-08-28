import mysql.connector
#! Creating the data base variable for connection

def connect():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "console_notes",
        port = 3306
    )
    cursor = database.cursor(buffered=True)
    
    return[database, cursor]