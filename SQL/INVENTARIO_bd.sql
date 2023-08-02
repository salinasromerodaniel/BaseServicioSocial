-- SELECCIONAR BD
USE INVENTARIO;

--
-- DROPS
--
ALTER TABLE ACTIVO DROP FOREIGN KEY FK_ACTIVO_RESGUARDO;
ALTER TABLE ACTIVO DROP FOREIGN KEY FK_ACTIVO_USUARIO_FINAL;
ALTER TABLE ACTIVO DROP FOREIGN KEY FK_ACTIVO_RESPONSABLE_INTERNO;
ALTER TABLE ACTIVO DROP FOREIGN KEY FK_ACTIVO_UBICACION;
ALTER TABLE ACTIVO DROP FOREIGN KEY FK_ACTIVO_MODELO;
ALTER TABLE DEPARTAMENTO DROP FOREIGN KEY FK_DEPARTAMENTO_DIVISION;
ALTER TABLE DISCO_DURO DROP FOREIGN KEY FK_DISCO_DURO_TECNOLOGIA_HD;
ALTER TABLE DISPO_DD DROP FOREIGN KEY FK_DISPO_DD_ACTIVO;
ALTER TABLE DISPO_DD DROP FOREIGN KEY FK_DISPO_DD_DISCO_DURO;
ALTER TABLE DISPO_INTELIIGENTE DROP FOREIGN KEY FK_DISPO_INTELIGENTE_ACTIVO;
ALTER TABLE DISPO_INTELIIGENTE DROP FOREIGN KEY FK_DISPO_INTELIGENTE_SISTEMA_OPERATIVO;
ALTER TABLE DISPO_INTELIIGENTE DROP FOREIGN KEY FK_DISPO_INTELIGENTE_MICROPROCESADOR;
ALTER TABLE DISPO_INTELIIGENTE DROP FOREIGN KEY FK_DISPO_INTELIGENTE_SUBTIPO;
ALTER TABLE DISPO_INTELIIGENTE DROP FOREIGN KEY FK_DISPO_INTELIGENTE_TARGETA_GRAFICA;
ALTER TABLE DISPO_PUERTO DROP FOREIGN KEY FK_DISPO_PUERTO_DISPO_INTELIIGENTE;
ALTER TABLE DISPO_PUERTO DROP FOREIGN KEY FK_DISPO_PUERTO_PUERTO;
ALTER TABLE DISPO_RAM DROP FOREIGN KEY FK_DISPO_RAM_DISPO_INTELIIGENTE;
ALTER TABLE DISPO_RAM DROP FOREIGN KEY FK_DISPO_RAM_RAM;
ALTER TABLE DISPOSITIVO_RED DROP FOREIGN KEY FK_DISPOSITIVO_RED_ACTIVO;
ALTER TABLE DISPOSITIVO_RED DROP FOREIGN KEY FK_DISPOSITIVO_RED_INTERFAZ_RED;
ALTER TABLE GRAFICA_INTERFAZ_VIDEO DROP FOREIGN KEY FK_GRAFICA_INTERFAZ_VIDEO_TARGETA_GRAFICA;
ALTER TABLE GRAFICA_INTERFAZ_VIDEO DROP FOREIGN KEY FK_GRAFICA_INTERFAZ_VIDEO_INTERFAZ_VIDEO;
ALTER TABLE HERRAMIENTA_CONSUMIBLE DROP FOREIGN KEY FK_HERRAMIENTA_CONSUMIBLE_ACTIVO;
ALTER TABLE HISTORICO_ACTIVO_RESPONSABLE DROP FOREIGN KEY FK_HISTORICO_ACTIVO_RESPONSABLE_ACTIVO;
ALTER TABLE HISTORICO_ACTIVO_RESPONSABLE DROP FOREIGN KEY FK_HISTORICO_ACTIVO_RESPONSABLE_RESPONSABLE_RESGUARDO;
ALTER TABLE HISTORICO_ACTIVO_RESPONSABLE_INTERNO DROP FOREIGN KEY FK_HISTORICO_ACTIVO_RESPONSABLE_INTERNO_ACTIVO;
ALTER TABLE HISTORICO_ACTIVO_RESPONSABLE_INTERNO DROP FOREIGN KEY FK_HISTORICO_ACTIVO_RESPONSABLE_INTERNO__RESPONSABLE_INTERNO;
ALTER TABLE HISTORICO_ACTIVO_USUARIO DROP FOREIGN KEY FK_HISTORICO_ACTIVO_USUARIO_ACTIVO;
ALTER TABLE HISTORICO_ACTIVO_USUARIO DROP FOREIGN KEY FK_HISTORICO_ACTIVO_USUARIO_USUARIO_FINAL;
ALTER TABLE HISTORICO_HERRAMIENTA_CONSUMIBLE DROP FOREIGN KEY FK_HISTORICO_HERRAMIENTA_CONSUMIBLE_HERRAMIENTA_CONSUMIBLE;
ALTER TABLE INTERFAZ_RED DROP FOREIGN KEY FK_INTERFAZ_RED_TIPO_INTERFAZ_RED;
ALTER TABLE LIBRO DROP FOREIGN KEY FK_LIBRO_ACTIVO;
ALTER TABLE MODELO DROP FOREIGN KEY FK_MODELO_MARCA;
ALTER TABLE PROYECTOR_TV DROP FOREIGN KEY FK_PROYECTOR_TV_TARGETA_GRAFICA;
ALTER TABLE PROYECTOR_TV DROP FOREIGN KEY FK_PROYECTOR_TV_ACTIVO;
ALTER TABLE RAM DROP FOREIGN KEY FK_RAM_TIPO_RAM;
ALTER TABLE RESPONSABLE_INTERNO DROP FOREIGN KEY FK_RESPONSABLE_INTERNO_DEPARTAMENTO;
ALTER TABLE RESPONSABLE_INTERNO DROP FOREIGN KEY FK_RESPONSABLE_INTERNO_TITULO;
ALTER TABLE RESPONSABLE_RESGUARDO DROP FOREIGN KEY FK_RESPONSABLE_RESGUARDO_DEPARTAMENTO;
ALTER TABLE RESPONSABLE_RESGUARDO DROP FOREIGN KEY FK_RESPONSABLE_RESGUARDO_TITULO;
ALTER TABLE SISTEMA_OPERATIVO DROP FOREIGN KEY FK_SISTEMA_OPERATIVO_TIPO_SO;
ALTER TABLE TARGETA_GRAFICA DROP FOREIGN KEY FK_TARGETA_GRAFICA_TIPO_TARGETA_GRAFICA;
ALTER TABLE UBICACION DROP FOREIGN KEY FK_UBICACION_EDIFICIO;
ALTER TABLE USUARIO_FINAL DROP FOREIGN KEY FK_USUARIO_FINAL_PERFIL;
ALTER TABLE USUARIO_FINAL DROP FOREIGN KEY FK_USUARIO_FINAL_SECTOR;


DROP TABLE IF EXISTS ACTIVO;
DROP TABLE IF EXISTS DEPARTAMENTO;
DROP TABLE IF EXISTS DISCO_DURO;
DROP TABLE IF EXISTS DISPO_DD;
DROP TABLE IF EXISTS DISPO_INTELIIGENTE;
DROP TABLE IF EXISTS DISPO_PUERTO;
DROP TABLE IF EXISTS DISPO_RAM;
DROP TABLE IF EXISTS DISPOSITIVO_RED;
DROP TABLE IF EXISTS DIVISION;
DROP TABLE IF EXISTS EDIFICIO;
DROP TABLE IF EXISTS GRAFICA_INTERFAZ_VIDEO;
DROP TABLE IF EXISTS HERRAMIENTA_CONSUMIBLE;
DROP TABLE IF EXISTS HISTORICO_ACTIVO_RESPONSABLE;
DROP TABLE IF EXISTS HISTORICO_ACTIVO_RESPONSABLE_INTERNO;
DROP TABLE IF EXISTS HISTORICO_ACTIVO_USUARIO;
DROP TABLE IF EXISTS HISTORICO_HERRAMIENTA_CONSUMIBLE;
DROP TABLE IF EXISTS INTERFAZ_RED;
DROP TABLE IF EXISTS INTERFAZ_VIDEO;
DROP TABLE IF EXISTS LIBRO;
DROP TABLE IF EXISTS MARCA;
DROP TABLE IF EXISTS MICROPROCESADOR;
DROP TABLE IF EXISTS MODELO;
DROP TABLE IF EXISTS PERFIL;
DROP TABLE IF EXISTS PROYECTOR_TV;
DROP TABLE IF EXISTS PUERTO;
DROP TABLE IF EXISTS RAM;
DROP TABLE IF EXISTS RESPONSABLE_INTERNO;
DROP TABLE IF EXISTS RESPONSABLE_RESGUARDO;
DROP TABLE IF EXISTS SECTOR;
DROP TABLE IF EXISTS SISTEMA_OPERATIVO;
DROP TABLE IF EXISTS SUBTIPO;
DROP TABLE IF EXISTS TARGETA_GRAFICA;
DROP TABLE IF EXISTS TECNOLOGIA_HD;
DROP TABLE IF EXISTS TIPO_INTERFAZ_RED;
DROP TABLE IF EXISTS TIPO_SO;
DROP TABLE IF EXISTS TIPO_RAM;
DROP TABLE IF EXISTS TIPO_TARGETA_GRAFICA;
DROP TABLE IF EXISTS TITULO;
DROP TABLE IF EXISTS UBICACION;
DROP TABLE IF EXISTS USUARIO_FINAL;

--
-- TABLES
--

-- ACTIVO
CREATE TABLE ACTIVO(
    ACTIVO_ID                   DECIMAL(10, 0)    NOT NULL,
    FACTURA                     VARCHAR(100),
    SERIAL                      VARCHAR(40),
    NUM_INVENTARIO              DECIMAL(10, 0),
    TIPO                        CHAR(1)           NOT NULL,
    NOMBRE                      VARCHAR(40)       NOT NULL,
    ESTADO                      VARCHAR(20)       NOT NULL,
    USUARIO_FINAL_ID            DECIMAL(10, 0)    NOT NULL,
    RESPONSABLE_INTERNO_ID      DECIMAL(10, 0)    NOT NULL,
    RESPONSABLE_RESGUARDO_ID    DECIMAL(10, 0)    NOT NULL,
    MODELO_ID                   DECIMAL(11, 0)    NOT NULL,
    UBICACION_ID                DECIMAL(10, 0)    NOT NULL,
    PRIMARY KEY (ACTIVO_ID)
);

-- DEPARTAMENTO
CREATE TABLE DEPARTAMENTO(
    DEPARTAMENTO_ID    DECIMAL(3, 0)    NOT NULL,
    CLAVE              VARCHAR(7),
    NOMBRE             VARCHAR(40)      NOT NULL,
    DIVISION_ID        DECIMAL(2, 0)    NOT NULL,
    PRIMARY KEY (DEPARTAMENTO_ID)
);

-- DISCO DURO
CREATE TABLE DISCO_DURO(
    DISCO_DURO_ID           DECIMAL(5,0)    NOT NULL,
    NUMERO_SERIE            VARCHAR(30)     NOT NULL,
    DISCO_DURO_MARCA        VARCHAR(30),
    DISCO_DURO_MODELO       VARCHAR(30),
    DISCO_DURO_CAPACIDAD    DECIMAL(3,0)    NOT NULL,
    TECNOLOGIA_HD_ID        DECIMAL(3,0)    NOT NULL,
    MECANICO_SOLIDO         BIT             NOT NULL,
    PRIMARY KEY (DISCO_DURO_ID)
);

-- DISPOSITIVO_DD
CREATE TABLE DISPO_DD(
    DISPO_DD_ID         DECIMAL(5,0)    NOT NULL,  
    ACTIVO_ID           DECIMAL(10, 0)  NOT NULL,
    DISCO_DURO_ID       DECIMAL(5,0)    NOT NULL,
    PRIMARY KEY (DISPO_DD_ID)
);

-- DISPO INTELIGENTE
CREATE TABLE DISPO_INTELIIGENTE(
    ACTIVO_ID               DECIMAL(10, 0)    NOT NULL,
    CARACTERISTICAS         TEXT,
    NUM_PROCESADORES        DECIMAL(2, 0),
    RAM_INSTALADA           DECIMAL(2, 0),
    RAM_MAX                 DECIMAL(2, 0)     NOT NULL,
    MICROPROCESADOR_ID      DECIMAL(10, 0),
    SISTEMA_OPERATIVO_ID    DECIMAL(5, 0),
    SUBTIPO_ID              DECIMAL(5,0)      NOT NULL,
    TARGETA_GARFICA_ID      DECIMAL(5,0)      NOT NULL,
    PRIMARY KEY (ACTIVO_ID)
);

CREATE TABLE DISPO_PUERTO(
    DISPO_PUERTO_ID DECIMAL(3,0)    NOT NULL,
    PUERTO_ID       DECIMAL(3,0)    NOT NULL,
    ACTIVO_ID       DECIMAL(10, 0)  NOT NULL,
    PRIMARY KEY (DISPO_PUERTO_ID)
);

-- DISPO_RAM
CREATE TABLE DISPO_RAM(
    DISPO_RAM_ID    DECIMAL(10, 0)    NOT NULL,
    ACTIVO_ID       DECIMAL(10, 0)    NOT NULL,
    RAM_ID          DECIMAL(10, 0)    NOT NULL,
    FECHA_COLOC     DATE              NOT NULL,
    PRIMARY KEY (DISPO_RAM_ID)
);

-- DISPOSITIVO_RED
CREATE TABLE DISPOSITIVO_RED(
    DISPOSITIVO_RED_ID     DECIMAL(10, 0)     NOT NULL,
    ACTIVO_ID              DECIMAL(10, 0),             
    INTERFAZ_RED_ID        DECIMAL(10, 0),   
    MAC                    VARCHAR(30),
    IP                     VARCHAR(15),
    PRIMARY KEY (DISPOSITIVO_RED_ID)
);

-- DIVISION
CREATE TABLE DIVISION(
    DIVISION_ID    DECIMAL(2, 0)    NOT NULL,
    ACRONIMO       VARCHAR(10)      NOT NULL,
    NOMBRE         VARCHAR(50)      NOT NULL,
    PRIMARY KEY (DIVISION_ID)
);

-- EDIFICIO
CREATE TABLE EDIFICIO(
    EDIFICIO_ID    DECIMAL(5, 0)    NOT NULL,
    NOMBRE         VARCHAR(20)      NOT NULL,
    PRIMARY KEY (EDIFICIO_ID)
);

-- GRAFICA_INTERFAZ-VIDEO
CREATE TABLE GRAFICA_INTERFAZ_VIDEO(
    GRAFICA_INTERFAZ_VIDEO_ID   DECIMAL(5,0)    NOT NULL,
    TARGETA_GARFICA_ID          DECIMAL(5,0)    NOT NULL,
    INTERFAZ_VIDEO_ID           DECIMAL(5,0)    NOT NULL,
    PRIMARY KEY (GRAFICA_INTERFAZ_VIDEO_ID)
);

-- HERRAMIENTA_CONSUMIBLE
CREATE TABLE HERRAMIENTA_CONSUMIBLE(
    ACTIVO_ID        DECIMAL(10, 0)    NOT NULL,
    FECHA_COMPRA     DATE              NOT NULL,
    FECHA_CONSUMO    DATE,
    CANTIDAD         DECIMAL(3, 0)     NOT NULL,
    CONTENIDO        VARCHAR(10),
    DESCRIPCION      VARCHAR(500),
    PRIMARY KEY (ACTIVO_ID)
);

-- HISTORICO_ACTIVO_RESPONSABLE
CREATE TABLE HISTORICO_ACTIVO_RESPONSABLE(
    HISTORICO_ACTIVO_RESPONSABLE_ID    DECIMAL(10, 0)    NOT NULL,
    FECHA_CAMBIO_RESGUARDO             DATE              NOT NULL,
    RESPONSABLE_RESGUARDO_ID           DECIMAL(10, 0)    NOT NULL,
    ACTIVO_ID                          DECIMAL(10, 0)    NOT NULL,
    PRIMARY KEY (HISTORICO_ACTIVO_RESPONSABLE_ID)
);

-- HISTORICO_ACTIVO_RESPONSABLE_INTERNO
CREATE TABLE HISTORICO_ACTIVO_RESPONSABLE_INTERNO(
    HISTORICO_ACTIVO_RESPONSABLE_INT_ID    DECIMAL(10, 0)    NOT NULL,
    FECHA_PRESTAMO                         DATE              NOT NULL,
    RESPONSABLE_INTERNO_ID                 DECIMAL(10, 0)    NOT NULL,
    ACTIVO_ID                              DECIMAL(10, 0)    NOT NULL,
    PRIMARY KEY (HISTORICO_ACTIVO_RESPONSABLE_INT_ID)
);

-- HISTORICO_ACTIVO_USUARIO
CREATE TABLE HISTORICO_ACTIVO_USUARIO(
    HISTORICO_ACTIVO_USUARIO_ID    DECIMAL(10, 0)    NOT NULL,
    FECHA_PRESTAMO                 DATE              NOT NULL,
    USUARIO_FINAL_ID               DECIMAL(10, 0)    NOT NULL,
    ACTIVO_ID                      DECIMAL(10, 0)    NOT NULL,
    PRIMARY KEY (HISTORICO_ACTIVO_USUARIO_ID)
);

-- HISTORICO_HERRAMIENTA_CONSUMIBLE
CREATE TABLE HISTORICO_HERRAMIENTA_CONSUMIBLE(
    HISTORICO_HERRAMIENTA_CONSUMIBLE_ID    DECIMAL(10, 0)    NOT NULL,
    FECHA_CONSUMO                          DATE              NOT NULL,
    ACTIVO_ID                              DECIMAL(10, 0)    NOT NULL,
    PRIMARY KEY (HISTORICO_HERRAMIENTA_CONSUMIBLE_ID)
);

-- INTERFAZ_RED
CREATE TABLE INTERFAZ_RED(
    INTERFAZ_RED_ID         DECIMAL(10, 0) NOT NULL, 
    INTERFAZ_RED_NOMBRE     VARCHAR(20),
    INTERFAZ_RED_MODELO     VARCHAR(20),
    INTERFAZ_RED_MARCA      VARCHAR(20),
    TIPO_INTERFAZ_RED_ID    DECIMAL(3,0) NOT NULL,
    PRIMARY KEY (INTERFAZ_RED_ID)
);

-- INTERFAZ_VIDEO
CREATE TABLE INTERFAZ_VIDEO(
    INTERFAZ_VIDEO_ID       DECIMAL(5,0)    NOT NULL,
    INTERFAZ_VIDEO_NOMBRE   VARCHAR(30)     NOT NULL,
    PRIMARY KEY (INTERFAZ_VIDEO_ID)
);

-- LIBRO
CREATE TABLE LIBRO(
    ACTIVO_ID    DECIMAL(10, 0)    NOT NULL,
    EDITORIAL    VARCHAR(40),
    EDICION      VARCHAR(40),
    ANIO         DECIMAL(4, 0),
    AUTOR        VARCHAR(500)      NOT NULL,
    PRIMARY KEY (ACTIVO_ID)
);

-- MARCA
CREATE TABLE MARCA(
    MARCA_ID    DECIMAL(5, 0)    NOT NULL,
    NOMBRE      VARCHAR(11)      NOT NULL,
    PRIMARY KEY (MARCA_ID)
);

-- MICROPROSESADOR
CREATE TABLE MICROPROCESADOR(
    MICROPROCESADOR_ID    DECIMAL(10, 0)    NOT NULL,
    NOMBRE                VARCHAR(35)       NOT NULL,
    ARQUITECTURA          VARCHAR(10)       NOT NULL,
    GENERACION            VARCHAR(20)       NOT NULL,
    MARCA                 DECIMAL(5, 0)     NOT NULL,
    PRIMARY KEY (MICROPROCESADOR_ID)
);

-- MODELO
CREATE TABLE MODELO(
    MODELO_ID    DECIMAL(11, 0)    NOT NULL,
    NOMBRE       VARCHAR(30)       NOT NULL,
    IMAGEN       VARCHAR(100),
    MARCA_ID     DECIMAL(5, 0)     NOT NULL,
    PRIMARY KEY (MODELO_ID)
);

-- PERFIL 
CREATE TABLE PERFIL(
    PERFIL_USUARIO_ID           DECIMAL(10, 0)  NOT NULL,
    PERFIL_USUARIO_NOMBRE      VARCHAR(15),
    PRIMARY KEY (PERFIL_USUARIO_ID)
);

-- PROYECTOR_TV
CREATE TABLE PROYECTOR_TV(
    ACTIVO_ID           DECIMAL(10, 0)    NOT NULL,
    VGA                 DECIMAL(1, 0)     NOT NULL,
    HDMI                DECIMAL(1, 0)     NOT NULL,
    USB                 DECIMAL(1, 0)     NOT NULL,
    ETHERNET            DECIMAL(1, 0)     NOT NULL,
    CONTROL_REMOTO      VARCHAR(2)        NOT NULL,
    TARGETA_GARFICA_ID  DECIMAL(5,0)      NOT NULL,
    PRIMARY KEY (ACTIVO_ID)
);

-- PUERTO
CREATE TABLE PUERTO(
    PUERTO_ID       DECIMAL(3,0)    NOT NULL,
    PUERTO_NOMBRE   VARCHAR(30)     NOT NULL,
    PRIMARY KEY (PUERTO_ID)
);

-- RAM
CREATE TABLE RAM(
    RAM_ID       DECIMAL(10, 0)    NOT NULL,
    MARCA        VARCHAR(40)       NOT NULL,
    NUM_SERIE    VARCHAR(40)       NOT NULL,
    TIPO_RAM_ID  DECIMAL(3,0)        NOT NULL,
    CAPACIDAD    DECIMAL(3, 0)     NOT NULL,
    PRIMARY KEY (RAM_ID)
);

-- RESPONSABLE_INTERNO
CREATE TABLE RESPONSABLE_INTERNO(
    RESPONSABLE_INTERNO_ID    DECIMAL(10, 0)    NOT NULL,
    NOMBRE                    VARCHAR(50)       NOT NULL,
    AP_PATERNO                VARCHAR(50)       NOT NULL,
    AP_MATERNO                VARCHAR(50)       NOT NULL,
    NUM_TRB                   DECIMAL(7, 0)     NOT NULL,
    RFC                       VARCHAR(15)       NOT NULL,
    TELEFONO                  DECIMAL(12, 0)    NOT NULL,
    CORREO                    VARCHAR(70)       NOT NULL,
    DEPARTAMENTO_ID           DECIMAL(3, 0)     NOT NULL,
    TITULO_ID                 DECIMAL(5, 0)     NOT NULL,
    PRIMARY KEY (RESPONSABLE_INTERNO_ID)
);

-- RESPONSABLE_RESGUARDO
CREATE TABLE RESPONSABLE_RESGUARDO(
    RESPONSABLE_RESGUARDO_ID    DECIMAL(10, 0)    NOT NULL,
    NOMBRE                      VARCHAR(50)       NOT NULL,
    AP_PATERNO                  VARCHAR(50)       NOT NULL,
    AP_MATERNO                  VARCHAR(50)       NOT NULL,
    NUM_TRB                     DECIMAL(7, 0)     NOT NULL,
    RFC                         VARCHAR(15)       NOT NULL,
    TELEFONO                    DECIMAL(12, 0)    NOT NULL,
    CORREO                      VARCHAR(70)       NOT NULL,
    DEPARTAMENTO_ID             DECIMAL(3, 0)     NOT NULL,
    TITULO_ID                   DECIMAL(5, 0)     NOT NULL,
    PRIMARY KEY (RESPONSABLE_RESGUARDO_ID)
);

-- SECTOR
CREATE TABLE SECTOR(
    SECTOR_ID    DECIMAL(5, 0)    NOT NULL,
    NOMBRE       VARCHAR(40)      NOT NULL,
    PRIMARY KEY (SECTOR_ID)
);

-- SISTEMA_OPERATIVO
CREATE TABLE SISTEMA_OPERATIVO(
    SISTEMA_OPERATIVO_ID    DECIMAL(5, 0)    NOT NULL,
    VERSION                 VARCHAR(40)      NOT NULL,
    ARQUITECTURA            VARCHAR(15)      NOT NULL,
    TIPO_SO_ID              DECIMAL(6, 0)    NOT NULL,
    PRIMARY KEY (SISTEMA_OPERATIVO_ID)
);

-- SUBTIPO
CREATE TABLE SUBTIPO(
    SUBTIPO_ID      DECIMAL(5,0)      NOT NULL,
    NOMBRE          VARCHAR(20)      NOT NULL, 
    PRIMARY KEY (SUBTIPO_ID)         
);

-- TARGETA_GRAFICA
CREATE TABLE TARGETA_GRAFICA(
    TARGETA_GARFICA_ID      DECIMAL(5,0)    NOT NULL,
    TARGETA_GRAFICA_MARCA   VARCHAR(30),
    TARGETA_GRAFICA_MODELO  VARCHAR(30),
    TIPO_TARGETA_GRAFICA_ID DECIMAL(5,0)    NOT NULL,    
    TARGETA_GRAFICA_PCI     VARCHAR(40),
    PRIMARY KEY (TARGETA_GARFICA_ID)
);

-- TECNOLOGIA HD
CREATE TABLE TECNOLOGIA_HD(
    TECNOLOGIA_HD_ID    DECIMAL(3,0)    NOT NULL,
    NOMBRE              VARCHAR(30)     NOT NULL,
    PRIMARY KEY (TECNOLOGIA_HD_ID)
);

-- TIPO_INTERFAZ_RED
CREATE TABLE TIPO_INTERFAZ_RED(
    TIPO_INTERFAZ_RED_ID    DECIMAL(3,0) NOT NULL,
    NOMBRE                  VARCHAR(20) NOT NULL,
    PRIMARY KEY (TIPO_INTERFAZ_RED_ID)
);

-- TIPO_ SISTEMAOPERATIVO
CREATE TABLE TIPO_SO(
    TIPO_SO_ID    DECIMAL(6, 0)    NOT NULL,
    NOMBRE        VARCHAR(40)      NOT NULL,
    PRIMARY KEY (TIPO_SO_ID)
);

-- TIPO_RAM
CREATE TABLE TIPO_RAM(
    TIPO_RAM_ID     DECIMAL(3,0) NOT NULL,
    NOMBRE          VARCHAR(20) NOT NULL,
    PRIMARY KEY (TIPO_RAM_ID)
);

-- TIPO-TARGETA_GRAFICA
CREATE TABLE TIPO_TARGETA_GRAFICA(
    TIPO_TARGETA_GRAFICA_ID     DECIMAL(5,0)    NOT NULL,   
    TIPO_TARGETA_GRAFICA_NOMBRE VARCHAR(30)     NOT NULL,
    PRIMARY KEY (TIPO_TARGETA_GRAFICA_ID)
);

-- TITULO
CREATE TABLE TITULO(
    TITULO_ID      DECIMAL(5, 0)    NOT NULL,
    NOMBRE         VARCHAR(60)      NOT NULL,
    ABREVIATURA    VARCHAR(10)      NOT NULL,
    PRIMARY KEY (TITULO_ID)
);

-- UBICACION
CREATE TABLE UBICACION(
    UBICACION_ID    DECIMAL(10, 0)    NOT NULL,
    PISO            VARCHAR(5),
    NOMBRE          VARCHAR(150)      NOT NULL,
    CUBICULO        VARCHAR(10),
    CORREO          VARCHAR(60),
    TELEFONO        DECIMAL(12, 0),
    EDIFICIO_ID     DECIMAL(5, 0)     NOT NULL,
    PRIMARY KEY (UBICACION_ID)
);

-- USUARIO_FINAL
CREATE TABLE USUARIO_FINAL(
    USUARIO_FINAL_ID    DECIMAL(10, 0)    NOT NULL,
    NOMBRE              VARCHAR(30)     NOT NULL,
    SECTOR_ID           DECIMAL(5, 0)     NOT NULL,
    PERFIL_USUARIO_ID   DECIMAL(10, 0)    NOT NULL,
    PRIMARY KEY (USUARIO_FINAL_ID)
);

--
-- FOREING KEYS
--

-- DE ACTIVO
ALTER TABLE ACTIVO ADD CONSTRAINT FK_ACTIVO_RESGUARDO
    FOREIGN KEY (RESPONSABLE_RESGUARDO_ID)
    REFERENCES RESPONSABLE_RESGUARDO(RESPONSABLE_RESGUARDO_ID);

ALTER TABLE ACTIVO ADD CONSTRAINT FK_ACTIVO_USUARIO_FINAL
    FOREIGN KEY (USUARIO_FINAL_ID)
    REFERENCES USUARIO_FINAL(USUARIO_FINAL_ID);

ALTER TABLE ACTIVO ADD CONSTRAINT FK_ACTIVO_RESPONSABLE_INTERNO 
    FOREIGN KEY (RESPONSABLE_INTERNO_ID)
    REFERENCES RESPONSABLE_INTERNO(RESPONSABLE_INTERNO_ID);

ALTER TABLE ACTIVO ADD CONSTRAINT FK_ACTIVO_UBICACION
    FOREIGN KEY (UBICACION_ID)
    REFERENCES UBICACION(UBICACION_ID);

ALTER TABLE ACTIVO ADD CONSTRAINT FK_ACTIVO_MODELO
    FOREIGN KEY (MODELO_ID)
    REFERENCES MODELO(MODELO_ID);

-- DE DEPARTAMENTO
ALTER TABLE DEPARTAMENTO ADD CONSTRAINT FK_DEPARTAMENTO_DIVISION
    FOREIGN KEY (DIVISION_ID)
    REFERENCES DIVISION(DIVISION_ID);

-- DE DISCO DURO
ALTER TABLE DISCO_DURO ADD CONSTRAINT FK_DISCO_DURO_TECNOLOGIA_HD
    FOREIGN KEY (TECNOLOGIA_HD_ID)
    REFERENCES TECNOLOGIA_HD (TECNOLOGIA_HD_ID);

-- DE DISPO_DD
ALTER TABLE DISPO_DD ADD CONSTRAINT FK_DISPO_DD_ACTIVO
    FOREIGN KEY (ACTIVO_ID)
    REFERENCES DISPO_INTELIIGENTE (ACTIVO_ID);

ALTER TABLE DISPO_DD ADD CONSTRAINT FK_DISPO_DD_DISCO_DURO
    FOREIGN KEY (DISCO_DURO_ID)
    REFERENCES DISCO_DURO (DISCO_DURO_ID);

-- DE DISPO_INTELIGENTE
ALTER TABLE DISPO_INTELIIGENTE ADD CONSTRAINT FK_DISPO_INTELIGENTE_ACTIVO 
    FOREIGN KEY (ACTIVO_ID)
    REFERENCES ACTIVO(ACTIVO_ID);

ALTER TABLE DISPO_INTELIIGENTE ADD CONSTRAINT FK_DISPO_INTELIGENTE_SISTEMA_OPERATIVO
    FOREIGN KEY (SISTEMA_OPERATIVO_ID)
    REFERENCES SISTEMA_OPERATIVO(SISTEMA_OPERATIVO_ID);

ALTER TABLE DISPO_INTELIIGENTE ADD CONSTRAINT FK_DISPO_INTELIGENTE_MICROPROCESADOR
    FOREIGN KEY (MICROPROCESADOR_ID)
    REFERENCES MICROPROCESADOR(MICROPROCESADOR_ID);

ALTER TABLE DISPO_INTELIIGENTE ADD CONSTRAINT FK_DISPO_INTELIGENTE_SUBTIPO
    FOREIGN KEY (SUBTIPO_ID)
    REFERENCES SUBTIPO(SUBTIPO_ID);

ALTER TABLE DISPO_INTELIIGENTE ADD CONSTRAINT FK_DISPO_INTELIGENTE_TARGETA_GRAFICA
    FOREIGN KEY (TARGETA_GARFICA_ID)
    REFERENCES TARGETA_GRAFICA(TARGETA_GARFICA_ID);

-- DE DISPO_PUERTO
ALTER TABLE DISPO_PUERTO ADD CONSTRAINT FK_DISPO_PUERTO_DISPO_INTELIIGENTE
    FOREIGN KEY (ACTIVO_ID)
    REFERENCES DISPO_INTELIIGENTE(ACTIVO_ID);

ALTER TABLE DISPO_PUERTO ADD CONSTRAINT FK_DISPO_PUERTO_PUERTO
    FOREIGN KEY (PUERTO_ID)
    REFERENCES PUERTO(PUERTO_ID);

-- DE DISPO_RAM
ALTER TABLE DISPO_RAM ADD CONSTRAINT FK_DISPO_RAM_DISPO_INTELIIGENTE
    FOREIGN KEY (ACTIVO_ID)
    REFERENCES DISPO_INTELIIGENTE(ACTIVO_ID);

ALTER TABLE DISPO_RAM ADD CONSTRAINT FK_DISPO_RAM_RAM
    FOREIGN KEY (RAM_ID)
    REFERENCES RAM(RAM_ID);

-- DE DISPOSITIVO_RED
ALTER TABLE DISPOSITIVO_RED ADD CONSTRAINT FK_DISPOSITIVO_RED_ACTIVO
    FOREIGN KEY (ACTIVO_ID)
    REFERENCES ACTIVO(ACTIVO_ID);

ALTER TABLE DISPOSITIVO_RED ADD CONSTRAINT FK_DISPOSITIVO_RED_INTERFAZ_RED
    FOREIGN KEY (INTERFAZ_RED_ID)
    REFERENCES INTERFAZ_RED(INTERFAZ_RED_ID);

-- DE GRAFICA_INTERFAZ_VIDEO
ALTER TABLE GRAFICA_INTERFAZ_VIDEO ADD CONSTRAINT FK_GRAFICA_INTERFAZ_VIDEO_TARGETA_GRAFICA
    FOREIGN KEY (TARGETA_GARFICA_ID)
    REFERENCES TARGETA_GRAFICA(TARGETA_GARFICA_ID);

ALTER TABLE GRAFICA_INTERFAZ_VIDEO ADD CONSTRAINT FK_GRAFICA_INTERFAZ_VIDEO_INTERFAZ_VIDEO
    FOREIGN KEY (INTERFAZ_VIDEO_ID)
    REFERENCES INTERFAZ_VIDEO(INTERFAZ_VIDEO_ID);

-- DE HERRAMIENTA_CONSUMIBLE
ALTER TABLE HERRAMIENTA_CONSUMIBLE ADD CONSTRAINT FK_HERRAMIENTA_CONSUMIBLE_ACTIVO
    FOREIGN KEY (ACTIVO_ID)
    REFERENCES ACTIVO(ACTIVO_ID);


-- DE HISTORICO_ACTIVO_RESPONSABLE
ALTER TABLE HISTORICO_ACTIVO_RESPONSABLE ADD CONSTRAINT FK_HISTORICO_ACTIVO_RESPONSABLE_ACTIVO
    FOREIGN KEY (ACTIVO_ID)
    REFERENCES ACTIVO(ACTIVO_ID);

ALTER TABLE HISTORICO_ACTIVO_RESPONSABLE ADD CONSTRAINT FK_HISTORICO_ACTIVO_RESPONSABLE_RESPONSABLE_RESGUARDO
    FOREIGN KEY (RESPONSABLE_RESGUARDO_ID)
    REFERENCES RESPONSABLE_RESGUARDO(RESPONSABLE_RESGUARDO_ID);

-- HISTORICO_ACTIVO_RESPONSABLE_INTERNO
ALTER TABLE HISTORICO_ACTIVO_RESPONSABLE_INTERNO ADD CONSTRAINT FK_HISTORICO_ACTIVO_RESPONSABLE_INTERNO_ACTIVO
    FOREIGN KEY (ACTIVO_ID)
    REFERENCES ACTIVO(ACTIVO_ID);

ALTER TABLE HISTORICO_ACTIVO_RESPONSABLE_INTERNO ADD CONSTRAINT FK_HISTORICO_ACTIVO_RESPONSABLE_INTERNO__RESPONSABLE_INTERNO
    FOREIGN KEY (RESPONSABLE_INTERNO_ID)
    REFERENCES RESPONSABLE_INTERNO(RESPONSABLE_INTERNO_ID);

-- DE HISTORICO_ACTIVO_USUARIO
ALTER TABLE HISTORICO_ACTIVO_USUARIO ADD CONSTRAINT FK_HISTORICO_ACTIVO_USUARIO_ACTIVO 
    FOREIGN KEY (ACTIVO_ID)
    REFERENCES ACTIVO(ACTIVO_ID);

ALTER TABLE HISTORICO_ACTIVO_USUARIO ADD CONSTRAINT FK_HISTORICO_ACTIVO_USUARIO_USUARIO_FINAL
    FOREIGN KEY (USUARIO_FINAL_ID)
    REFERENCES USUARIO_FINAL(USUARIO_FINAL_ID);

-- DE HISTORICO_HERRAMIENTA_CONSUMIBLE
ALTER TABLE HISTORICO_HERRAMIENTA_CONSUMIBLE ADD CONSTRAINT FK_HISTORICO_HERRAMIENTA_CONSUMIBLE_HERRAMIENTA_CONSUMIBLE
    FOREIGN KEY (ACTIVO_ID)
    REFERENCES HERRAMIENTA_CONSUMIBLE(ACTIVO_ID);

-- DE INTERFAZ_RED
ALTER TABLE INTERFAZ_RED ADD CONSTRAINT FK_INTERFAZ_RED_TIPO_INTERFAZ_RED 
    FOREIGN KEY (TIPO_INTERFAZ_RED_ID) 
    REFERENCES TIPO_INTERFAZ_RED(TIPO_INTERFAZ_RED_ID);

-- DE LIBRO
ALTER TABLE LIBRO ADD CONSTRAINT FK_LIBRO_ACTIVO
    FOREIGN KEY (ACTIVO_ID)
    REFERENCES ACTIVO(ACTIVO_ID);

-- DE MODELO
ALTER TABLE MODELO ADD CONSTRAINT FK_MODELO_MARCA 
    FOREIGN KEY (MARCA_ID)
    REFERENCES MARCA(MARCA_ID);

-- DE PROYECTOR_TV
ALTER TABLE PROYECTOR_TV ADD CONSTRAINT FK_PROYECTOR_TV_ACTIVO
    FOREIGN KEY (ACTIVO_ID)
    REFERENCES ACTIVO(ACTIVO_ID);

ALTER TABLE PROYECTOR_TV ADD CONSTRAINT FK_PROYECTOR_TV_TARGETA_GRAFICA
    FOREIGN KEY (TARGETA_GARFICA_ID)
    REFERENCES TARGETA_GRAFICA(TARGETA_GARFICA_ID);

-- DE RAM
ALTER TABLE RAM ADD CONSTRAINT FK_RAM_TIPO_RAM
    FOREIGN KEY (TIPO_RAM_ID)
    REFERENCES TIPO_RAM(TIPO_RAM_ID);

-- DE RESPONSABLE_INTERNO
ALTER TABLE RESPONSABLE_INTERNO ADD CONSTRAINT FK_RESPONSABLE_INTERNO_DEPARTAMENTO
    FOREIGN KEY (DEPARTAMENTO_ID)
    REFERENCES DEPARTAMENTO(DEPARTAMENTO_ID);

ALTER TABLE RESPONSABLE_INTERNO ADD CONSTRAINT FK_RESPONSABLE_INTERNO_TITULO
    FOREIGN KEY (TITULO_ID)
    REFERENCES TITULO(TITULO_ID);

-- DE RESPONSABLE_RESGUARDO
ALTER TABLE RESPONSABLE_RESGUARDO ADD CONSTRAINT FK_RESPONSABLE_RESGUARDO_DEPARTAMENTO
    FOREIGN KEY (DEPARTAMENTO_ID)
    REFERENCES DEPARTAMENTO(DEPARTAMENTO_ID);

ALTER TABLE RESPONSABLE_RESGUARDO ADD CONSTRAINT FK_RESPONSABLE_RESGUARDO_TITULO
    FOREIGN KEY (TITULO_ID)
    REFERENCES TITULO(TITULO_ID);

-- DE SISTEMA_OPERATIVO
ALTER TABLE SISTEMA_OPERATIVO ADD CONSTRAINT FK_SISTEMA_OPERATIVO_TIPO_SO
    FOREIGN KEY (TIPO_SO_ID)
    REFERENCES TIPO_SO(TIPO_SO_ID);

-- DE TARGETA GRAFICA
ALTER TABLE TARGETA_GRAFICA ADD CONSTRAINT FK_TARGETA_GRAFICA_TIPO_TARGETA_GRAFICA
    FOREIGN KEY (TIPO_TARGETA_GRAFICA_ID)
    REFERENCES TIPO_TARGETA_GRAFICA(TIPO_TARGETA_GRAFICA_ID);

-- DE UBICACION
ALTER TABLE UBICACION ADD CONSTRAINT FK_UBICACION_EDIFICIO
    FOREIGN KEY (EDIFICIO_ID)
    REFERENCES EDIFICIO(EDIFICIO_ID);

-- DE USUARIO_FINAL
ALTER TABLE USUARIO_FINAL ADD CONSTRAINT FK_USUARIO_FINAL_SECTOR
    FOREIGN KEY (SECTOR_ID)
    REFERENCES SECTOR(SECTOR_ID);

ALTER TABLE USUARIO_FINAL ADD CONSTRAINT FK_USUARIO_FINAL_PERFIL
    FOREIGN KEY (PERFIL_USUARIO_ID)
    REFERENCES PERFIL(PERFIL_USUARIO_ID);