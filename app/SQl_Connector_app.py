from asyncio.windows_events import NULL
from enum import Enum
from importlib.abc import PathEntryFinder
import math
from math import isnan, nan
import time
import os
from sqlite3 import Cursor
from tkinter import CHAR
from xml.dom import UserDataHandler
import mysql.connector
import pandas as pd
import re
import pymongo
from pymongo import MongoClient
from enum import Enum

#define enums to allow connection to both databases
class DDType(Enum):
    Mysql = 1
    MongoDb = 2
DatabaseType = None

class DBEntry:
    def __init__(self):
        self.PatronTypeID = None
        self.PatronTypeDefinition = None
        self.TotalCheckouts = None
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

#mysql files
def handle_foreign_key_error(err):
    match = re.search(r"CONSTRAINT `([^`]+)` FOREIGN KEY", err.msg)
    return match.group(1)
def WritePatronType(mycursor, Entry: DBEntry):
    sql = "INSERT INTO PatronTypes( PatronTypeID, PatronTypeDefinition) VALUES (%s, %s)"
    values = (Entry.PatronTypeID, Entry.PatronTypeDefinition)
    try:
        mycursor.execute(sql, values)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    return
def WriteLibraryCode(mycursor, Entry: DBEntry):
    sql = "INSERT INTO HomeLibararyCodes( HomeLibraryCode, HomeLibraryDefinition) VALUES (%s, %s)"
    values = (Entry.HomeLibraryCode, Entry.HomeLibraryDefinition)
    try:
        mycursor.execute(sql, values)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    return
def WriteNotificationCode(mycursor, Entry: DBEntry):
    sql = "INSERT INTO NotificationCodes( NotificationPreferenceCode, NotificationCodeDefinition) VALUES (%s, %s)"
    values = (Entry.NotificationPreferenceCode, Entry.NotificationCodeDefinition)
    try:
        mycursor.execute(sql, values)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    return
def WritePatron(mycursor, Entry: DBEntry):
    sql = "INSERT INTO Patrons ( PatronTypeID, TotalCheckouts, TotalRenews, AgeRangeLow, AgeRangeHigh, HomeLibraryCode, CirculationActiveMonth, CirculationActiveYear, NotificationPreferenceCode, providedEmailAddress, WithinSanFranciscoCounty, PatronRegisterYear) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (Entry.PatronTypeID, Entry.TotalCheckouts, Entry.TotalRenews, Entry.AgeRangeLow, Entry.AgeRangehigh, Entry.HomeLibraryCode, Entry.CirculationActiveMonth, Entry.CirculationActiveYear, Entry.NotificationPreferenceCode, Entry.providedEmailAddress, Entry.WithinSanFranciscoCounty, Entry.PatronRegisterYear)
    try:
        mycursor.execute(sql, values)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        ferror  = handle_foreign_key_error(err)
        if ferror == 'patrons_ibfk_1':
            WritePatronType(mycursor, Entry)
            WritePatron(mycursor, Entry)
        elif ferror == 'patrons_ibfk_2':
            WriteLibraryCode(mycursor, Entry)
            WritePatron(mycursor, Entry)
        elif ferror == 'patrons_ibfk_3':
            WriteNotificationCode(mycursor, Entry)
            WritePatron(mycursor, Entry)
    return

#mongoDB files
def M_WritePatronType(Entry: DBEntry):
    collection = Mdb["PatronTypes"]
    ToInsert = {"TypeID": Entry.PatronTypeID, "Type" : Entry.PatronTypeDefinition}
    x = collection.insert_one(ToInsert)
    print(x.inserted_id,ToInsert)
    return
def M_WriteLibraryCode(Entry: DBEntry):
    collection  = Mdb["HomeLibraryCodes"]
    ToInsert = {"LibraryID" : Entry.HomeLibraryCode, "LibraryDef": Entry.HomeLibraryDefinition}
    x = collection.insert_one(ToInsert)
    print(x.inserted_id,ToInsert)
    return
def M_WriteNotificationCode(Entry: DBEntry):
    collection = Mdb["NotificationCodes"]
    ToInsert = {"NotificationCode": Entry.NotificationPreferenceCode, "NotificationType": Entry.NotificationCodeDefinition}
    x = collection.insert_one(ToInsert)
    print(x.inserted_id, ToInsert)
    return
def M_WritePatron(Entry: DBEntry):
    #perform checks to see if data exists in other tables
    M_checkCollections(Entry)
    collection = Mdb["Patrons"]
    ToInsert = {
        "TotalCheckouts" : Entry.TotalCheckouts,
        "TotalRenews" : Entry.TotalRenews,
        "AgeRangeLow" : Entry.AgeRangeLow,
        "AgeRangeHigh" : Entry.AgeRangehigh,
        "HomeLibraryCode" : Entry.HomeLibraryCode,
        "CirculationActiveMonth" : Entry.CirculationActiveMonth,
        "CirculationActiveYear" : Entry.CirculationActiveYear,
        "NotificationPreferenceCode" : Entry.NotificationPreferenceCode,
        "ProvidedEmailAddress" : Entry.providedEmailAddress,
        "WithinSanFranciscoCounty" : Entry.WithinSanFranciscoCounty,
        "PatronRegisterYear" : Entry.PatronRegisterYear
        }
    x = collection.insert_one(ToInsert)
    return
def M_checkCollections(Entry: DBEntry):
    #PatronTypes Check
    collection = Mdb["PatronTypes"]
    x = collection.find_one({"TypeID": Entry.PatronTypeID})
    if x is None:
        M_WritePatronType(Entry)
    #libararyCodes Check
    collection = Mdb["HomeLibraryCodes"]
    x = collection.find_one({"LibraryID": Entry.HomeLibraryCode})
    if x is None:
        M_WriteLibraryCode(Entry)
    #NotificationCodeCheck
    collection = Mdb["NotificationCodes"]
    x = collection.find_one({"NotificationCode": Entry.NotificationPreferenceCode})
    if x is None:
        M_WriteNotificationCode(Entry)
    return
def Corected(value):
    if value in [' ', '-', '']:
        return None
    elif isinstance(value, (int, float)) and math.isnan(value):
        return None
    else:
        return value


#main
print("Please Select database to connect to:")
print("1 - Mysql\n2 - MongoDb")
userinput = input()
match userinput:
    case "1":
        DatabaseType = DDType.Mysql
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="admin",
                database="RFAssignment1"
            )
            print("Connected to RFAssignment1 database!")
            mycursor = mydb.cursor()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    case "2":
        DatabaseType = DDType.MongoDb
        try:
            client = MongoClient("mongodb://localhost:27017/")
            print(client.list_database_names)
            Mdb = client["LibraryDB"]
            collection = Mdb["Patrons"]
            print("Connected to RFAssignment1 Database!")
        except:
            print("Something went wrong! Could not connect")


print("1 - import Sample.xlsx file\n2 - query existing database\n3 - Expert mode: Direct SQL queries")
userinput = input()
mytime = time.time()
if int(userinput) == 1:
    print("opening Sample.xlsn file...")
    #opening file to be read
    try:
        df = pd.read_excel('app/Sample.xlsx', sheet_name='Sheet1')
    except:
        print("failed to open file")
    #add these collumns
    print(df.columns)
    #go through all the lines in the DB
    for index, row in df.iterrows():
        NewRow = DBEntry()
        NewRow.PatronTypeID = row['Patron Type Code\npatron_type_code']
        NewRow.PatronTypeDefinition = row['Patron Type Definition\n']
        NewRow.TotalCheckouts = row['Total Checkouts\ncheckout_total']
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
                NewRow.AgeRangeLow = int(separatedAge)
                NewRow.AgeRangehigh = None
        except:
            NewRow.AgeRangeLow = None
            NewRow.AgeRangehigh = None
        NewRow.HomeLibraryCode = Corected(row['Home Library Code\nhome_library_code'])
        NewRow.HomeLibraryDefinition = row['Home Library Definition\n']
        #some genius went through and put a space on every single row 
        NewRow.CirculationActiveMonth = Corected(row['Circulation Active Month\n'])
        NewRow.CirculationActiveYear = Corected(row['Circulation Active Year\n'])
        NewRow.NotificationPreferenceCode = Corected(row['Notification Preference Code\nnotification_medium_code'])
        NewRow.NotificationCodeDefinition = row['Notification Code Definition']
        NewRow.providedEmailAddress = row['Provided Email Address\n']
        NewRow.WithinSanFranciscoCounty = row['Within San Francisco County']
        NewRow.PatronRegisterYear = row['Year Patron Registered']
        print(index)
        match DatabaseType:
            case DDType.Mysql:
                WritePatron(mycursor, NewRow)
            case DDType.MongoDb:
                M_WritePatron(NewRow)
    print("Database populated in {:.2f} seconds".format(time.time() - mytime))
elif int(userinput) == 3:
    print("Try quering database - type exit to quit")
    conquery = True
    while conquery == True:
        userinput = input()
        if userinput != exit:
            #horrible horrible horible
            mycursor.execute(userinput)
            for db in mycursor:
                print(db)
        else:
            conquery = False
else:
    conquery = True
    while conquery:
        print("Options:")
        print("1 - Show tables")
        print("2 - select a patron by ID")
        print("3 - Show Patron Types")
        print("4 - Show Home Libary Codes")
        print("5 - Show Notification Codes")
        print("exit - to exit\n")
        userinput = input()
        match userinput:
            case "1":
                mycursor.execute("SHOW TABLES")
            case "2":
                print("Enter Patron ID")
                userinput = input()
                mycursor.execute("SELECT * FROM Patrons WHERE PatronID = %s", (int(userinput),))
            case "3":
                mycursor.execute("SELECT * FROM PatronTypes")
            case "4":
                mycursor.execute("SELECT * FROM HomeLibararyCodes")
            case "5":
                mycursor.execute("SELECT * FROM NotificationCodes")
            case "exit":
                conquery = False

        results = mycursor.fetchall() 
        for row in results:
            print(row)
    
mycursor.close()
mydb.close()
