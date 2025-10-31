from sqlite3 import Cursor
import mysql.connector
import pandas as pd
class DBEntry:
    def __init__(self, PatronTypeID):
        self.PatronTypeID = PatronTypeID
        self.TotalCheckots = TotalCheckouts
        self.TotalRenews 
        self.AgeRangeLow
        self.AgeRangehigh
        self.HomeLibraryCode
        self.CirculationActiveMonth
        self.CirculationActiveYear
        self.NotificationPreferenceCode
        self.providedEmailAddress
        self.WithinSanFranciscoCounty
        self.PatronRegisterYear
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
def WritePatronType(mycursor):
    return
def WriteLibraryCode(mucursor):
    return

#opening file to be read
df = pd.read_excel('Sample.xlsx', sheet_name='Sheet1')

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")


for db in mycursor:
    print(db)