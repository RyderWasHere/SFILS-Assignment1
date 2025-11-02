CREATE DATABASE RfAssignment1;

use RfAssignment1;
CREATE TABLE PatronTypes(
PatronTypeID int,
PatronTypeDefinition varchar(225) NOT NULL,
PRIMARY KEY(PatronTypeID)
);

CREATE TABLE HomeLibararyCodes(
HomeLibraryCode varchar(10) NOT NULL,
HomeLibraryDefinition varchar(225),
PRIMARY KEY(HomeLibraryCode)
);
Create Table NotificationCodes(
NotificationPreferenceCode char,
NotificationCodeDefinition varchar(225),
PRIMARY KEY(NotificationPreferenceCode)
);
CREATE TABLE Patrons (
PatronID int auto_increment, 
PatronTypeID int NOT NULL,
TotalCheckouts int,
TotalRenews int,
AgeRangeLow int,
AgeRangeHigh int,
HomeLibraryCode varchar(10),
CirculationActiveMonth varchar(225),
CirculationActiveYear int,
NotificationPreferenceCode char,
providedEmailAddress bool,
WithinSanFranciscoCounty bool,
PatronRegisterYear int,
PRIMARY KEY (PatronID),
FOREIGN KEY(PatronTypeID) references PatronTypes(PatronTypeID),
FOREIGN KEY(HomeLibraryCode) references HomeLibararyCodes(HomeLibraryCode),
FOREIGN KEY(NotificationPreferenceCode) references NotificationCodes(NotificationPreferenceCode)
);

    
