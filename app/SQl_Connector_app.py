from sqlite3 import Cursor
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="RFAssignment1" # Optional: specify a database to connect to
    )
    print("Connected to MySQL database!")
except mysql.connector.Error as err:
    print(f"Error: {err}")


mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)