import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database_name" # Optional: specify a database to connect to
    )
    print("Connected to MySQL database!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

