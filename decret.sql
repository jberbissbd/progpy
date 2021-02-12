BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "competencies" (
	"ID_compt"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"comp_desc"	TEXT,
	"comp_num"	INTEGER,
	"comp_dim"	NUMERIC,
	"comp_ambit"	INTEGER
);
CREATE TABLE IF NOT EXISTS "dimensions" (
	"ID_dim"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"dim_ambit"	INTEGER,
	"dim_desc"	TEXT
);
CREATE TABLE IF NOT EXISTS "ambit" (
	"ID_ambitcomp"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"ambit_desc"	TEXT
);
CREATE TABLE IF NOT EXISTS "continguts_clau" (
	"ID_cclau"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"cclau_ord"	INTEGER,
	"cclau_desc"	TEXT,
	"cclau_ambit"	INTEGER,
	"cclau_pref"	TEXT,
	"cclau_num"	INTEGER
);
INSERT INTO "competencies" VALUES (2,'Analitzar els canvis i les continuïtats dels fets o fenòmens històrics per comprendre’n la causalitat històrica.',1,1,1);
INSERT INTO "competencies" VALUES (3,'Aplicar els procediments de la recerca històrica a partir de la formulació de preguntes i l’anàlisi de fonts, per interpretar el passat',2,1,1);
INSERT INTO "competencies" VALUES (4,'Interpretar que el present és producte del passat, per comprendre que el futur és fruit de les decisions i accions actuals.',3,1,1);
INSERT INTO "competencies" VALUES (5,'Identificar i valorar la identitat individual i col·lectiva per comprendre la seva intervenció en la construcció de subjectes històrics',4,1,1);
INSERT INTO "competencies" VALUES (6,'Explicar les interrelacions entre els elements del’espai geogràfic, per gestionar les activitats humanes en el territori amb criteris de sostenibilitat.',5,2,1);
INSERT INTO "competencies" VALUES (7,'Aplicar els procediments de l’anàlisi geogràfica apartir de la cerca i l’anàlisi de diverses fonts, per interpretar l’espaii prendre decisions.',6,2,1);
INSERT INTO "competencies" VALUES (8,'Analitzar diferents models d’organització política, econòmica i territorial, i les desigualtats que generen, per valorar com afecten la vida de les persones i fer propostes d’actuació.',7,2,1);
INSERT INTO "competencies" VALUES (9,'Analitzar les manifestacions culturals i relacionar-les amb els seus creadors i la seva època, per interpretar les diverses cosmovisions i la seva finalitat.',8,3,1);
INSERT INTO "competencies" VALUES (10,'Valorar el patrimoni cultural com a herència rebuda del passat, per defensar-ne la conservació i afavorir que les generacions futures se l’apropiïn.',9,3,1);
INSERT INTO "competencies" VALUES (11,'Valorar les expressions culturals pròpies, per afavorir la construcció de la identitat personal dins d’un món global i divers.',10,3,1);
INSERT INTO "competencies" VALUES (12,'Formar-se un criteri propi sobre problemes socials rellevants per desenvolupar un pensament crític.',11,4,1);
INSERT INTO "competencies" VALUES (13,'Participar activament i de manera compromesa en projectes per exercir drets, deures i responsabilitats propis d’una societat democràtica.',12,4,1);
INSERT INTO "competencies" VALUES (14,'Pronunciar-se i comprometre’s en la defensa de la justícia, la llibertat i la igualtat entre homes i dones.',13,4,1);
INSERT INTO "competencies" VALUES (15,'Traduir un problema a llenguatge matemàtic o a una representació matemàtica utilitzant variables, símbols, diagrames imodels adequats.',1,5,2);
INSERT INTO "competencies" VALUES (16,'Emprar conceptes, eines i estratègies matemàtiques per resoldre problemes.',2,5,2);
INSERT INTO "competencies" VALUES (17,'Mantenir una actitud de recerca davant d’un problema assajant estratègies diverses.',3,5,2);
INSERT INTO "competencies" VALUES (18,'Generar preguntes de caire matemàtic i plantejar problemes.',4,5,2);
INSERT INTO "competencies" VALUES (19,'Construir, expressar i contrastar argumentacions per justificar i validar les afirmacions que es fan en matemàtiques.',5,6,2);
INSERT INTO "competencies" VALUES (20,'Emprar el raonament matemàtic en entorns no ma-temàtics.',6,6,2);
INSERT INTO "competencies" VALUES (21,'Usar les relacions que hi ha entre les diverses parts de les matemàtiques per analitzar situacions i per raonar.',7,7,2);
INSERT INTO "competencies" VALUES (22,'Identificar les matemàtiques implicades en situacions properes i acadèmiques i cercar situacions que es puguin relacionaramb idees matemàtiques concretes.',8,7,2);
INSERT INTO "competencies" VALUES (23,'Representar un concepte o relació matemàtica de diverses maneres i usar el canvi de representació com a estratègia de treball matemàtic.',9,8,2);
INSERT INTO "competencies" VALUES (24,'Expressar idees matemàtiques amb claredat i precisió i comprendre les dels altres.',10,8,2);
INSERT INTO "competencies" VALUES (25,'Emprar la comunicació i el treball col·laboratiu per compartir i construir coneixement a partir d’idees matemàtiques.',11,8,2);
INSERT INTO "competencies" VALUES (26,'Seleccionar i usar tecnologies diverses per gestionar i mostrar informació, i visualitzar i estructurar idees o processos matemàtics.',12,8,2);
INSERT INTO "competencies" VALUES (27,'Seleccionar, configurar i programar dispositius digitals segons les tasques a realitzar.',1,9,8);
INSERT INTO "competencies" VALUES (28,'Utilitzar les aplicacions d’edició de textos, presentacions multimèdia i tractament de dades numèriques per a la producció de documents digitals.',2,9,8);
INSERT INTO "competencies" VALUES (29,'Utilitzar les aplicacions bàsiques d’edició d’imatge fixa, so i imatge en moviment per a produccions de documents digitals.',3,9,8);
INSERT INTO "competencies" VALUES (30,'Cercar, contrastar i seleccionar informació digital adequada per al treball a realitzar, tot considerant diverses fonts i mitjans digitals.',4,10,8);
INSERT INTO "competencies" VALUES (31,'Construir nou coneixement personal mitjançant estratègies de tractament de la informació amb el suport d’aplicacions digitals.',5,10,8);
INSERT INTO "competencies" VALUES (32,'Organitzar i utilitzar un entorn personal de treball i aprenentatge amb eines digitals per desenvolupar-se en la societat del coneixement.',6,10,8);
INSERT INTO "competencies" VALUES (33,'Participar en entorns de comunicació interpersonal i publicacions virtuals per compartir informació.',7,11,8);
INSERT INTO "competencies" VALUES (34,'Realitzar activitats en grup tot utilitzant eines i entorns virtuals de treball col·laboratiu.',8,11,8);
INSERT INTO "competencies" VALUES (35,'Realitzar accions de ciutadania i de desenvolupament personal, tot utilitzant els recursos digitals propis de la societat actual.',9,12,8);
INSERT INTO "competencies" VALUES (36,'Fomentar hàbits d’ús saludable de les TIC vinculats a l’ergonomia per a la prevenció de riscos.',10,12,8);
INSERT INTO "competencies" VALUES (37,'Actuar de forma crítica i responsable en l’ús de les TIC, tot considerant aspectes ètics, legals, de seguretat, de sostenibilitat i d’identitat digital.',11,12,8);
INSERT INTO "competencies" VALUES (38,'Prendre consciència d’un mateix i implicar-se en el procés de creixement personal',1,13,9);
INSERT INTO "competencies" VALUES (39,'Conèixer i posar en pràctica estratègies i hàbits que intervenen en el propi aprenentatge.',2,14,9);
INSERT INTO "competencies" VALUES (40,'Desenvolupar habilitats i actituds que permetin afrontar els reptes de l’aprenentatge al llarg de la vida',3,14,9);
INSERT INTO "competencies" VALUES (41,'Participar a l’aula, al centre i a l’entorn de manera reflexiva i responsable',4,15,9);
INSERT INTO "dimensions" VALUES (1,1,'Històrica');
INSERT INTO "dimensions" VALUES (2,1,'Geogràfica');
INSERT INTO "dimensions" VALUES (3,1,'Cultural i artística');
INSERT INTO "dimensions" VALUES (4,1,'Ciutadana');
INSERT INTO "dimensions" VALUES (5,2,'Resolució de problemes');
INSERT INTO "dimensions" VALUES (6,2,'Raonament i prova');
INSERT INTO "dimensions" VALUES (7,2,'Connexions');
INSERT INTO "dimensions" VALUES (8,2,'Comunicació i representació');
INSERT INTO "dimensions" VALUES (9,8,'Instruments i aplicacions');
INSERT INTO "dimensions" VALUES (10,8,'Tractament de la informació i organització dels entorns de treball i aprenentatge');
INSERT INTO "dimensions" VALUES (11,8,'Comunicació interpersonal i col·laboració');
INSERT INTO "dimensions" VALUES (12,8,'Ciutadania, hàbits,civisme i identitat digital');
INSERT INTO "dimensions" VALUES (13,9,'Autoconeixement');
INSERT INTO "dimensions" VALUES (14,9,'Aprendre a aprendre');
INSERT INTO "dimensions" VALUES (15,9,'Participació');
INSERT INTO "ambit" VALUES (1,'Social');
INSERT INTO "ambit" VALUES (2,'Matemàtic');
INSERT INTO "ambit" VALUES (3,'Lingüístic');
INSERT INTO "ambit" VALUES (4,'Cientificotecnològic');
INSERT INTO "ambit" VALUES (5,'Artístic');
INSERT INTO "ambit" VALUES (6,'Educació física');
INSERT INTO "ambit" VALUES (7,'Cultura i valors');
INSERT INTO "ambit" VALUES (8,'Digital');
INSERT INTO "ambit" VALUES (9,'Personal i Social');
INSERT INTO "continguts_clau" VALUES (1,1,'Textos de les ciències socials: descripció, explicació,  justificació, interpretació i argumentació, i vocabulari  propi.',1,'CC',1);
INSERT INTO "continguts_clau" VALUES (2,2,'Estratègies comunicatives en situacions d’interacció oral.',1,'CC',2);
INSERT INTO "continguts_clau" VALUES (3,3,'Cronologia i temps històric.',1,'CC',3);
INSERT INTO "continguts_clau" VALUES (4,4,'Coneixements històrics temporals.',1,'CC',4);
INSERT INTO "continguts_clau" VALUES (5,5,'Fonts primàries i secundàries.',1,'CC',5);
INSERT INTO "continguts_clau" VALUES (6,6,'Vincles entre el passat, el present i el futur. L’empatia històrica.',1,'CC',6);
INSERT INTO "continguts_clau" VALUES (7,7,'La memòria històrica.',1,'CC',7);
INSERT INTO "continguts_clau" VALUES (8,8,'Elements de canvi i continuïtat entre etapes històriques. Arrels històriques de la contemporaneïtat.',1,'CC',8);
INSERT INTO "continguts_clau" VALUES (9,9,'El passat i el present de Catalunya en el context d’Espanya i d’Europa.',1,'CC',9);
INSERT INTO "continguts_clau" VALUES (10,10,'Models d’interpretació geogràfics i de fets històrics.',1,'CC',10);
INSERT INTO "continguts_clau" VALUES (11,11,'Les dones en la història i en les societats actuals.',1,'CC',11);
INSERT INTO "continguts_clau" VALUES (12,12,'Les manifestacions artístiques en el seu context històric. Valoració estètica. Estils i llenguatges expressius.',1,'CC',12);
INSERT INTO "continguts_clau" VALUES (13,13,'Anàlisi d’imatges i referents estètics. Descodificació de llenguatges icònics, simbòlics i audiovisuals.',1,'CC',13);
INSERT INTO "continguts_clau" VALUES (14,14,'Defensa, protecció i difusió del patrimoni historicoartístic i cultural.',1,'CC',14);
INSERT INTO "continguts_clau" VALUES (15,15,'Canvis, continuïtats i ruptures en el món de la cultura i l’art, i en les mentalitats.',1,'CC',15);
INSERT INTO "continguts_clau" VALUES (16,16,'La diversitat cultural i religiosa com a riquesa de les societats. Relativisme cultural.',1,'CC',16);
INSERT INTO "continguts_clau" VALUES (17,17,'Cerca, anàlisi i contrast d’informacions diverses.',1,'CC',17);
INSERT INTO "continguts_clau" VALUES (18,18,'Lectura i interpretació de mapes, plànols i imatges de diferents característiques i suports. Eines d’orientació espacial.',1,'CC',18);
INSERT INTO "continguts_clau" VALUES (19,19,'Interacció entre els grups humans i el medi. Activitats econòmiques i el seu impacte mediambiental. Matèries primeres i fonts d’energia.',1,'CC',19);
INSERT INTO "continguts_clau" VALUES (20,20,'Principals zones bioclimàtiques de Catalunya, Espanya, Europa i el món. Defensa i preservació del patrimoni paisatgístic.',1,'CC',20);
INSERT INTO "continguts_clau" VALUES (21,21,'Trets demogràfics, econòmics, socials, polítics i culturals de la societat catalana, espanyola, europea i del món. Població i  poblament. Migracions.',1,'CC',21);
INSERT INTO "continguts_clau" VALUES (22,22,'Els grans àmbits geopolítics i econòmics. Models econòmics.',1,'CC',22);
INSERT INTO "continguts_clau" VALUES (23,23,'Organització política i territorial: àmbits local, nacional i internacional.',1,'CC',23);
INSERT INTO "continguts_clau" VALUES (24,24,'Globalització i intercanvi desigual. Mecanismes de cooperació internacional.',1,'CC',24);
INSERT INTO "continguts_clau" VALUES (25,25,'Desenvolupament humà sostenible.',1,'CC',25);
INSERT INTO "continguts_clau" VALUES (26,26,'Funcionament del sistema democràtic.',1,'CC',26);
INSERT INTO "continguts_clau" VALUES (27,27,'Drets humans.',1,'CC',27);
INSERT INTO "continguts_clau" VALUES (28,28,'Situacions de desigualtat, injustícia i discriminació.',1,'CC',28);
INSERT INTO "continguts_clau" VALUES (29,29,'Focus de conflicte en el món actual.',1,'CC',29);
INSERT INTO "continguts_clau" VALUES (30,30,'Identitats personals i col·lectives. Pertinença i cohesió social.',1,'CC',30);
INSERT INTO "continguts_clau" VALUES (31,1,'Sentit del nombre i de les operacions.',2,'CC',1);
INSERT INTO "continguts_clau" VALUES (32,2,'Raonament proporcional.',2,'CC',2);
INSERT INTO "continguts_clau" VALUES (33,3,'Càlcul (mental, estimatiu, algorísmic, amb calculadora).',2,'CC',3);
INSERT INTO "continguts_clau" VALUES (34,4,'Llenguatge i càlcul algebraic.',2,'CC',4);
INSERT INTO "continguts_clau" VALUES (35,5,'Patrons, relacions i funcions.',2,'CC',5);
INSERT INTO "continguts_clau" VALUES (36,6,'Representació de funcions: gràfics, taules i fórmules.',2,'CC',6);
INSERT INTO "continguts_clau" VALUES (37,7,'Anàlisi del canvi i tipus de funcions.',2,'CC',7);
INSERT INTO "continguts_clau" VALUES (38,8,'Sentit espacial i representació de figures tridimensionals.',2,'CC',8);
INSERT INTO "continguts_clau" VALUES (39,9,'Figures geomètriques, característiques, propietats i processos de construcció.',2,'CC',9);
INSERT INTO "continguts_clau" VALUES (40,10,'Relacions i transformacions geomètriques.',2,'CC',10);
INSERT INTO "continguts_clau" VALUES (41,11,'Magnituds i mesura.',2,'CC',11);
INSERT INTO "continguts_clau" VALUES (42,12,'Relacions mètriques i càlcul de mesures en figures.',2,'CC',12);
INSERT INTO "continguts_clau" VALUES (43,13,'Sentit de l’estadística.',2,'CC',13);
INSERT INTO "continguts_clau" VALUES (44,14,'Dades, taules i gràfics estadístics.',2,'CC',14);
INSERT INTO "continguts_clau" VALUES (45,15,'Mètodes estadístics d’anàlisi de dades.',2,'CC',15);
INSERT INTO "continguts_clau" VALUES (46,16,'Sentit i mesura de la probabilitat.',2,'CC',16);
INSERT INTO "continguts_clau" VALUES (47,1,'Funcionalitats bàsiques dels dispositius.',8,'CCD',1);
INSERT INTO "continguts_clau" VALUES (48,2,'Tipus de connexions entre aparells.',8,'CCD',2);
INSERT INTO "continguts_clau" VALUES (49,3,'Emmagatzematge de dades i còpies de seguretat.',8,'CCD',3);
INSERT INTO "continguts_clau" VALUES (50,4,'Conceptes bàsics del sistema operatiu.',8,'CCD',4);
INSERT INTO "continguts_clau" VALUES (51,5,'Seguretat informàtica.',8,'CCD',5);
INSERT INTO "continguts_clau" VALUES (52,6,'Robòtica i programació.',8,'CCD',6);
INSERT INTO "continguts_clau" VALUES (53,7,'Realitat virtual i augmentada.',8,'CCD',7);
INSERT INTO "continguts_clau" VALUES (54,8,'Sistemes de projecció.',8,'CCD',8);
INSERT INTO "continguts_clau" VALUES (55,9,'Eines d’edició de documents de text, presentacions multimèdia i processament de dades numèriques.',8,'CCD',9);
INSERT INTO "continguts_clau" VALUES (56,10,'Llenguatge audiovisual: imatge fixa, so i vídeo.',8,'CCD',10);
INSERT INTO "continguts_clau" VALUES (57,11,'Funcionalitats dels navegadors.',8,'CCD',11);
INSERT INTO "continguts_clau" VALUES (58,12,'Cercadors: tipus de cerca i planificació.',8,'CCD',12);
INSERT INTO "continguts_clau" VALUES (59,13,'Fonts d’informació digital: selecció i valoració.',8,'CCD',13);
INSERT INTO "continguts_clau" VALUES (60,14,'Selecció, catalogació, emmagatzematge i compartició de la informació.',8,'CCD',14);
INSERT INTO "continguts_clau" VALUES (61,15,'Ètica i legalitat en l’ús i instal·lació de programes, comunicacions i publicacions, i en la utilització de la informació.',8,'CCD',15);
INSERT INTO "continguts_clau" VALUES (62,16,'Tractament de la informació.',8,'CCD',16);
INSERT INTO "continguts_clau" VALUES (63,17,'Construcció de coneixement: tècniques i instruments.',8,'CCD',17);
INSERT INTO "continguts_clau" VALUES (64,18,'Entorn personal d’aprenentatge (EPA).',8,'CCD',18);
INSERT INTO "continguts_clau" VALUES (65,19,'Dossiers personals d’aprenentatge (portafolis digital).',8,'CCD',19);
INSERT INTO "continguts_clau" VALUES (66,20,'Sistemes de comunicació.',8,'CCD',20);
INSERT INTO "continguts_clau" VALUES (67,21,'Normes de cortesia a la xarxa.',8,'CCD',21);
INSERT INTO "continguts_clau" VALUES (68,22,'Entorns de treball i aprenentatge col·laboratiu.',8,'CCD',22);
INSERT INTO "continguts_clau" VALUES (69,23,'Ciutadania digital: tràmits, gestió, lleure i cultura.',8,'CCD',23);
INSERT INTO "continguts_clau" VALUES (70,24,'Aprenentatge permanent: entorns virtuals d’aprenentatge, recursos per a l’aprenentatge formal i no formal a la xarxa...',8,'CCD',24);
INSERT INTO "continguts_clau" VALUES (71,25,'Ergonomia: salut física i psíquica.',8,'CCD',25);
INSERT INTO "continguts_clau" VALUES (72,26,'Entorns virtuals segurs.',8,'CCD',26);
INSERT INTO "continguts_clau" VALUES (73,27,'Sostenibilitat: consum d’energia, despesa d’impressió, mesures d’estalvi, substitució de dispositius, etc.',8,'CCD',27);
INSERT INTO "continguts_clau" VALUES (74,28,'Identitat digital: visibilitat, reputació, gestió de la privacitat pública i aliena.',8,'CCD',28);
INSERT INTO "continguts_clau" VALUES (82,1,'Capacitats físiques i sensorials.',9,'CC',1);
INSERT INTO "continguts_clau" VALUES (83,2,'Capacitats cognitives.',9,'CC',2);
INSERT INTO "continguts_clau" VALUES (84,3,'Capacitats emocionals.',9,'CC',3);
INSERT INTO "continguts_clau" VALUES (85,4,'Hàbits saludables.',9,'CC',4);
INSERT INTO "continguts_clau" VALUES (86,5,'Actitud de superació personal.',9,'CC',5);
INSERT INTO "continguts_clau" VALUES (87,6,'Hàbits d’aprenentatge.',9,'CC',6);
INSERT INTO "continguts_clau" VALUES (88,7,'Planificació dels aprenentatges.',9,'CC',7);
INSERT INTO "continguts_clau" VALUES (89,8,'Organització del coneixement.',9,'CC',8);
INSERT INTO "continguts_clau" VALUES (90,9,'Consolidació i recuperació del coneixement.',9,'CC',9);
INSERT INTO "continguts_clau" VALUES (91,10,'Transferència dels aprenentatges.',9,'CC',10);
INSERT INTO "continguts_clau" VALUES (92,11,'Característiques de la societat actual.',9,'CC',11);
INSERT INTO "continguts_clau" VALUES (93,12,'Aprenentatge continuat al llarg de la vida.',9,'CC',12);
INSERT INTO "continguts_clau" VALUES (94,13,'Actituds i hàbits en la societat i en el món professional.',9,'CC',13);
INSERT INTO "continguts_clau" VALUES (95,14,'Habilitats i actituds per al treball en grup.',9,'CC',14);
INSERT INTO "continguts_clau" VALUES (96,15,'Dinàmiques de cohesió de grup i col·laboratives.',9,'CC',15);
INSERT INTO "continguts_clau" VALUES (97,16,'Eines digitals col·laboratives.',9,'CC',16);
INSERT INTO "continguts_clau" VALUES (98,17,'Habilitats i actituds per a la participació.',9,'CC',17);
INSERT INTO "continguts_clau" VALUES (99,18,'Espais de participació.',9,'CC',18);
INSERT INTO "continguts_clau" VALUES (100,19,'Recursos i tècniques de participació.',9,'CC',19);
INSERT INTO "continguts_clau" VALUES (101,20,'Eines digitals de participació.',9,'CC',20);
COMMIT;
