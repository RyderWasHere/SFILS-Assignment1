from asyncio.windows_events import NULL
import math
from math import isnan, nan
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
        NewRow.PatronTypeID = row['Patron Type Code\npatron_type_code']
        NewRow.PatronTypeDefinition = row['Patron Type Definition\n']
        NewRow.TotalCheckots = row['Total Checkouts\ncheckout_total']
        NewRow.TotalRenews = row['Total Renewals\nrenewal_total']

        #get low and high age
        combinedAge = row['Age Range\n']
        #not the best way to handle this case but it works
        try:
            separatedAge = re.findall(r'\d+', combinedAge)
            try:
                low, high = map(int, separatedAge)
                NewRow.AgeRangeLow = low
                NewRow.AgeRangehigh = high
            except:
                NewRow.AgeRangeLow = separatedAge
                NewRow.AgeRangehigh = None
        except:
            NewRow.AgeRangeLow = None
            NewRow.AgeRangehigh = None
        NewRow.HomeLibraryCode = row['Home Library Code\nhome_library_code']
        NewRow.HomeLibraryDefinition = row['Home Library Definition\n']
        NewRow.CirculationActiveMonth = row['Circulation Active Month\n']
        NewRow.CirculationActiveYear = row['Circulation Active Year\n']
        NewRow.NotificationPreferenceCode = row['Notification Preference Code\nnotification_medium_code']
        NewRow.NotificationCodeDefinition = row['Notification Code Definition']
        NewRow.providedEmailAddress = row['Provided Email Address\n']
        NewRow.WithinSanFranciscoCounty = row['Within San Francisco County']
        NewRow.PatronRegisterYear = row['Year Patron Registered']
        print(index)


mycursor.execute("SHOW TABLES")
for db in mycursor:
    print(db)