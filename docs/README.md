# Project Documentation
## how to import excel sheet
This project uses python as its primary language and requires a few libaries to function
- Pandas
- mysql Connector
- openpyxl
1. Start your SQL server
   - Create your sql server and run the CreateFile.sql
   - You may ned to modify ```SQl_Connector_app.py``` to start the program. The database information is located from line 93 to 97. Make sure your login is accurate
2. import your spreadsheet
   - Make sure your desired Database file is located in the apps folder. Make sure its titled ```Sample.xlsx```
  - Start the ```SQl_Connector_app.py``` program
  - Select 1 to import database
  - wait patiently. Sample file from assignment took about 10 minutes
## How to run commands
  1. Start ```SQl_Connector_app.py``` and select 2 or 3
  2. From here you are able to select from a list of options to navigate the database
  ## AI disclaimer
  AI wass used for line 91-96 for the code snipit and the handle_foreign_key_error funciton
