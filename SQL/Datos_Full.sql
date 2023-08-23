USE INVENTARIO;

-- TIPO_PCI
INSERT INTO TIPO_PCI VALUES (1,'PCI');
INSERT INTO TIPO_PCI VALUES (2,'NAN');
INSERT INTO TIPO_PCI VALUES (4,'PCI EXPRESS');
INSERT INTO TIPO_PCI VALUES (5,'PCI-E 3.0');
INSERT INTO TIPO_PCI VALUES (6,'PCI-E 2.0 / ATI PCI-E 3.0');
INSERT INTO TIPO_PCI VALUES (7,'AGP/PCI');
INSERT INTO TIPO_PCI VALUES (8,'PCI 2.3');
INSERT INTO TIPO_PCI VALUES (9,'INTEGRADA');


-- EDIFICIO
INSERT INTO EDIFICIO VALUES (7, 'CAMPUS JURIQUILLA');
INSERT INTO EDIFICIO VALUES (8, 'EDIFICIO A');
INSERT INTO EDIFICIO VALUES (24, 'EDIFICIO B');
INSERT INTO EDIFICIO VALUES (12, 'EDIFICIO C');
INSERT INTO EDIFICIO VALUES (9, 'EDIFICIO D');
INSERT INTO EDIFICIO VALUES (21, 'EDIFICIO E');
INSERT INTO EDIFICIO VALUES (13, 'EDIFICIO F');
INSERT INTO EDIFICIO VALUES (2, 'EDIFICIO G');
INSERT INTO EDIFICIO VALUES (18, 'EDIFICIO H');
INSERT INTO EDIFICIO VALUES (25, 'EDIFICIO I');
INSERT INTO EDIFICIO VALUES (19, 'EDIFICIO J');
INSERT INTO EDIFICIO VALUES (22, 'EDIFICIO K');
INSERT INTO EDIFICIO VALUES (26, 'EDIFICIO L');
INSERT INTO EDIFICIO VALUES (23, 'EDIFICIO M');
INSERT INTO EDIFICIO VALUES (16, 'EDIFICIO N');
INSERT INTO EDIFICIO VALUES ( 1,'EDIFICIO O');
INSERT INTO EDIFICIO VALUES ( 4,'EDIFICIO P');
INSERT INTO EDIFICIO VALUES ( 5,'EDIFICIO Q');
INSERT INTO EDIFICIO VALUES ( 3,'EDIFICIO R');
INSERT INTO EDIFICIO VALUES (11, 'EDIFICIO S');
INSERT INTO EDIFICIO VALUES (6, 'EDIFICIO T');
INSERT INTO EDIFICIO VALUES (17, 'EDIFICIO U');
INSERT INTO EDIFICIO VALUES (14, 'EDIFICIO V');
INSERT INTO EDIFICIO VALUES (27, 'EDIFICIO W');
INSERT INTO EDIFICIO VALUES (15, 'EDIFICIO X');
INSERT INTO EDIFICIO VALUES (10, 'JUITEPEC, MORELOS');
INSERT INTO EDIFICIO VALUES (20, 'PALACIO DE MINERIA');

-- UBICACION
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (152, 'ADMINISTRACION SALA A Y B', 'PB', 'N/A', 5);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (151, 'ADMINISTRACION SALA C', '2', 'N/A', 5);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (130, 'COMPUTACION GRAFICA', '2', '219', 5);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (18, 'COMPUTACION SALA A', 'PB', '8', 5);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (128, 'COMPUTACION SALA B', 'PB', '7', 5);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (17, 'COMPUTACION SALA CISCO', '2', '218', 5);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (136, 'COMPUTACION SALA C', 'PB', '3', 9);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (11, 'ESTANDARES ABIERTOS JAVA-IBM','1', '102',6);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (150, 'IOS DEVELOPMENT LAB', 'PB', '10', 9);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (13, 'MICROCOMPUTADORAS', '2', '209', 5);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (53, 'MICROPROCESADORES Y MICROCONTROLADORES', '1', '102', 6);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (9, 'MICROSOFT RESEARCH', '2', '221', 5);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (15, 'PROGRAMA DE TECNOLOGIA EN COMPUTACION (PROTECO)', '2', '208', 5);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (16, 'REDES Y SEGURIDAD', '2', '208',5);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (116, 'SISTEMAS ELECTRICOS DE POTENCIA II', 'PB', 'N/A', 5);
INSERT INTO UBICACION (UBICACION_ID, NOMBRE, PISO, CUBICULO, EDIFICIO_ID)VALUES (200, 'SITE P', 'PB', '5', 9);

-- SUBTIPO
INSERT INTO SUBTIPO VALUES (1, 'TABLETA');
INSERT INTO SUBTIPO VALUES (2, 'PORTATIL');
INSERT INTO SUBTIPO VALUES (3, 'ESCRITORIO');
INSERT INTO SUBTIPO VALUES (4, 'TODO EN UNO');
INSERT INTO SUBTIPO VALUES (5, 'ESTACION DE TRABAJO');
INSERT INTO SUBTIPO VALUES (6, 'SERVIDOR');
INSERT INTO SUBTIPO VALUES (7, 'CLUSTER');
INSERT INTO SUBTIPO VALUES (8, 'CLIENTE LIGERO');
INSERT INTO SUBTIPO VALUES (9, 'MONITOR');
INSERT INTO SUBTIPO VALUES (10, 'IMPRESORA');
INSERT INTO SUBTIPO VALUES (11, 'MULTIFUNCIONAL');

-- MARCA
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (1, 'BESTEC');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (2, 'DELL');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (3, 'DELTAELECTR');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (4, 'EDGESYSTEMS');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (5, 'GENERICO');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (6, 'HP');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (7, 'ITT POWERSY');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (8, 'LENOVO');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (9, 'POWERMAN');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (10, 'BOSCH');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (11, 'RICOH');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (12, 'ROHS');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (13, '3COM');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (14, 'ACCO');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (15, 'ACER');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (16, 'AJAX');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (17, 'ALCATEL');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (18, 'ASUS');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (19, 'BELDEN');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (20, 'BLUEX');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (21, 'CABEL');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (22, 'CH');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (23, 'CISCO');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (24, 'CLORALEX');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (25, 'CONDUMEX');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (26, 'DEWALT');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (27, 'DISSTON');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (28, 'DURACEL');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (29, 'ELPIDA');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (30, 'FANAL');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (31, 'FIERO');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (32, 'GAMAXEL');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (33, 'HILLMAN');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (34, 'HUSKY');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (35, 'HYNIX');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (36, 'IDEAL');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (37, 'INIDANA');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (38, 'JANEL');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (39, 'JHONSON&JHO');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (40, 'KINGSTON');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (41, 'LEVITON');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (42, 'LYNKSIS');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (43, 'MAXTOR');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (44, 'MILKWAUKEE');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (45, 'MYLIN');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (46, 'NEC');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (47, 'NITTO');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (48, 'OML');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (49, 'PANDUIT');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (50, 'PHILIPS');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (51, 'PRETUL');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (52, 'RAID');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (53, 'RESISTOL');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (54, 'ROSHFRANS');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (55, 'SAMSUNSG');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (56, 'SCJHONSON');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (57, 'SEAGATE');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (58, 'SONY');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (59, 'STEREN');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (60, 'TOSHIBA');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (61, 'TP-LINK');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (62, 'TRUPER');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (63, 'UNIT');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (64, 'URREA');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (65, 'VLAKON');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (66, 'WELLER');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (67, 'WESTERN DIG');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (68, 'INTEL');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (69, 'AMD');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (70, 'QUALCOMM');
INSERT INTO MARCA (MARCA_ID, NOMBRE) VALUES (71, 'MEDIATEK');

-- MODELO
INSERT INTO MODELO VALUES (1, '4200', '',13);
INSERT INTO MODELO VALUES (2, '4226T', '',13);
INSERT INTO MODELO VALUES (3, '3CRDAG675', '',13);
INSERT INTO MODELO VALUES (4, 'SK-10', '',14);
INSERT INTO MODELO VALUES (5, 'ICONIA TAB', '',15);
INSERT INTO MODELO VALUES (6, 'DNX1843', '',15);
INSERT INTO MODELO VALUES (7, 'BICLORO', '',16);
INSERT INTO MODELO VALUES (8, 'DIGITAL EDO 1', '',17);
INSERT INTO MODELO VALUES (9, 'GEFORCE GTX 980', '',18);
INSERT INTO MODELO VALUES (10, 'MEMO PAD FDH10', '',18);
INSERT INTO MODELO VALUES (11, '6T125312AV', '',22);
INSERT INTO MODELO VALUES (12, '2800 SERIES', '',23);
INSERT INTO MODELO VALUES (13, 'CATALYST 3500', '',23);
INSERT INTO MODELO VALUES (14, 'CATALYST 3560', '',23);
INSERT INTO MODELO VALUES (15, 'CATALYST 2960', '',23);
INSERT INTO MODELO VALUES (16, '5G200-50', '',23);
INSERT INTO MODELO VALUES (17, 'WAP561', '',23);
INSERT INTO MODELO VALUES (18, 'W55001ABYS', '',2);
INSERT INTO MODELO VALUES (19, 'AF-B500 SLIM', '',4);
INSERT INTO MODELO VALUES (20, 'ACE390A', '',6);
INSERT INTO MODELO VALUES (31, 'VIQ10-24G', '',6);
INSERT INTO MODELO VALUES (32, 'CF064A', '',6);
INSERT INTO MODELO VALUES (33, 'JETDIRECT 300X', '',6);
INSERT INTO MODELO VALUES (34, 'FELXIBLE T610', '',6);
INSERT INTO MODELO VALUES (35, 'ST3660A', '',6);
INSERT INTO MODELO VALUES (36, 'DVD 740', '',6);
INSERT INTO MODELO VALUES (37, 'THINK CENTRE', '',8);
INSERT INTO MODELO VALUES (38, 'WRT54G', '',42);
INSERT INTO MODELO VALUES (39, 'WAP55AG', '',42);
INSERT INTO MODELO VALUES (40, 'WAP4400N', '',42);
INSERT INTO MODELO VALUES (41, '90432D2', '',43);
INSERT INTO MODELO VALUES (42, 'D33019', '',43);
INSERT INTO MODELO VALUES (43, '5T020H2', '',43);
INSERT INTO MODELO VALUES (44, 'CBOT', '',49);
INSERT INTO MODELO VALUES (45, 'RP3102', '',11);
INSERT INTO MODELO VALUES (46, 'SB2042H', '',55);
INSERT INTO MODELO VALUES (47, 'WU32553A', '',55);
INSERT INTO MODELO VALUES (48, 'SP0802N', '',55);
INSERT INTO MODELO VALUES (49, 'HD181HJ', '',55);
INSERT INTO MODELO VALUES (50, 'BAYGON', '',56);
INSERT INTO MODELO VALUES (51, 'BARRACUDA 7200.7', '',57);
INSERT INTO MODELO VALUES (52, 'BARRACUDA ATV', '',57);
INSERT INTO MODELO VALUES (53, 'CHEETA 10K.7', '',57);
INSERT INTO MODELO VALUES (54, 'BARRACUDA ATAII', '',57);
INSERT INTO MODELO VALUES (55, 'BARRACUDA 7200.10', '',57);
INSERT INTO MODELO VALUES (56, 'ST340015A', '',57);
INSERT INTO MODELO VALUES (57, 'VPL-CS6', '',58);
INSERT INTO MODELO VALUES (58, 'VPL-CX21', '',58);
INSERT INTO MODELO VALUES (59, 'LIM-CIR', '',59);
INSERT INTO MODELO VALUES (60, 'LIM-ESP', '',59);
INSERT INTO MODELO VALUES (61, 'FLUX', '',59);
INSERT INTO MODELO VALUES (62, 'CAU-150', '',59);
INSERT INTO MODELO VALUES (63, 'MUL-285', '',59);
INSERT INTO MODELO VALUES (64, 'HER-254', '',59);
INSERT INTO MODELO VALUES (65, 'HER-253', '',59);
INSERT INTO MODELO VALUES (66, 'SATELITE PSLB8U-027RL2', '',60);
INSERT INTO MODELO VALUES (67, 'TL-WA7510N', '',61);
INSERT INTO MODELO VALUES (68, 'AC3200', '',60);
INSERT INTO MODELO VALUES (69, 'TL-WDR4300', '',60);
INSERT INTO MODELO VALUES (70, 'WT-400', '',62);
INSERT INTO MODELO VALUES (71, 'UT682', '',62);
INSERT INTO MODELO VALUES (72, 'UT682', '',63);
INSERT INTO MODELO VALUES (73, 'EWSD51', '',66);
INSERT INTO MODELO VALUES (74, 'CAVIAR2100', '',67);
INSERT INTO MODELO VALUES (75, 'WD1600AAJS', '',67);
INSERT INTO MODELO VALUES (76, 'N/A', '',5);

-- PERFIL
INSERT INTO PERFIL VALUES (1, 'ESTUDIANTE');
INSERT INTO PERFIL VALUES (2, 'ACADEMICO');
INSERT INTO PERFIL VALUES (3, 'INVESTIGADOR');
INSERT INTO PERFIL VALUES (4, 'FUNCIONARIO');
INSERT INTO PERFIL VALUES (5, 'ADMINISTRATIVO');

-- SECTOR
INSERT INTO SECTOR VALUES (1,'EDUCACION');
INSERT INTO SECTOR VALUES (2,'INVESTIGACION');
INSERT INTO SECTOR VALUES (3,'DIFUSION CULTURAL');
INSERT INTO SECTOR VALUES (4,'ADMINISTRATIVO/SERVICIOS');

-- TIPO_SO
INSERT INTO TIPO_SO VALUES (1, 'WINDOWS');
INSERT INTO TIPO_SO VALUES (2, 'LINUX');
INSERT INTO TIPO_SO VALUES (3, 'MAC OS');
INSERT INTO TIPO_SO VALUES (4, 'UNIX');
INSERT INTO TIPO_SO VALUES (5, 'SOLARIS');
INSERT INTO TIPO_SO VALUES (6, 'ANDROID');
INSERT INTO TIPO_SO VALUES (7, 'IOS');
INSERT INTO TIPO_SO VALUES (8, 'FREEBSD');

-- MICROPROCESADOR
INSERT INTO MICROPROCESADOR VALUES (1, 'INTEL 386', 'X86', 'TERCERA', 68);
INSERT INTO MICROPROCESADOR VALUES (2, 'INTEL 486', 'X86', 'CUARTA', 68);
INSERT INTO MICROPROCESADOR VALUES (3, 'INTEL PENTIUM', 'X86', 'DECIMA', 68);
INSERT INTO MICROPROCESADOR VALUES (4, 'INTEL CELERON', 'X86', 'DECIMA', 68);
INSERT INTO MICROPROCESADOR VALUES (5, 'INTEL CORE DÚO', 'X86', 'UNDECIMA', 68);
INSERT INTO MICROPROCESADOR VALUES (6, 'INTEL ATOM', 'X86', 'ELKHART LAKE', 68);
INSERT INTO MICROPROCESADOR VALUES (7, 'INTEL I3', 'X86', 'UNDECIMA', 68);
INSERT INTO MICROPROCESADOR VALUES (8, 'INTEL I5', 'X86', 'UNDECIMA', 68);
INSERT INTO MICROPROCESADOR VALUES (9, 'INTEL I7', 'X86', 'UNDECIMA', 68);
INSERT INTO MICROPROCESADOR VALUES (10, 'INTEL XEON', 'X86', 'TERCERA', 68);
INSERT INTO MICROPROCESADOR VALUES (11, 'AMD DURON', 'X86', 'DURON 2003', 69);
INSERT INTO MICROPROCESADOR VALUES (12, 'AMD SEMPRON', 'X86', 'AMD SEMPRON 1500+', 69);
INSERT INTO MICROPROCESADOR VALUES (13, 'AMD TURION', 'X86', 'AMD TURION M640', 69);
INSERT INTO MICROPROCESADOR VALUES (14, 'AMD PHENOM', 'X86', 'AMD PHENOM IIX61100T', 69); 
INSERT INTO MICROPROCESADOR VALUES (15, 'AMD A3', 'X86', 'AMD A4-9120', 69);
INSERT INTO MICROPROCESADOR VALUES (16, 'AMD A6', 'X86', 'AMD A6-9550', 69);
INSERT INTO MICROPROCESADOR VALUES (17, 'AMD A8', 'X86', 'AMD A8-7680', 69);
INSERT INTO MICROPROCESADOR VALUES (18, 'AMD A10', 'X86', 'AMD A10-9700', 69);
INSERT INTO MICROPROCESADOR VALUES (19, 'ARM', 'ARM', 'ARM CORTEX-A78', 70);
INSERT INTO MICROPROCESADOR VALUES (20, 'QUALCOMM', 'ARM', 'SNAPDRAGON 888', 70);
INSERT INTO MICROPROCESADOR VALUES (21, 'MKT', 'ARM', 'DIMENSITY 1200', 71);
INSERT INTO MICROPROCESADOR VALUES (22, 'OTRO', 'N/A', 'N/A', 5);

-- TIPO RAM
INSERT INTO TIPO_RAM VALUES (1, 'DDR1');
INSERT INTO TIPO_RAM VALUES (2, 'DDR2');
INSERT INTO TIPO_RAM VALUES (3, 'DDR3');
INSERT INTO TIPO_RAM VALUES (4, 'DDR4');
INSERT INTO TIPO_RAM VALUES (5, 'EPROM');

-- TIPO_INTERFAZ RED
INSERT INTO TIPO_INTERFAZ_RED VALUES (1,'ETHERNET');
INSERT INTO TIPO_INTERFAZ_RED VALUES (2,'WI-FI');
INSERT INTO TIPO_INTERFAZ_RED VALUES (3,'ETHERNET-WIFI');
INSERT INTO TIPO_INTERFAZ_RED VALUES (4,'3G/4G');

-- TECNOLOGIA_HD
INSERT INTO TECNOLOGIA_HD VALUES (1, 'SATA I');
INSERT INTO TECNOLOGIA_HD VALUES (2, 'SATA II');
INSERT INTO TECNOLOGIA_HD VALUES (3, 'SATA III');
INSERT INTO TECNOLOGIA_HD VALUES (4, 'IDE');
INSERT INTO TECNOLOGIA_HD VALUES (5, 'SCSI');

-- PUERTOS
INSERT INTO PUERTO VALUES (1,'USB 2.0');
INSERT INTO PUERTO VALUES (2,'USB 3.0');
INSERT INTO PUERTO VALUES (3,'DB9');
INSERT INTO PUERTO VALUES (4,'DB25');
INSERT INTO PUERTO VALUES (5,'FIREWIRE');
INSERT INTO PUERTO VALUES (6,'PS72');
INSERT INTO PUERTO VALUES (7,'THUNDERBOLT');
INSERT INTO PUERTO VALUES (8,'NANO SIM');

-- INTERFAZ_VIDEO
INSERT INTO INTERFAZ_VIDEO VALUES (1, 'HDMI');
INSERT INTO INTERFAZ_VIDEO VALUES (2, 'VGA');
INSERT INTO INTERFAZ_VIDEO VALUES (3, 'DVI');
INSERT INTO INTERFAZ_VIDEO VALUES (4, 'DISPLAY PORT');
INSERT INTO INTERFAZ_VIDEO VALUES (5, 'THUNDERBOLT');

-- TITULO
INSERT INTO TITULO (TITULO_ID, NOMBRE, ABREVIATURA) VALUES (1, 'MAESTRO EN CIENCIAS', 'M.C');
INSERT INTO TITULO (TITULO_ID, NOMBRE, ABREVIATURA) VALUES (2, 'INGENIERO', 'ING.');
INSERT INTO TITULO (TITULO_ID, NOMBRE, ABREVIATURA) VALUES (3, 'MAESTRO EN INGENIERIA', 'M.I');
INSERT INTO TITULO (TITULO_ID, NOMBRE, ABREVIATURA) VALUES (4, 'LICENCIADO', 'LIC.');
INSERT INTO TITULO (TITULO_ID, NOMBRE, ABREVIATURA) VALUES (5, 'DOCTOR', 'DR.');

-- TIPO_UNIDAD_LECTORA
INSERT INTO TIPO_UNIDAD_LECTORA VALUES (1, 'DVD-CD'); 
INSERT INTO TIPO_UNIDAD_LECTORA VALUES (2, 'SSD');

-- TIPO_TARGETA_GRAFICA
INSERT INTO TIPO_TARGETA_GRAFICA VALUES (1, 'INTEGRADA'); 
INSERT INTO TIPO_TARGETA_GRAFICA VALUES (2, 'EXTERNA');
INSERT INTO TIPO_TARGETA_GRAFICA VALUES (3, 'Integrada/Externa');
INSERT INTO TIPO_TARGETA_GRAFICA VALUES (4, 'OTRO');

-- TARGETA_GRAFICA
INSERT INTO TARGETA_GRAFICA VALUES (1, 'AMD', 'AMD RADEON R7 GRAPHICS', 12, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (2, 'NAN', 'NAN', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (3, 'NVIDIA/INTEL', 'GEFORCE GTX 670', 13, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (4, 'NVIDIA/INTEL', 'GEFORCE GTX TITAN', 26, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (5, 'NVIDIA/INTEL', 'NVIDIA GEFORCE GTX 970', 16, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (6, 'NVIDIA/INTEL', 'QUADRO K620', 384, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (7, 'NVIDIA/INTEL', 'QUADRO 6000', 448, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (8, 'INTEL', 'IRIS PLUS GRAPHICS 640', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (9, 'ATI', 'ATI RADEON 7000-M', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (10, 'ATI', 'RADEON X600', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (11, 'INTEL ', 'GMA950 GRAPHICS', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (12, 'NVIDIA', 'GEFORCE GTX980', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (13, 'NVIDIA', 'GEFORCE GTX TITAN X', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (14, 'NVIDIA', 'GEFORCE GTX1080', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (15, 'INTEL', 'HD GRAPHICS P4600-P4700', 20, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (16, 'AMD', 'FIREPRO W4100', 20, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (17, 'NVIDIA', 'NVIDIA NVS 315', 20, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (18, 'NVIDIA', 'GEFORCE  GTX 980', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (19, 'NVIDIA', 'GEFORCE 9600 GS', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (20, 'INTEL', 'HD GRAPHICS 4000', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (21, 'INTEL', 'MEDIA ACCELERATOR 3150', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (22, 'MATROX', 'GMA G200 EV', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (23, 'NVIDIA ', 'GEFORCE GTX 1080', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (24, 'NVIDIA', 'GEFORCE GT 720', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (25, 'AMD', 'ATI RADEON X300', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (26, 'AMD', 'RV370 GL', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (27, 'MATROX', 'MGA G200E', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (28, 'ATI', ' RADEON HD 4200', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (29, 'INTEL', 'HD GRAPHICS', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (30, 'ATI', 'RADEON XPRESS 1150', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (31, 'ATI', 'AMD RADEON HD 8470', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (32, 'INTEL', 'GMA 3000', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (33, 'AMD', 'RV370 RADE0N X300 SE', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (34, 'NVIDIA', 'FX1700', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (35, 'ATI', 'ES1000', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (36, 'MATROX', 'G200', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (37, 'NVIDIA', 'GEFORCE 6150SE NFORCE 430', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (38, 'MATROX', 'G200ER2', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (39, 'NVIDIA', '6150SE GRAPHICS ', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (40, 'AMD', 'RADEON R4 GRAPHICS', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (41, 'INTEL', 'INTEL HD GRAPHICS 620', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (42, 'AND', 'ATI RADEON X1300 ', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (43, 'NVIDIA', 'GEFORCE GT720', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (44, 'INTEL', 'HD GRAPHICS 4400', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (45, 'INTEL', '82865G', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (46, 'INTEL', 'GMA 900', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (47, 'GENERICO', 'VIDEO EMBEBIDO', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (48, 'INTEL', 'INTEL IRIS PLUS GRAPHICS 655', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (49, 'NVIDIA', 'GEFORCE 8500 GT', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (50, 'INTEL', 'HD GRAPHICS 2000', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (51, 'INTEL', 'HD GRAPHICS P530', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (52, 'INTEL', 'HD GRAPHICS 200 DYNAMIC VIDEO', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (53, 'NVIDIA', 'GEFORCE GT 940M ', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (54, 'INTEL', 'INTEL GMA 3100', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (55, 'AMD', 'AMD MOBILITY RADEON HD 3600', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (56, 'INTEL', 'VIDEO ACELERATOR 900', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (57, 'INTEL', '815 INTEGRATED GRAPHICS AGP', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (58, 'AMD', 'MOBILITY RADEON HD 2600 XT', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (59, 'NVIDIA', 'GEFORCE G310', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (60, 'INTEL', '865GV', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (61, 'NVIDIA', 'ATI FIREGL  V3100', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (62, 'INTEL', 'HD GRAPHICS 520', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (63, 'NVIDIA', 'GEFORCE GTX 960', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (64, 'NVIDIA ', 'NVS310', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (65, 'INTEL', 'GMA X4500HD', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (66, 'NVIDIA', 'GTX 1050', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (67, 'INTEL ', 'HD GRAPHICS 630', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (68, 'INTEL', 'HD GRAPHICS 530', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (69, 'NVIDIA', 'GTX 750 TI', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (70, 'AMD', 'X300', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (71, 'AMD', 'X300 SE', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (72, 'AMD', ' RADEON HD GRAPHICS', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (73, 'AMD', 'ATHLON 5000B', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (74, 'ATI', ' RADEON 3100 GRAPHICS', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (75, 'ATI', ' RADEON XPRESS 200 SERIES', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (76, 'AMD', 'RADEON  HD 7540D', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (77, 'APPLE', 'POWERVR SERIES7XT', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (78, 'APPLE', 'POWERVR GT7600', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (79, 'APPLE', 'POWERVR GT6450', 0, 4, 1);
INSERT INTO TARGETA_GRAFICA VALUES (80, 'APPLE', 'POWERVR GT76450', 0, 4, 1);

-- DIVISION
INSERT INTO DIVISION VALUES (1,'DIE', 'DIVISIÓN DE INGENIERÍA ELECTRICA');
INSERT INTO DIVISION VALUES (2,'DCB', 'DIVISIÓN DE CIENCIAS BASICAS');
INSERT INTO DIVISION VALUES (3,'DICYG', 'DIVISIÓN DE INGENIERÍAS CIVIL Y GEOMÁTICA');
INSERT INTO DIVISION VALUES (4,'DICT', 'DIVISIÓN DE INGENIERÍA EN CIENCIAS DE LA TIERRA');
INSERT INTO DIVISION VALUES (5,'DIM', 'DIVISIÓN DE INGENIERÍA MECÁNICA E INDUSTRIAL');
INSERT INTO DIVISION VALUES (6,'DCSH', 'DIVISIÓN DE CIENCIAS SOCIALES Y HUMANIDADES');
INSERT INTO DIVISION VALUES (7,'UAT', 'UNIDAD DE ALTA TECNOLOGÍA');
INSERT INTO DIVISION VALUES (8,'DECYD', 'DIVISIÓN DE EDUCACIÓN CONTINUA Y A DISTANCIA');

-- DEPARTAMENTO
INSERT INTO DEPARTAMENTO VALUES (1,NULL,'COORDINACION DE CIENCIAS APLICADAS', 2);
INSERT INTO DEPARTAMENTO VALUES (2,NULL,'COORDINACION DE EVALUACION EDUCATIVA ', 8);
INSERT INTO DEPARTAMENTO VALUES (3,NULL,'COORDINACION DE FISICA Y QUIMCA ', 2);
INSERT INTO DEPARTAMENTO VALUES (4,NULL,'COORDINACION DE MATEMATICAS', 2);
INSERT INTO DEPARTAMENTO VALUES (5,NULL,'DEPARTAMENTO DE ASIGNATURAS SOCIO-HUMANISTICAS', 6);
INSERT INTO DEPARTAMENTO VALUES (6,NULL,'DEPARTAMENTO DE CONSTRUCCION', 3);
INSERT INTO DEPARTAMENTO VALUES (7,NULL,'DEPARTAMENTO DE ESTRUCTURAS', 3);
INSERT INTO DEPARTAMENTO VALUES (8,NULL,'DEPARTAMENTO DE FOTOGAMETRIA', 3);
INSERT INTO DEPARTAMENTO VALUES (9,NULL,'DEPARTAMENTO DE GEODESIA', 3);
INSERT INTO DEPARTAMENTO VALUES (10,NULL,'DEPARTAMENTO DE GEOTECNIA', 3);
INSERT INTO DEPARTAMENTO VALUES (11,NULL,'DEPARTAMENTO DE INGENIERIA GEOFISICA', 3);
INSERT INTO DEPARTAMENTO VALUES (12,NULL,'DEPARTAMENTO DE INGENIERIA GEOLOGICA', 3);
INSERT INTO DEPARTAMENTO VALUES (13,NULL,'DEPARTAMENTO DE INGENIERIA DE CONTROL', 5);
INSERT INTO DEPARTAMENTO VALUES(14,NULL,'DEPARTAMENTO DE INGENIERIA DE MINAS Y METALURGIA', 4);
INSERT INTO DEPARTAMENTO VALUES (15,NULL,'DEPARTAMENTO DE INGENIERIA EN SISTEMAS DE PLANEACION Y PLANEACION', 5);
INSERT INTO DEPARTAMENTO VALUES (16,NULL,'DEPARTAMENTO DE INGENIERIA ELECTRICA DE POTENCIA', 1);
INSERT INTO DEPARTAMENTO VALUES (17,NULL,'DEPARTAMENTO DE INGENIERIA  ELECTRONICA', 1);
INSERT INTO DEPARTAMENTO VALUES (18,NULL,'DEPARTAMENTO DE INGENIERIA EN COMPUTACION', 1);
INSERT INTO DEPARTAMENTO VALUES (19,NULL,'DEPARTAMENTO DE INGENIERIA EN TELECOMUNICACIONES', 1);
INSERT INTO DEPARTAMENTO VALUES (20,NULL,'DEPARTAMENTO DE INGENIERIA ENERGETICA', 3);
INSERT INTO DEPARTAMENTO VALUES (21,NULL,'DEPARTAMENTO DE INGENIERIA HIDRAULICA', 3);
INSERT INTO DEPARTAMENTO VALUES (22,NULL,'DEPARTAMENTO DE INGENIERIA PETROLERA', 4);
INSERT INTO DEPARTAMENTO VALUES (23,NULL,'DEPARTAMENTO DE INGENIERIA SANITARIA Y AMBIENTAL', 3);
INSERT INTO DEPARTAMENTO VALUES (24,NULL,'DEPARTAMENTO DE PROCESAMIENTO DE SEÑALES', 5);
INSERT INTO DEPARTAMENTO VALUES (25,NULL,'DEPARTAMENTO DE TOPOGRAFIA', 3);
INSERT INTO DEPARTAMENTO VALUES (26,NULL,'DEPARTAMENTO DE DISE Y MANUFACTURA', 5);
INSERT INTO DEPARTAMENTO VALUES (27,NULL,'DEPARTAMENTO DE INGENIERIA INDUSTRIAL', 5);
INSERT INTO DEPARTAMENTO VALUES (28,NULL,'DEPARTAMENTO DE INGENIERIA MECATRONICA', 1);
INSERT INTO DEPARTAMENTO VALUES (29,NULL,'DEPARTAMENTO DE SISTEMAS BIOMEDICOS', 5);
INSERT INTO DEPARTAMENTO VALUES (30,NULL,'DEPARTAMENTO DE TERMOFLUIDOS', 3);
INSERT INTO DEPARTAMENTO VALUES (31,NULL,'GEOLOGIA AREA DE YACIMIENTOS MINERALES', 3);
INSERT INTO DEPARTAMENTO VALUES (32,NULL,'GEOLOGIA AREA GEOLOGIC DEL PETROLEO Y GEOHIDROLOGIA', 3);

-- RAM
INSERT INTO RAM VALUES (1, 'HYNIX', ' ', 3, 8);
INSERT INTO RAM VALUES (2, 'KINGSTON', ' ', 3, 8);
INSERT INTO RAM VALUES (3, 'SAMSUNG', ' ', 2,  1);
INSERT INTO RAM VALUES (4, 'RAMAXEL', ' ', 2,  1);
INSERT INTO RAM VALUES (5, 'MICRON', ' ', 3, 2);
INSERT INTO RAM VALUES (6, 'SAMSUNG', ' ', 3, 1);
INSERT INTO RAM VALUES (7, 'MICRON', ' ', 3, 1);
INSERT INTO RAM VALUES (8, 'SAMSUNG', ' ', 3, 2);
INSERT INTO RAM VALUES (9, 'HYNIX', ' ', 3, 8);
INSERT INTO RAM VALUES (10, 'HYUNDAI', ' ', 3, 8);
INSERT INTO RAM VALUES (11, 'HYNIX', ' ', 3, 2);
INSERT INTO RAM VALUES (12, 'SAMSUNG', ' ', 3, 4);
INSERT INTO RAM VALUES (13, 'KINGSTON', ' ', 2, 1);
INSERT INTO RAM VALUES (14, 'HYNIX', ' ', 2, 1);
INSERT INTO RAM VALUES (15, 'SAMSUNG', ' ', 4, 8);
INSERT INTO RAM VALUES (16, 'HYNIX', ' ', 4, 8);
INSERT INTO RAM VALUES (17, 'HYNIX', ' ', 3, 4);
INSERT INTO RAM VALUES (18, 'KINGTON', ' ', 3, 8);
INSERT INTO RAM VALUES (19, 'RAMAXEL', ' ', 2, 1);
INSERT INTO RAM VALUES (20, 'NANYA', ' ', 2, 1);
INSERT INTO RAM VALUES (21, 'HYNIX', ' ', 2, 1);
INSERT INTO RAM VALUES (22, 'TRASCEND', ' ', 3, 8);
INSERT INTO RAM VALUES (23, 'DELL', ' ', 4, 8);
INSERT INTO RAM VALUES (24, 'KINGSTON', ' ', 3, 4);
INSERT INTO RAM VALUES (25, 'KINGSTON', ' ', 3, 2);
INSERT INTO RAM VALUES (26, 'MICRON', ' ', 3, 2);
INSERT INTO RAM VALUES (27, 'UNIFOSA', ' ', 3, 2);
INSERT INTO RAM VALUES (28, 'NANYA', ' ', 1, .256);
INSERT INTO RAM VALUES (29, 'NANYA', ' ', 1, 1);
INSERT INTO RAM VALUES (30, 'AMD', ' ', 3, 1);
INSERT INTO RAM VALUES (31, 'INTEL', ' ', 3, 1);
INSERT INTO RAM VALUES (32, 'MICRON', ' ', 4, 16);
INSERT INTO RAM VALUES (33, 'HYNNIX', ' ', 2, 2);
INSERT INTO RAM VALUES (34, 'HP', ' ', 3, 2);
INSERT INTO RAM VALUES (35, 'HP', ' ', 3, 1);
INSERT INTO RAM VALUES (36, 'APPLE', ' ', 3, 4);
INSERT INTO RAM VALUES (37, 'APPLE', ' ', 3, 8);
INSERT INTO RAM VALUES (38, 'HP', ' ', 2, 1);
INSERT INTO RAM VALUES (39, 'QUIMONDA', ' ', 2, 1);

-- DISCO_DURO
INSERT INTO DISCO_DURO VALUES (1, 'Z4YC2QYR', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (2, 'Z4YC2QZY', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (3, 'Z4YC2R96', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (4, 'Z4YC2VRJ', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (5, 'Z4YC2RBT', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (6, 'Z4YC2V00', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (7, 'Z1DDN0HT', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (8, 'Z4YC2R5H', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (9, 'Z4YC2VQ6', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (10, 'Z4YC2Y4C', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (11, 'Z4YC2RC5', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (12, 'Z4YC2R0N', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (13, 'Z4YC2V04', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (14, 'Z4YC2VZD', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (15, 'Z4YA5MZR', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (16, 'Z4YC2QZD', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (17, 'Z4YC2QSC', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (18, 'Z4YC2VLG', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (19, 'Z4YC2VFZ', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (20, 'Z4YC2R9X', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (21, 'Z4YC2W80', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (22, 'Z4YC2WAB', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (23, 'Z4YC2QVT', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (24, 'Z4YCZR56', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (25, 'Z4YC2RC3', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (26, 'Z4YC2QZZ', 'SEAGATE', ' ', 'AHCI', 1000, 3, 0);
INSERT INTO DISCO_DURO VALUES (27, 'ERTC2RC3', 'SEAGATE', ' ', 'AHCI', 250, 3, 1);
INSERT INTO DISCO_DURO VALUES (28, 'DFCC2QZZ', 'SEAGATE', ' ', 'AHCI', 500, 3, 1);
INSERT INTO DISCO_DURO VALUES (29, 'ERTC2RC3', 'KINGSTON', ' ', 'AHCI', 250, 3, 1);
INSERT INTO DISCO_DURO VALUES (30, 'DFCC2QZZ', 'KINGSTON', ' ', 'AHCI', 500, 3, 1);

-- RESPONSABLE RESGUARDO (NUMERO TRABAJADOR, RFC FICTISIO)
INSERT INTO RESPONSABLE_RESGUARDO VALUES (1, 'ALEJANDRO', 'VELÁZQUEZ', 'MENA', '11111', '1233', '553492837', 'mena@fi-b.unam.mx',1, 1);
INSERT INTO RESPONSABLE_RESGUARDO VALUES (2, 'ROCÍO ALEJANDRA', 'ALDECO', 'PÉREZ', '11111', '1233', '553492837', 'aldeco@fi-b.unam.mx',1, 5);

-- RESPONSABLE INTERNO
INSERT INTO RESPONSABLE_INTERNO VALUES (1, 'ALEJANDO', 'VELÁZQUEZ', 'MENA', '11111', '1233', '553492837', 'mena@fi-b.unam.mx',1, 1);
INSERT INTO RESPONSABLE_INTERNO VALUES (2, 'ROCÍO ALEJANDRA', 'ALDECO', 'PÉREZ', '11111', '1233', '553492837', 'aldeco@fi-b.unam.mx',1, 5);

-- SISTEMA OPERATIVO
INSERT INTO SISTEMA_OPERATIVO VALUES (1, '10', '64 BITS', 1);
INSERT INTO SISTEMA_OPERATIVO VALUES (2, '37.2', '64 BITS',2);
INSERT INTO SISTEMA_OPERATIVO VALUES (3, '10', '64 BITS',6);

-- USUARIO_FINAL
INSERT INTO USUARIO_FINAL VALUES (1, 'ALUMNO', 1, 1);
INSERT INTO USUARIO_FINAL VALUES (2, 'INVESTIGADOR', 2, 3);
INSERT INTO USUARIO_FINAL VALUES (3, 'PERSONAL ACADEMICO', 1, 5);
INSERT INTO USUARIO_FINAL VALUES (4, 'PERSONAL ADMINISTRATIVO', 4, 5);
INSERT INTO USUARIO_FINAL VALUES (5, 'BIBLIOTECA USUARIO', 2, 1);
INSERT INTO USUARIO_FINAL VALUES (6, 'BIBLIOTECA ADMINISTRATIVO', 4, 5);
INSERT INTO USUARIO_FINAL VALUES (7, 'SERVIDOR WEB', 2, 3);
INSERT INTO USUARIO_FINAL VALUES (8, 'SERVIDOR', 4, 4);

-- UNIDAD LECTORA
INSERT INTO UNIDAD_LECTORA VALUES (1, 1, '657958-001', 'HP', 'Bisel Negro,Unidad combinada CD-RW/DVD,Sata, búfer de 2 MB,velocidad de transferencia 145 MB/s');
INSERT INTO UNIDAD_LECTORA VALUES (2, 1, '8300 SF', 'HP', 'Bisel Negro,Unidad combinada CD-RW/DVD,Sata, búfer de 2 MB,velocidad de transferencia 145 MB/s');
INSERT INTO UNIDAD_LECTORA VALUES (3, 1, '726537', 'HP','');
INSERT INTO UNIDAD_LECTORA VALUES (4, 1, 'GT301', 'HP','');
INSERT INTO UNIDAD_LECTORA VALUES (5, 2, 'DV3500', 'HP','Bisel Negro,Unidad combinada CD-RW/DVD,Sata, búfer de 2 MB,velocidad de transferencia 145 MB/s');
INSERT INTO UNIDAD_LECTORA VALUES (6, 2, '2234LA', 'HP','');
INSERT INTO UNIDAD_LECTORA VALUES (7, 2, '7581S', 'HP', 'Bisel Negro,Unidad combinada CD-RW/DVD,Sata, búfer de 2 MB,velocidad de transferencia 145 MB/s');

INSERT INTO INTERFAZ_RED VALUES (1, 'GIGA', 'AirPortExtreme', 'Apple', 1, 1);
INSERT INTO INTERFAZ_RED VALUES (2, 'FO', 'AirPortExtreme', 'Apple', 1, 3);
INSERT INTO INTERFAZ_RED VALUES (3, 'NIC', 'AirPortExtreme', 'Apple', 0, 2);