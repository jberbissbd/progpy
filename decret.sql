BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "compcclau" (
	"contpcclau_ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"contpcclau_idcomp"	INTEGER,
	"contpcclau_idcclau"	INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS "curs" (
	"curs_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"curs_etapa"	INTEGER,
	"curs_desc"	INTEGER,
	FOREIGN KEY("curs_etapa") REFERENCES "etapa"("etapa_id")
);
CREATE TABLE IF NOT EXISTS "etapa" (
	"etapa_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"etapa_desc"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "dimensio" (
	"dim_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"dim_ambit"	INTEGER,
	"dim_desc"	TEXT
);
CREATE TABLE IF NOT EXISTS "cclau" (
	"cclau_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"cclau_ord"	INTEGER,
	"cclau_desc"	TEXT,
	"cclau_ambit"	INTEGER,
	"cclau_pref"	TEXT,
	"cclau_num"	INTEGER
);
CREATE TABLE IF NOT EXISTS "competencia" (
	"comp_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"comp_desc"	TEXT,
	"comp_num"	INTEGER,
	"comp_dim"	NUMERIC,
	"comp_ambit"	INTEGER
);
CREATE TABLE IF NOT EXISTS "ambit" (
	"ambit_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"ambit_desc"	TEXT
);
INSERT INTO "compcclau" VALUES (1,12,3);
INSERT INTO "compcclau" VALUES (2,13,3);
INSERT INTO "compcclau" VALUES (3,14,6);
INSERT INTO "compcclau" VALUES (4,15,6);
INSERT INTO "compcclau" VALUES (5,16,6);
INSERT INTO "compcclau" VALUES (8,19,24);
INSERT INTO "compcclau" VALUES (9,20,25);
INSERT INTO "compcclau" VALUES (10,21,25);
INSERT INTO "compcclau" VALUES (12,22,25);
INSERT INTO "compcclau" VALUES (13,2,6);
INSERT INTO "compcclau" VALUES (15,6,6);
INSERT INTO "compcclau" VALUES (16,7,6);
INSERT INTO "compcclau" VALUES (17,8,6);
INSERT INTO "compcclau" VALUES (18,9,6);
INSERT INTO "compcclau" VALUES (20,4,6);
INSERT INTO "compcclau" VALUES (21,5,6);
INSERT INTO "compcclau" VALUES (22,10,6);
INSERT INTO "compcclau" VALUES (23,10,6);
INSERT INTO "compcclau" VALUES (24,23,25);
INSERT INTO "compcclau" VALUES (25,24,25);
INSERT INTO "compcclau" VALUES (26,25,25);
INSERT INTO "compcclau" VALUES (27,26,25);
INSERT INTO "compcclau" VALUES (28,27,25);
INSERT INTO "compcclau" VALUES (29,29,33);
INSERT INTO "compcclau" VALUES (30,30,33);
INSERT INTO "compcclau" VALUES (31,31,33);
INSERT INTO "compcclau" VALUES (32,33,26);
INSERT INTO "compcclau" VALUES (33,35,26);
INSERT INTO "compcclau" VALUES (34,36,26);
INSERT INTO "compcclau" VALUES (36,39,24);
INSERT INTO "compcclau" VALUES (37,40,26);
INSERT INTO "compcclau" VALUES (38,41,29);
INSERT INTO "compcclau" VALUES (39,42,29);
INSERT INTO "compcclau" VALUES (40,43,1);
INSERT INTO "compcclau" VALUES (41,44,3);
INSERT INTO "compcclau" VALUES (42,45,9);
INSERT INTO "compcclau" VALUES (43,46,3);
INSERT INTO "compcclau" VALUES (44,47,24);
INSERT INTO "compcclau" VALUES (45,48,24);
INSERT INTO "compcclau" VALUES (46,48,62);
INSERT INTO "compcclau" VALUES (47,49,62);
INSERT INTO "compcclau" VALUES (48,49,1);
INSERT INTO "compcclau" VALUES (49,51,24);
INSERT INTO "compcclau" VALUES (50,52,24);
INSERT INTO "compcclau" VALUES (51,54,26);
INSERT INTO "compcclau" VALUES (52,55,27);
INSERT INTO "compcclau" VALUES (53,56,27);
INSERT INTO "compcclau" VALUES (54,58,27);
INSERT INTO "compcclau" VALUES (55,59,27);
INSERT INTO "compcclau" VALUES (56,60,27);
INSERT INTO "compcclau" VALUES (57,61,27);
INSERT INTO "compcclau" VALUES (58,63,2);
INSERT INTO "compcclau" VALUES (59,64,26);
INSERT INTO "compcclau" VALUES (60,65,33);
INSERT INTO "compcclau" VALUES (61,34,26);
INSERT INTO "compcclau" VALUES (62,50,1);
INSERT INTO "compcclau" VALUES (63,57,26);
INSERT INTO "compcclau" VALUES (65,62,27);
INSERT INTO "compcclau" VALUES (68,39,55);
INSERT INTO "compcclau" VALUES (69,34,60);
INSERT INTO "compcclau" VALUES (71,73,60);
INSERT INTO "compcclau" VALUES (72,35,55);
INSERT INTO "compcclau" VALUES (75,56,55);
INSERT INTO "compcclau" VALUES (76,23,94);
INSERT INTO "compcclau" VALUES (77,26,94);
INSERT INTO "compcclau" VALUES (78,32,33);
INSERT INTO "compcclau" VALUES (79,63,94);
INSERT INTO "compcclau" VALUES (80,64,94);
INSERT INTO "compcclau" VALUES (81,75,60);
INSERT INTO "compcclau" VALUES (83,74,86);
INSERT INTO "compcclau" VALUES (86,16,55);
INSERT INTO "compcclau" VALUES (88,19,92);
INSERT INTO "compcclau" VALUES (89,76,55);
INSERT INTO "compcclau" VALUES (90,76,60);
INSERT INTO "compcclau" VALUES (91,11,6);
INSERT INTO "compcclau" VALUES (92,24,4);
INSERT INTO "compcclau" VALUES (93,25,4);
INSERT INTO "compcclau" VALUES (95,28,25);
INSERT INTO "compcclau" VALUES (96,29,94);
INSERT INTO "compcclau" VALUES (97,30,94);
INSERT INTO "compcclau" VALUES (98,31,94);
INSERT INTO "compcclau" VALUES (99,32,94);
INSERT INTO "compcclau" VALUES (100,28,60);
INSERT INTO "compcclau" VALUES (101,27,94);
INSERT INTO "compcclau" VALUES (102,66,26);
INSERT INTO "compcclau" VALUES (103,66,60);
INSERT INTO "compcclau" VALUES (105,67,26);
INSERT INTO "compcclau" VALUES (106,68,32);
INSERT INTO "compcclau" VALUES (107,69,32);
INSERT INTO "compcclau" VALUES (108,70,26);
INSERT INTO "compcclau" VALUES (109,71,33);
INSERT INTO "compcclau" VALUES (110,72,33);
INSERT INTO "compcclau" VALUES (111,56,26);
INSERT INTO "compcclau" VALUES (112,75,94);
INSERT INTO "compcclau" VALUES (113,77,56);
INSERT INTO "compcclau" VALUES (114,78,92);
INSERT INTO "compcclau" VALUES (115,79,94);
INSERT INTO "compcclau" VALUES (116,80,60);
INSERT INTO "compcclau" VALUES (118,37,26);
INSERT INTO "curs" VALUES (1,1,'1er ESO');
INSERT INTO "curs" VALUES (2,1,'2n ESO');
INSERT INTO "curs" VALUES (3,1,'3er ESO');
INSERT INTO "curs" VALUES (4,1,'4t ESO
');
INSERT INTO "curs" VALUES (5,2,'1er Batxillerat');
INSERT INTO "curs" VALUES (6,2,'2n Batxillerat');
INSERT INTO "etapa" VALUES (1,'ESO');
INSERT INTO "etapa" VALUES (2,'Batxillerat');
INSERT INTO "dimensio" VALUES (1,1,'Històrica');
INSERT INTO "dimensio" VALUES (2,1,'Geogràfica');
INSERT INTO "dimensio" VALUES (3,1,'Cultural i artística');
INSERT INTO "dimensio" VALUES (4,1,'Ciutadana');
INSERT INTO "dimensio" VALUES (5,2,'Resolució de problemes');
INSERT INTO "dimensio" VALUES (6,2,'Raonament i prova');
INSERT INTO "dimensio" VALUES (7,2,'Connexions');
INSERT INTO "dimensio" VALUES (8,2,'Comunicació i representació');
INSERT INTO "dimensio" VALUES (9,8,'Instruments i aplicacions');
INSERT INTO "dimensio" VALUES (10,8,'Tractament de la informació i organització dels entorns de treball i aprenentatge');
INSERT INTO "dimensio" VALUES (11,8,'Comunicació interpersonal i col·laboració');
INSERT INTO "dimensio" VALUES (12,8,'Ciutadania, hàbits,civisme i identitat digital');
INSERT INTO "dimensio" VALUES (13,9,'Autoconeixement');
INSERT INTO "dimensio" VALUES (14,9,'Aprendre a aprendre');
INSERT INTO "dimensio" VALUES (15,9,'Participació');
INSERT INTO "cclau" VALUES (1,1,'Textos de les ciències socials: descripció, explicació,  justificació, interpretació i argumentació, i vocabulari  propi.',1,'CC',1);
INSERT INTO "cclau" VALUES (2,2,'Estratègies comunicatives en situacions d’interacció oral.',1,'CC',2);
INSERT INTO "cclau" VALUES (3,3,'Cronologia i temps històric.',1,'CC',3);
INSERT INTO "cclau" VALUES (4,4,'Coneixements històrics temporals.',1,'CC',4);
INSERT INTO "cclau" VALUES (5,5,'Fonts primàries i secundàries.',1,'CC',5);
INSERT INTO "cclau" VALUES (6,6,'Vincles entre el passat, el present i el futur. L’empatia històrica.',1,'CC',6);
INSERT INTO "cclau" VALUES (7,7,'La memòria històrica.',1,'CC',7);
INSERT INTO "cclau" VALUES (8,8,'Elements de canvi i continuïtat entre etapes històriques. Arrels històriques de la contemporaneïtat.',1,'CC',8);
INSERT INTO "cclau" VALUES (9,9,'El passat i el present de Catalunya en el context d’Espanya i d’Europa.',1,'CC',9);
INSERT INTO "cclau" VALUES (10,10,'Models d’interpretació geogràfics i de fets històrics.',1,'CC',10);
INSERT INTO "cclau" VALUES (11,11,'Les dones en la història i en les societats actuals.',1,'CC',11);
INSERT INTO "cclau" VALUES (12,12,'Les manifestacions artístiques en el seu context històric. Valoració estètica. Estils i llenguatges expressius.',1,'CC',12);
INSERT INTO "cclau" VALUES (13,13,'Anàlisi d’imatges i referents estètics. Descodificació de llenguatges icònics, simbòlics i audiovisuals.',1,'CC',13);
INSERT INTO "cclau" VALUES (14,14,'Defensa, protecció i difusió del patrimoni historicoartístic i cultural.',1,'CC',14);
INSERT INTO "cclau" VALUES (15,15,'Canvis, continuïtats i ruptures en el món de la cultura i l’art, i en les mentalitats.',1,'CC',15);
INSERT INTO "cclau" VALUES (16,16,'La diversitat cultural i religiosa com a riquesa de les societats. Relativisme cultural.',1,'CC',16);
INSERT INTO "cclau" VALUES (17,17,'Cerca, anàlisi i contrast d’informacions diverses.',1,'CC',17);
INSERT INTO "cclau" VALUES (18,18,'Lectura i interpretació de mapes, plànols i imatges de diferents característiques i suports. Eines d’orientació espacial.',1,'CC',18);
INSERT INTO "cclau" VALUES (19,19,'Interacció entre els grups humans i el medi. Activitats econòmiques i el seu impacte mediambiental. Matèries primeres i fonts d’energia.',1,'CC',19);
INSERT INTO "cclau" VALUES (20,20,'Principals zones bioclimàtiques de Catalunya, Espanya, Europa i el món. Defensa i preservació del patrimoni paisatgístic.',1,'CC',20);
INSERT INTO "cclau" VALUES (21,21,'Trets demogràfics, econòmics, socials, polítics i culturals de la societat catalana, espanyola, europea i del món. Població i  poblament. Migracions.',1,'CC',21);
INSERT INTO "cclau" VALUES (22,22,'Els grans àmbits geopolítics i econòmics. Models econòmics.',1,'CC',22);
INSERT INTO "cclau" VALUES (23,23,'Organització política i territorial: àmbits local, nacional i internacional.',1,'CC',23);
INSERT INTO "cclau" VALUES (24,24,'Globalització i intercanvi desigual. Mecanismes de cooperació internacional.',1,'CC',24);
INSERT INTO "cclau" VALUES (25,25,'Desenvolupament humà sostenible.',1,'CC',25);
INSERT INTO "cclau" VALUES (26,26,'Funcionament del sistema democràtic.',1,'CC',26);
INSERT INTO "cclau" VALUES (27,27,'Drets humans.',1,'CC',27);
INSERT INTO "cclau" VALUES (28,28,'Situacions de desigualtat, injustícia i discriminació.',1,'CC',28);
INSERT INTO "cclau" VALUES (29,29,'Focus de conflicte en el món actual.',1,'CC',29);
INSERT INTO "cclau" VALUES (30,30,'Identitats personals i col·lectives. Pertinença i cohesió social.',1,'CC',30);
INSERT INTO "cclau" VALUES (31,1,'Sentit del nombre i de les operacions.',2,'CC',1);
INSERT INTO "cclau" VALUES (32,2,'Raonament proporcional.',2,'CC',2);
INSERT INTO "cclau" VALUES (33,3,'Càlcul (mental, estimatiu, algorísmic, amb calculadora).',2,'CC',3);
INSERT INTO "cclau" VALUES (34,4,'Llenguatge i càlcul algebraic.',2,'CC',4);
INSERT INTO "cclau" VALUES (35,5,'Patrons, relacions i funcions.',2,'CC',5);
INSERT INTO "cclau" VALUES (36,6,'Representació de funcions: gràfics, taules i fórmules.',2,'CC',6);
INSERT INTO "cclau" VALUES (37,7,'Anàlisi del canvi i tipus de funcions.',2,'CC',7);
INSERT INTO "cclau" VALUES (38,8,'Sentit espacial i representació de figures tridimensionals.',2,'CC',8);
INSERT INTO "cclau" VALUES (39,9,'Figures geomètriques, característiques, propietats i processos de construcció.',2,'CC',9);
INSERT INTO "cclau" VALUES (40,10,'Relacions i transformacions geomètriques.',2,'CC',10);
INSERT INTO "cclau" VALUES (41,11,'Magnituds i mesura.',2,'CC',11);
INSERT INTO "cclau" VALUES (42,12,'Relacions mètriques i càlcul de mesures en figures.',2,'CC',12);
INSERT INTO "cclau" VALUES (43,13,'Sentit de l’estadística.',2,'CC',13);
INSERT INTO "cclau" VALUES (44,14,'Dades, taules i gràfics estadístics.',2,'CC',14);
INSERT INTO "cclau" VALUES (45,15,'Mètodes estadístics d’anàlisi de dades.',2,'CC',15);
INSERT INTO "cclau" VALUES (46,16,'Sentit i mesura de la probabilitat.',2,'CC',16);
INSERT INTO "cclau" VALUES (47,1,'Funcionalitats bàsiques dels dispositius.',8,'CCD',1);
INSERT INTO "cclau" VALUES (48,2,'Tipus de connexions entre aparells.',8,'CCD',2);
INSERT INTO "cclau" VALUES (49,3,'Emmagatzematge de dades i còpies de seguretat.',8,'CCD',3);
INSERT INTO "cclau" VALUES (50,4,'Conceptes bàsics del sistema operatiu.',8,'CCD',4);
INSERT INTO "cclau" VALUES (51,5,'Seguretat informàtica.',8,'CCD',5);
INSERT INTO "cclau" VALUES (52,6,'Robòtica i programació.',8,'CCD',6);
INSERT INTO "cclau" VALUES (53,7,'Realitat virtual i augmentada.',8,'CCD',7);
INSERT INTO "cclau" VALUES (54,8,'Sistemes de projecció.',8,'CCD',8);
INSERT INTO "cclau" VALUES (55,9,'Eines d’edició de documents de text, presentacions multimèdia i processament de dades numèriques.',8,'CCD',9);
INSERT INTO "cclau" VALUES (56,10,'Llenguatge audiovisual: imatge fixa, so i vídeo.',8,'CCD',10);
INSERT INTO "cclau" VALUES (57,11,'Funcionalitats dels navegadors.',8,'CCD',11);
INSERT INTO "cclau" VALUES (58,12,'Cercadors: tipus de cerca i planificació.',8,'CCD',12);
INSERT INTO "cclau" VALUES (59,13,'Fonts d’informació digital: selecció i valoració.',8,'CCD',13);
INSERT INTO "cclau" VALUES (60,14,'Selecció, catalogació, emmagatzematge i compartició de la informació.',8,'CCD',14);
INSERT INTO "cclau" VALUES (61,15,'Ètica i legalitat en l’ús i instal·lació de programes, comunicacions i publicacions, i en la utilització de la informació.',8,'CCD',15);
INSERT INTO "cclau" VALUES (62,16,'Tractament de la informació.',8,'CCD',16);
INSERT INTO "cclau" VALUES (63,17,'Construcció de coneixement: tècniques i instruments.',8,'CCD',17);
INSERT INTO "cclau" VALUES (64,18,'Entorn personal d’aprenentatge (EPA).',8,'CCD',18);
INSERT INTO "cclau" VALUES (65,19,'Dossiers personals d’aprenentatge (portafolis digital).',8,'CCD',19);
INSERT INTO "cclau" VALUES (66,20,'Sistemes de comunicació.',8,'CCD',20);
INSERT INTO "cclau" VALUES (67,21,'Normes de cortesia a la xarxa.',8,'CCD',21);
INSERT INTO "cclau" VALUES (68,22,'Entorns de treball i aprenentatge col·laboratiu.',8,'CCD',22);
INSERT INTO "cclau" VALUES (69,23,'Ciutadania digital: tràmits, gestió, lleure i cultura.',8,'CCD',23);
INSERT INTO "cclau" VALUES (70,24,'Aprenentatge permanent: entorns virtuals d’aprenentatge, recursos per a l’aprenentatge formal i no formal a la xarxa...',8,'CCD',24);
INSERT INTO "cclau" VALUES (71,25,'Ergonomia: salut física i psíquica.',8,'CCD',25);
INSERT INTO "cclau" VALUES (72,26,'Entorns virtuals segurs.',8,'CCD',26);
INSERT INTO "cclau" VALUES (73,27,'Sostenibilitat: consum d’energia, despesa d’impressió, mesures d’estalvi, substitució de dispositius, etc.',8,'CCD',27);
INSERT INTO "cclau" VALUES (74,28,'Identitat digital: visibilitat, reputació, gestió de la privacitat pública i aliena.',8,'CCD',28);
INSERT INTO "cclau" VALUES (82,1,'Capacitats físiques i sensorials.',9,'CC',1);
INSERT INTO "cclau" VALUES (83,2,'Capacitats cognitives.',9,'CC',2);
INSERT INTO "cclau" VALUES (84,3,'Capacitats emocionals.',9,'CC',3);
INSERT INTO "cclau" VALUES (85,4,'Hàbits saludables.',9,'CC',4);
INSERT INTO "cclau" VALUES (86,5,'Actitud de superació personal.',9,'CC',5);
INSERT INTO "cclau" VALUES (87,6,'Hàbits d’aprenentatge.',9,'CC',6);
INSERT INTO "cclau" VALUES (88,7,'Planificació dels aprenentatges.',9,'CC',7);
INSERT INTO "cclau" VALUES (89,8,'Organització del coneixement.',9,'CC',8);
INSERT INTO "cclau" VALUES (90,9,'Consolidació i recuperació del coneixement.',9,'CC',9);
INSERT INTO "cclau" VALUES (91,10,'Transferència dels aprenentatges.',9,'CC',10);
INSERT INTO "cclau" VALUES (92,11,'Característiques de la societat actual.',9,'CC',11);
INSERT INTO "cclau" VALUES (93,12,'Aprenentatge continuat al llarg de la vida.',9,'CC',12);
INSERT INTO "cclau" VALUES (94,13,'Actituds i hàbits en la societat i en el món professional.',9,'CC',13);
INSERT INTO "cclau" VALUES (95,14,'Habilitats i actituds per al treball en grup.',9,'CC',14);
INSERT INTO "cclau" VALUES (96,15,'Dinàmiques de cohesió de grup i col·laboratives.',9,'CC',15);
INSERT INTO "cclau" VALUES (97,16,'Eines digitals col·laboratives.',9,'CC',16);
INSERT INTO "cclau" VALUES (98,17,'Habilitats i actituds per a la participació.',9,'CC',17);
INSERT INTO "cclau" VALUES (99,18,'Espais de participació.',9,'CC',18);
INSERT INTO "cclau" VALUES (100,19,'Recursos i tècniques de participació.',9,'CC',19);
INSERT INTO "cclau" VALUES (101,20,'Eines digitals de participació.',9,'CC',20);
INSERT INTO "competencia" VALUES (2,'Analitzar els canvis i les continuïtats dels fets o fenòmens històrics per comprendre’n la causalitat històrica.',1,1,1);
INSERT INTO "competencia" VALUES (3,'Aplicar els procediments de la recerca històrica a partir de la formulació de preguntes i l’anàlisi de fonts, per interpretar el passat',2,1,1);
INSERT INTO "competencia" VALUES (4,'Interpretar que el present és producte del passat, per comprendre que el futur és fruit de les decisions i accions actuals.',3,1,1);
INSERT INTO "competencia" VALUES (5,'Identificar i valorar la identitat individual i col·lectiva per comprendre la seva intervenció en la construcció de subjectes històrics',4,1,1);
INSERT INTO "competencia" VALUES (6,'Explicar les interrelacions entre els elements del’espai geogràfic, per gestionar les activitats humanes en el territori amb criteris de sostenibilitat.',5,2,1);
INSERT INTO "competencia" VALUES (7,'Aplicar els procediments de l’anàlisi geogràfica apartir de la cerca i l’anàlisi de diverses fonts, per interpretar l’espaii prendre decisions.',6,2,1);
INSERT INTO "competencia" VALUES (8,'Analitzar diferents models d’organització política, econòmica i territorial, i les desigualtats que generen, per valorar com afecten la vida de les persones i fer propostes d’actuació.',7,2,1);
INSERT INTO "competencia" VALUES (9,'Analitzar les manifestacions culturals i relacionar-les amb els seus creadors i la seva època, per interpretar les diverses cosmovisions i la seva finalitat.',8,3,1);
INSERT INTO "competencia" VALUES (10,'Valorar el patrimoni cultural com a herència rebuda del passat, per defensar-ne la conservació i afavorir que les generacions futures se l’apropiïn.',9,3,1);
INSERT INTO "competencia" VALUES (11,'Valorar les expressions culturals pròpies, per afavorir la construcció de la identitat personal dins d’un món global i divers.',10,3,1);
INSERT INTO "competencia" VALUES (12,'Formar-se un criteri propi sobre problemes socials rellevants per desenvolupar un pensament crític.',11,4,1);
INSERT INTO "competencia" VALUES (13,'Participar activament i de manera compromesa en projectes per exercir drets, deures i responsabilitats propis d’una societat democràtica.',12,4,1);
INSERT INTO "competencia" VALUES (14,'Pronunciar-se i comprometre’s en la defensa de la justícia, la llibertat i la igualtat entre homes i dones.',13,4,1);
INSERT INTO "competencia" VALUES (15,'Traduir un problema a llenguatge matemàtic o a una representació matemàtica utilitzant variables, símbols, diagrames imodels adequats.',1,5,2);
INSERT INTO "competencia" VALUES (16,'Emprar conceptes, eines i estratègies matemàtiques per resoldre problemes.',2,5,2);
INSERT INTO "competencia" VALUES (17,'Mantenir una actitud de recerca davant d’un problema assajant estratègies diverses.',3,5,2);
INSERT INTO "competencia" VALUES (18,'Generar preguntes de caire matemàtic i plantejar problemes.',4,5,2);
INSERT INTO "competencia" VALUES (19,'Construir, expressar i contrastar argumentacions per justificar i validar les afirmacions que es fan en matemàtiques.',5,6,2);
INSERT INTO "competencia" VALUES (20,'Emprar el raonament matemàtic en entorns no ma-temàtics.',6,6,2);
INSERT INTO "competencia" VALUES (21,'Usar les relacions que hi ha entre les diverses parts de les matemàtiques per analitzar situacions i per raonar.',7,7,2);
INSERT INTO "competencia" VALUES (22,'Identificar les matemàtiques implicades en situacions properes i acadèmiques i cercar situacions que es puguin relacionaramb idees matemàtiques concretes.',8,7,2);
INSERT INTO "competencia" VALUES (23,'Representar un concepte o relació matemàtica de diverses maneres i usar el canvi de representació com a estratègia de treball matemàtic.',9,8,2);
INSERT INTO "competencia" VALUES (24,'Expressar idees matemàtiques amb claredat i precisió i comprendre les dels altres.',10,8,2);
INSERT INTO "competencia" VALUES (25,'Emprar la comunicació i el treball col·laboratiu per compartir i construir coneixement a partir d’idees matemàtiques.',11,8,2);
INSERT INTO "competencia" VALUES (26,'Seleccionar i usar tecnologies diverses per gestionar i mostrar informació, i visualitzar i estructurar idees o processos matemàtics.',12,8,2);
INSERT INTO "competencia" VALUES (27,'Seleccionar, configurar i programar dispositius digitals segons les tasques a realitzar.',1,9,8);
INSERT INTO "competencia" VALUES (28,'Utilitzar les aplicacions d’edició de textos, presentacions multimèdia i tractament de dades numèriques per a la producció de documents digitals.',2,9,8);
INSERT INTO "competencia" VALUES (29,'Utilitzar les aplicacions bàsiques d’edició d’imatge fixa, so i imatge en moviment per a produccions de documents digitals.',3,9,8);
INSERT INTO "competencia" VALUES (30,'Cercar, contrastar i seleccionar informació digital adequada per al treball a realitzar, tot considerant diverses fonts i mitjans digitals.',4,10,8);
INSERT INTO "competencia" VALUES (31,'Construir nou coneixement personal mitjançant estratègies de tractament de la informació amb el suport d’aplicacions digitals.',5,10,8);
INSERT INTO "competencia" VALUES (32,'Organitzar i utilitzar un entorn personal de treball i aprenentatge amb eines digitals per desenvolupar-se en la societat del coneixement.',6,10,8);
INSERT INTO "competencia" VALUES (33,'Participar en entorns de comunicació interpersonal i publicacions virtuals per compartir informació.',7,11,8);
INSERT INTO "competencia" VALUES (34,'Realitzar activitats en grup tot utilitzant eines i entorns virtuals de treball col·laboratiu.',8,11,8);
INSERT INTO "competencia" VALUES (35,'Realitzar accions de ciutadania i de desenvolupament personal, tot utilitzant els recursos digitals propis de la societat actual.',9,12,8);
INSERT INTO "competencia" VALUES (36,'Fomentar hàbits d’ús saludable de les TIC vinculats a l’ergonomia per a la prevenció de riscos.',10,12,8);
INSERT INTO "competencia" VALUES (37,'Actuar de forma crítica i responsable en l’ús de les TIC, tot considerant aspectes ètics, legals, de seguretat, de sostenibilitat i d’identitat digital.',11,12,8);
INSERT INTO "competencia" VALUES (38,'Prendre consciència d’un mateix i implicar-se en el procés de creixement personal',1,13,9);
INSERT INTO "competencia" VALUES (39,'Conèixer i posar en pràctica estratègies i hàbits que intervenen en el propi aprenentatge.',2,14,9);
INSERT INTO "competencia" VALUES (40,'Desenvolupar habilitats i actituds que permetin afrontar els reptes de l’aprenentatge al llarg de la vida',3,14,9);
INSERT INTO "competencia" VALUES (41,'Participar a l’aula, al centre i a l’entorn de manera reflexiva i responsable',4,15,9);
INSERT INTO "ambit" VALUES (1,'Social');
INSERT INTO "ambit" VALUES (2,'Matemàtic');
INSERT INTO "ambit" VALUES (3,'Lingüístic');
INSERT INTO "ambit" VALUES (4,'Cientificotecnològic');
INSERT INTO "ambit" VALUES (5,'Artístic');
INSERT INTO "ambit" VALUES (6,'Educació física');
INSERT INTO "ambit" VALUES (7,'Cultura i valors');
INSERT INTO "ambit" VALUES (8,'Digital');
INSERT INTO "ambit" VALUES (9,'Personal i Social');
COMMIT;
