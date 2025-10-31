from asyncio.windows_events import NULL
import os
from sqlite3 import Cursor
from tkinter import CHAR
from xml.dom import UserDataHandler
import mysql.connector
import pandas as pd

class DBEntry:
    def __init__(self):
        self.PatronTypeID = None
        self.TotalCheckots = None
        self.TotalRenews = None
        self.AgeRangeLow = None
        self.AgeRangehigh = None
        self.HomeLibraryCode = None
        self.NotificationPreferenceCode = None
        self.CirculationActiveMonth = None
        self.CirculationActiveYear = None
        self.providedEmailAddress = None
        self.WithinSanFranciscoCounty = None
        self.PatronRegisterYear = None

def WritePatronType(mycursor):
    return

def WriteLibraryCode(mycursor):
    return
def WritePatron(mycursor):
    return

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="RFAssignment1" # Optional: specify a database to connect to
    )
    print("Connected to RFAssignment1 database!")
except mysql.connector.Error as err:
    print(f"Error: {err}")


print("1 - import Sample.xlsx file\n2 - query existing database")
userinput = input()

if int(userinput) == 1:
    print("opening Sample.xlsn file...")
    #opening file to be read
    try:
        df = pd.read_excel('app/Sample.xlsx', sheet_name='Sheet1')
        
    except:
        print("failed to open file")
    #go through all the lines in the DB
    for index, row in df.iterrows():

        print(index)
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")
for db in mycursor:
    print(db)