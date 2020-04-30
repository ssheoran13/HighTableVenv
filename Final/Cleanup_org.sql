CREATE TABLE `db`.`Cleanup Org` (
  `Org ID` VARCHAR(45) NOT NULL,
  `Deal ID` VARCHAR(45) NOT NULL,
  `Target Areas` VARCHAR(45) NOT NULL,
  `Min Price` VARCHAR(45) NOT NULL,
  `Contact` VARCHAR(100) NOT NULL,
  FOREIGN KEY (`Deal ID`) REFERENCES Deals_Proposed(`Deal ID`),
  PRIMARY KEY (`Org ID`));


insert into `Cleanup Org` values ('12-218-8765',  '54-464-6842', 'Pak Chong', 			'8182922585', 'kpennings0@dion.ne.jp');
insert into `Cleanup Org`  values ('50-654-3241', '48-760-3928', 'Bonneuil-sur-Marne', 	'3482404143', 'wgioani1@columbia.edu');
insert into `Cleanup Org`  values ('67-274-0160', '19-500-5029', 'São Sebastião', 		'1206838302', 'faurelius2@rambler.ru');
insert into `Cleanup Org`  values ('60-556-5186', '84-576-4467', 'Västanfjärd', 		'6372358166', 'centissle3@zdnet.com');
insert into `Cleanup Org`  values ('82-589-1488', '22-955-9158', 'Kanganpur', 			'8044700234', 'gkimmerling4@gmpg.org');
insert into `Cleanup Org`  values ('87-008-6138', '82-225-6120', 'Svenljunga', 			'9848707778', 'lsweetland5@nps.gov');
insert into `Cleanup Org`  values ('73-173-4626', '13-511-7654', 'Trinidad', 			'3605037321', 'mcorneille6@trellian.com');
insert into `Cleanup Org`  values ('74-862-3442', '12-701-3472', 'Ħamrun', 				'7177214593', 'iferrea7@acquirethisname.com');
insert into `Cleanup Org`  values ('92-388-4264', '11-512-4185', 'Nampera', 			'7871860658', 'mposselwhite8@elpais.com');
insert into `Cleanup Org`  values ('72-572-4714', '62-035-2784', 'Thị Trấn Nho Quan', 	'7607434836', 'glippett9@tmall.com');
insert into `Cleanup Org`  values ('04-503-5551', '96-249-0103', 'Mas‘adah', 			'1949353222', 'jskellya@msn.com');
insert into `Cleanup Org`  values ('47-418-3775', '20-731-8644', 'Matadi', 				'4952509311', 'tcheyenneb@telegraph.co.uk');
insert into `Cleanup Org`  values ('05-192-2060', '85-634-6855', 'Główczyce', 			'0086942271', 'mcattoc@intel.com');
insert into `Cleanup Org`  values ('46-856-9213', '14-191-7062', 'Dalongdong', 			'7970459005', 'drouked@google.com.au');
insert into `Cleanup Org`  values ('25-965-9028', '76-357-9306', 'Santo Tomás', 		'5851142545', 'hjainee@csmonitor.com');
insert into `Cleanup Org`  values ('52-246-4607', '73-610-8510', 'Centre de Flacq', 	'6409999798', 'rhallamf@alibaba.com');
insert into `Cleanup Org`  values ('56-199-1267', '87-841-5877', 'Zhenyuan', 			'0285502220', 'jhenzleyg@tmall.com');
insert into `Cleanup Org`  values ('52-195-9977', '66-794-0989', 'Taphan Hin', 			'8591343131', 'ttenderh@ifeng.com');
insert into `Cleanup Org`  values ('51-357-1339', '14-527-0914', 'Ad Dujayl', 			'3900929807', 'ageilli@umn.edu');
insert into `Cleanup Org`  values ('79-800-7457', '94-776-2317', 'Lanas', 				'2454949679', 'fbehanj@cnbc.com');

