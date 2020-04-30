CREATE TABLE `db`.`Continental_Staff` (
  `Staff ID` VARCHAR(45) NOT NULL,
  `Salary` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Role` VARCHAR(45) NOT NULL,
  `idContinentals` VARCHAR(45) NOT NULL,
  FOREIGN KEY (`idContinentals`) REFERENCES Continentals(`idContinentals`),
  PRIMARY KEY (`Staff ID`));


insert into `Continental_Staff`  values ('92-897-6606', '18000', 'Jasun Froom',	 		'Moscow', 		'90-210-0391');
insert into `Continental_Staff`  values ('41-577-6808', '95900', 'Sawyer Spon', 		'Berlin', 		'23-739-7547');
insert into `Continental_Staff`  values ('30-902-2308', '52280', 'Nobe Cleworth', 		'Rio', 			'56-749-0064');
insert into `Continental_Staff`  values ('39-611-4736', '40000', 'Tom Finn',			'Denver', 		'34-940-3656');
insert into `Continental_Staff`  values ('68-858-1187', '46050', 'Jelene Jakubski', 	'Oslo', 		'02-254-3961');
insert into `Continental_Staff`  values ('35-203-9933', '53247', 'Gina Rousell', 		'Tokiyo', 		'80-860-8003');
insert into `Continental_Staff`  values ('26-386-4933', '87000', 'Wallace Linguard', 	'Nairobi', 		'88-625-5465');
insert into `Continental_Staff`  values ('92-507-6755', '97150', 'Willian Spacy', 		'Helsinki', 	'63-916-9347');
insert into `Continental_Staff`  values ('09-768-3563', '72190', 'Kevin Goldfinger', 	'Stockholm',	'49-082-6142');
insert into `Continental_Staff`  values ('49-654-9280', '66530', 'John Williamson', 	'Lisbon', 		'41-583-5857');
insert into `Continental_Staff`  values ('84-966-3837', '91500', 'Kate Blackwell', 		'London', 		'82-016-4173');
insert into `Continental_Staff`  values ('10-303-5472', '51525', 'Imran Wood', 			'Marsillise', 	'03-966-6665');
insert into `Continental_Staff`  values ('75-841-4009', '17900', 'Tyrell Wellick', 		'Copenhagen', 	'65-871-0931');
insert into `Continental_Staff`  values ('19-534-5492', '22380', 'Christian alderson',	'Sydney', 		'54-067-1967');
insert into `Continental_Staff`  values ('74-625-9264', '17000', 'Henry Arturito', 		'Perth', 		'65-911-4009');
insert into `Continental_Staff`  values ('09-455-8430', '12700', 'Sergio Martini', 		'Glasgow',	 	'01-470-7364');
insert into `Continental_Staff`  values ('10-304-5472', '50000', 'Frank Oxford', 		'Cairo', 		'49-835-1434'); changed
insert into `Continental_Staff`  values ('36-863-9311', '61000', 'Jim Abe', 			'Zurich', 		'79-260-1161');
insert into `Continental_Staff`  values ('80-796-2075', '55000', 'Rockford', 			'Paris', 		'56-948-6708');
insert into `Continental_Staff`  values ('06-404-1447', '90000', 'Chris Bryant', 		'Chicago', 		'40-834-9661');
