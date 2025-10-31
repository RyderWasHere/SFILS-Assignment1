CREATE DATABASE RfAssignment1;

use RfAssignment1;

CREATE TABLE PatronTypes(
PatronTypeID int,
PatronTypeDefinition varchar(225) NOT NULL,
PRIMARY KEY(PatronTypeID)
);

CREATE TABLE HomeLibararyCodes(
HomeLibraryCode varchar(2) NOT NULL,
HomeLibraryDefinition varchar(225),
PRIMARY KEY(HomeLibraryCode)
);
CREATE TABLE Patrons (
PatronID int auto_increment, 
PatronTypeID int NOT NULL,
TotalCheckouts int,
TotalRenews int,
AgeRangeLow int,
AgeRangeHigh int,
HomeLibraryCode varchar(2),
CirculationActiveMonth varchar(225),
CirculationActiveYear int,
NotificationPreferenceCode char,
providedEmailAddress bool,
WithinSanFranciscoCounty bool,
PatronRegisterYear int,
PRIMARY KEY (PatronID),
FOREIGN KEY(PatronTypeID) references PatronTypes(PatronTypeID),
FOREIGN KEY(HomeLibraryCode) references HomeLibararyCodes(HomeLibraryCode)
);
Show tables
/*
insert into PatronTypes (PatronTypeID, PatronTypeDefinition)
values 
	(0, 'Adult'),
	(1, 'Juvenile'),
	(2, 'Teen'),
    (3, 'Senior'),
    (4, 'Welcome'),
    (16, 'Digital Access Card');

insert into HomeLibararyCodes(HomeLibraryCode, HomeLibraryDefinition)
values
	('r3', 'RichMond'),
    ('x', 'Main'),
    ('m4', 'Merced'),
    ('b2', 'Bayview'),
    ('s7', 'Sunset'),
    ('m8', 'Mission Bay'), 
    ('p3', 'Parkside');
    */
    