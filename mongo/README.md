# MISFILS
MISFILS: The MongoDB-based Implementation for the San Francisco Integrated Library System.

This folder contains the submission files for Assignment 2. The remaining folders contain the files from Assignment 1.

Make sure to keep all your Assignment 2 files inside this folder to keep the rest of the folders free from clutter. That way, it will be easier to grade both Assignment 1 and Assignment 2.
# Sorry :(
All of the files for MongoDb are contained in the original spots since I just built the implementation on top of the origional program and I don't want to cause issues shuffling things around.
However, I will provide a guide on what is new since last implementation
## New features
- Added new enum type DDType for logic to swap depending on what database you are using which includes
- A new input required to select which database type you will be using
- Case statements will swap to what logic you need to be using for each implementation
- Timer added that starts when opening the document to finishing populating database
- New Reflection doc(unsure if this was required)
## New functions
### M_WritePatron
Since MongoDB is a lazy database, there is no foreign key support so instead of recursively adding to the foreign key table, I instead check ahead of time.
The checkCollections function is called to update the other collections and then the current Patron is added to the table
### M_checkCollections
Goes through the 3 different collections and checks to see if the current ID exists in each of the collections, if not add it to the collection
### Other Collections
These do the same thing but for other collections 
- M_WritePatronType
- M_WriteLibraryCode
- M_WriteNotificationCode
## New query options
Upon Selecting MongoDB, you will get to make select querys for the mongodb implementation from line 286 to 319