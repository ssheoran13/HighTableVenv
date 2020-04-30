CREATE TABLE `db`.`Deals Proposed` (
  `Deal ID` VARCHAR(45) NOT NULL,
  `Client ID` VARCHAR(45) NOT NULL,
  `idContinentals` VARCHAR(45) NOT NULL,
  `Client Name` VARCHAR(45) NOT NULL,
  `Work` VARCHAR(45) NOT NULL,
  `Min reward` VARCHAR(45) NOT NULL,
  `Client Contact` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Deal ID`),
  FOREIGN KEY (`idContinentals`) REFERENCES Continentals(`idContinentals`),
  FOREIGN KEY (`Client ID`) REFERENCES Clients(`Client ID`)
  );

insert into `Deals Proposed`  values ('54-464-6842', '65-841-6296', '90-210-0391', 'Sissie Quibell', 		'Scouting', 		'5287519400', 'squibell0@google.ru');
insert into `Deals Proposed`  values ('48-760-3928', '71-250-9114', '23-739-7547', 'Aloin Bettleson',		'Analysis', 		'1527243478', 'abettleson1@ning.com');
insert into `Deals Proposed`  values ('19-500-5029', '86-460-3372', '56-749-0064', 'Rutherford Lewinton', 	'Scouting', 		'0790555999', 'rlewinton2@dell.com');
insert into `Deals Proposed`  values ('84-576-4467', '86-202-5328', '34-940-3656', 'Chrotoem Spinley', 		'Assassination', 	'5701405370', 'cspinley3@yellowpages.com');
insert into `Deals Proposed`  values ('22-955-9158', '81-377-2356', '02-254-3961', 'Petra Cadore', 			'Cyber Security',	'5201382401', 'pcadore4@xing.com');
insert into `Deals Proposed`  values ('82-225-6120', '22-718-0421', '80-860-8003', 'Lorrie McTeer', 		'Scouting', 	 	'5925806751', 'lmcteer5@facebook.com');
insert into `Deals Proposed`  values ('13-511-7654', '64-316-3424', '88-625-5465', 'Faulkner Cowles', 		'Assassination', 	'4616671370', 'fcowles6@nasa.gov');
insert into `Deals Proposed`  values ('12-701-3472', '30-952-1766', '63-916-9347', 'Kahlil McCart', 		'Cyber Security', 	'3997256772', 'kmccart7@blogger.com');
insert into `Deals Proposed`  values ('11-512-4185', '09-226-1109', '49-082-6142', 'Yasmin Downage',		'Analysis', 		'1047683466', 'ydownage8@independent.co.uk');
insert into `Deals Proposed`  values ('62-035-2784', '14-806-9508', '41-583-5857', 'Westleigh Marushak', 	'Cyber Security', 	'1618245198', 'wmarushak9@weibo.com');
insert into `Deals Proposed`  values ('96-249-0103', '42-775-8016', '82-016-4173', 'Armstrong Lillicrop', 	'Cyber Security', 	'0945204817', 'alillicropa@ucoz.com');
insert into `Deals Proposed`  values ('20-731-8644', '55-519-8409', '03-966-6665', 'Bobbe Raffon',			'Analysis', 		'6251878169', 'braffonb@hao123.com');
insert into `Deals Proposed`  values ('85-634-6855', '81-558-7012', '65-871-0931', 'Christoforo Bute', 		'Analysis', 		'2169213031', 'cbutec@twitpic.com');
insert into `Deals Proposed`  values ('14-191-7062', '58-529-1644', '54-067-1967', 'Daven Queenborough', 	'Analysis', 		'0938690035', 'dqueenboroughd@weather.com');
insert into `Deals Proposed`  values ('76-357-9306', '86-593-6361', '65-911-4009', 'Yul Tommis', 			'Scouting', 		'8874106157', 'ytommise@usda.gov');
insert into `Deals Proposed`  values ('73-610-8510', '00-739-6574', '01-470-7364', 'Darya Posse', 			'Analysis', 		'3009324065', 'dpossef@shareasale.com');
insert into `Deals Proposed`  values ('87-841-5877', '61-601-9835', '49-835-1434', 'Norry Penlington', 		'Scouting', 		'5695723868', 'npenlingtong@aol.com');
insert into `Deals Proposed`  values ('66-794-0989', '60-591-1769', '79-260-1161', 'Nikolas Spuner', 		'Analysis', 		'1746140682', 'nspunerh@sfgate.com');
insert into `Deals Proposed`  values ('14-527-0914', '63-527-5397', '56-948-6708', 'Hashim Keeltagh', 		'Scouting', 		'2871426511', 'hkeeltaghi@webmd.com');
insert into `Deals Proposed`  values ('94-776-2317', '56-896-2706', '40-834-9661', 'Ravid Bolstridge', 		'Cyber Security', 	'5580385420', 'rbolstridgej@opensource.org');
