from asyncio.windows_events import NULL
import os
from sqlite3 import Cursor
from tkinter import CHAR
from xml.dom import UserDataHandler
import mysql.connector
import pandas as pd
import re

class DBEntry:
    def __init__(self):
        self.PatronTypeID = None
        self.PatronTypeDefinition = None
        self.TotalCheckots = None
        self.TotalRenews = None
        self.AgeRangeLow = None
        self.AgeRangehigh = None
        self.HomeLibraryCode = None
        self.HomeLibraryDefinition = None
        self.NotificationPreferenceCode = None
        self.NotificationCodeDefinition = None
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
    mycursor = mydb.cursor()
    #add these collumns
    print(df.columns)
    #go through all the lines in the DB
    for index, row in df.iterrows():
        NewRow = DBEntry()
        NewRow.PatronTypeID = row['ColumnA']
        NewRow.PatronTypeDefinition = row['ColumnB']
        NewRow.TotalCheckots = row['ColumnC']
        NewRow.TotalRenews = row['ColumnD']

        #get low and high age
        combinedAge = row['ColumnE']
        separatedAge = re.findall(r'\d+', combinedAge)
        low, high = map(int, separatedAge)
        NewRow.AgeRangeLow = low
        NewRow.AgeRangehigh = high

        NewRow.HomeLibraryCode = row['ColumnF']
        NewRow.HomeLibraryDefinition = row['ColumnG']
        NewRow.CirculationActiveMonth = row['ColumnH']
        NewRow.CirculationActiveYear = row['ColumnI']
        NewRow.NotificationPreferenceCode = row['ColumnJ']
        NewRow.NotificationCodeDefinition = row['ColumnK']
        NewRow.providedEmailAddress = row['ColumnL']
        NewRow.WithinSanFranciscoCounty = row['ColumnM']
        NewRow.PatronRegisterYear = row['ColumnN']
        print(index)


mycursor.execute("SHOW TABLES")
for db in mycursor:
    print(db)