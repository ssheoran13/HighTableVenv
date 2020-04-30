CREATE TABLE `db`.`All_Hitmans` (
  `Hitman ID` VARCHAR(45) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Specialization` VARCHAR(45) NOT NULL,
  `Region` VARCHAR(45) NOT NULL,
  `BountyID` VARCHAR(45) NOT NULL,  
  `Contact` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Hitman ID`),
  FOREIGN KEY (`BountyID`) REFERENCES Hitman_Bounty(`Bounty ID`)
);

insert into All_Hitmans values ('33-922-8067', 'Travus Cartmel', 	'Assassination', 	'Iturama',			'34-303-8705', 'tcartmel0@japanpost.jp');
insert into All_Hitmans values ('85-636-4650', 'Ase Tassell',		'Assassination', 	'Buensuseso',		'12-284-3757', 'atassell1@jiathis.com');
insert into All_Hitmans values ('12-654-2290', 'Antin Beden', 		'Scouting', 		'Pingsha',			'34-990-3106', 'abeden2@tiny.cc');
insert into All_Hitmans values ('61-683-4883', 'Cobby Mully', 		'Scouting', 		'Junkou',			'58-013-6149', 'cmully3@utexas.edu');
insert into All_Hitmans values ('12-861-6705', 'Reggi Wasteney', 	'Assassination', 	'Bojongbenteng',	'76-302-8218', 'rwasteney4@mediafire.com');
insert into All_Hitmans values ('64-632-3547', 'Brewer Giacomello', 'Scouting', 		'Kuala Terengganu',	'08-901-7681', 'bgiacomello5@ifeng.com');
insert into All_Hitmans values ('32-415-8012', 'Jeanie Spikins',	'Cyber Security', 	'Nunguan',			'11-934-6594', 'jspikins6@cam.ac.uk');
insert into All_Hitmans values ('71-472-5689', 'Glyn Stenyng', 		'Assassination', 	'As Suwaydā’',		'63-609-5525', 'gstenyng7@va.gov');
insert into All_Hitmans values ('47-066-8753', 'Aeriel Larway', 	'Cyber Security', 	'Koran',			'35-649-0058', 'alarway8@army.mil');
insert into All_Hitmans values ('68-026-4569', 'Nadeen Megarrell', 	'Scouting', 		'Raksajaya',		'11-435-2825', 'nmegarrell9@imdb.com');
insert into All_Hitmans values ('63-476-2692', 'Carissa Keyes', 	'Analysis', 		'Baiyang',			'13-134-0768', 'ckeyesa@cbslocal.com');
insert into All_Hitmans values ('49-014-1696', 'Wini Frede', 	   	'Assassination', 	'Al Farwānīyah',	'34-953-7691', 'wfredeb@sphinn.com');
insert into All_Hitmans values ('53-013-5429', 'Loria Waterhouse', 	'Analysis', 		'Tonghae',			'57-027-9627', 'lwaterhousec@goodreads.com');
insert into All_Hitmans values ('47-826-2333', 'Caron Angeau', 		'Cyber Security', 	'Fonadhoo',			'93-000-4741', 'cangeaud@soup.io');
insert into All_Hitmans values ('58-368-1243', 'Artie Dundon', 		'Assassination', 	'Staraya Kupavna',	'31-913-1524', 'adundone@home.pl');
insert into All_Hitmans values ('66-477-7464', 'Alys Rostern', 		'Scouting', 		'Kerva',			'85-505-7466', 'arosternf@desdev.cn');
insert into All_Hitmans values ('45-412-2997', 'Wash Benedict', 	'Assassination', 	'Jiangxigou',		'93-562-2986', 'wbenedictg@plala.or.jp');
insert into All_Hitmans values ('24-157-3309', 'Lilli Merrett', 	'Analysis', 		'Shijie',			'76-166-7722', 'lmerretth@vk.com');
insert into All_Hitmans values ('14-214-1566', 'Osborne Tongue', 	'Assassination', 	'Zwolle',			'24-321-4492', 'otonguei@shutterfly.com');
insert into All_Hitmans values ('68-614-3131', 'Sheilah Rothera', 	'Analysis', 		'Ube',				'16-366-2374', 'srotheraj@sciencedirect.com');
