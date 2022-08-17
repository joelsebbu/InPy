create database IRCTC;
use IRCTC;

create table Bookings(
	 aadhar int
	,name varchar(25)
	,constraint PK_Bookings primary key(aadhar)
);

create table Trains(
	 _index int
	,trainId varchar(25)
	,constraint PK_Trains primary key(trainId)
);

create table Stations(
	 stId int
	,name varchar(25)
	,constraint PK_Stations primary key(stId)
);

create table TVM_ALP(
	 aadhar int
	,fromId int
	,toId int
	,waitList bit
	,constraint PK_TVM_ALP primary key(aadhar)
	,constraint FK_TVM_ALP foreign key (aadhar) references Bookings(aadhar)
	,constraint FK_TVM_ALP_from foreign key (fromId) references Stations(stId)
	,constraint FK_TVM_ALP_to foreign key (toId) references Stations(stId)
);

create table TVM_ERN(
	 aadhar int
	,fromId int
	,toId int
	,waitList bit
	,constraint PK_TVM_ERN primary key(aadhar)
	,constraint FK_TVM_ERN foreign key (aadhar) references Bookings(aadhar)
	,constraint FK_TVM_ERN_from foreign key (fromId) references Stations(stId)
	,constraint FK_TVM_ERN_to foreign key (toId) references Stations(stId)
);

create table TVM_KOZ(
	 aadhar int
	,fromId int
	,toId int
	,waitList bit
	,constraint PK_TVM_KOZ primary key(aadhar)
	,constraint FK_TVM_KOZ foreign key (aadhar) references Bookings(aadhar)
	,constraint FK_TVM_KOZ_from foreign key (fromId) references Stations(stId)
	,constraint FK_TVM_KOZ_to foreign key (toId) references Stations(stId)
);

alter table Bookings
add trainId varchar(25) constraint FK_Trains foreign key(trainId) references Trains(trainId)

insert into Trains values(1,'TVM_ALP'),(2,'TVM_ERN'),(3,'TVM_KOZ');

insert into Stations values(0,'TVM'),(1,'ALP'),(2,'ERN'),(3,'KOZ');

select * from TVM_KOZ;