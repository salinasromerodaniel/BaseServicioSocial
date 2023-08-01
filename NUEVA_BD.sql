-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: inventario
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `activo`
--

DROP TABLE IF EXISTS `activo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activo` (
  `ACTIVO_ID` decimal(10,0) NOT NULL,
  `FACTURA` varchar(100) DEFAULT NULL,
  `SERIAL` varchar(40) DEFAULT NULL,
  `NUM_INVENTARIO` decimal(10,0) DEFAULT NULL,
  `TIPO` char(1) NOT NULL,
  `NOMBRE` varchar(40) NOT NULL,
  `ESTADO` varchar(20) NOT NULL,
  `USUARIO_FINAL_ID` decimal(10,0) NOT NULL,
  `RESPONSABLE_INTERNO_ID` decimal(10,0) NOT NULL,
  `RESPONSABLE_RESGUARDO_ID` decimal(10,0) NOT NULL,
  `MODELO_ID` decimal(11,0) NOT NULL,
  `UBICACION_ID` decimal(10,0) NOT NULL,
  PRIMARY KEY (`ACTIVO_ID`),
  KEY `FK_ACTIVO_RESGUARDO` (`RESPONSABLE_RESGUARDO_ID`),
  KEY `FK_ACTIVO_USUARIO_FINAL` (`USUARIO_FINAL_ID`),
  KEY `FK_ACTIVO_RESPONSABLE_INTERNO` (`RESPONSABLE_INTERNO_ID`),
  KEY `FK_ACTIVO_UBICACION` (`UBICACION_ID`),
  KEY `FK_ACTIVO_MODELO` (`MODELO_ID`),
  CONSTRAINT `FK_ACTIVO_MODELO` FOREIGN KEY (`MODELO_ID`) REFERENCES `modelo` (`MODELO_ID`),
  CONSTRAINT `FK_ACTIVO_RESGUARDO` FOREIGN KEY (`RESPONSABLE_RESGUARDO_ID`) REFERENCES `responsable_resguardo` (`RESPONSABLE_RESGUARDO_ID`),
  CONSTRAINT `FK_ACTIVO_RESPONSABLE_INTERNO` FOREIGN KEY (`RESPONSABLE_INTERNO_ID`) REFERENCES `responsable_interno` (`RESPONSABLE_INTERNO_ID`),
  CONSTRAINT `FK_ACTIVO_UBICACION` FOREIGN KEY (`UBICACION_ID`) REFERENCES `ubicacion` (`UBICACION_ID`),
  CONSTRAINT `FK_ACTIVO_USUARIO_FINAL` FOREIGN KEY (`USUARIO_FINAL_ID`) REFERENCES `usuario_final` (`USUARIO_FINAL_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activo`
--

LOCK TABLES `activo` WRITE;
/*!40000 ALTER TABLE `activo` DISABLE KEYS */;
/*!40000 ALTER TABLE `activo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departamento`
--

DROP TABLE IF EXISTS `departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departamento` (
  `DEPARTAMENTO_ID` decimal(3,0) NOT NULL,
  `CLAVE` varchar(7) DEFAULT NULL,
  `NOMBRE` varchar(40) NOT NULL,
  `DIVISION_ID` decimal(2,0) NOT NULL,
  PRIMARY KEY (`DEPARTAMENTO_ID`),
  KEY `FK_DEPARTAMENTO_DIVISION` (`DIVISION_ID`),
  CONSTRAINT `FK_DEPARTAMENTO_DIVISION` FOREIGN KEY (`DIVISION_ID`) REFERENCES `division` (`DIVISION_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departamento`
--

LOCK TABLES `departamento` WRITE;
/*!40000 ALTER TABLE `departamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dispo_inteliigente`
--

DROP TABLE IF EXISTS `dispo_inteliigente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dispo_inteliigente` (
  `ACTIVO_ID` decimal(10,0) NOT NULL,
  `CARACTERISTICAS` text,
  `NUM_PROCESADORES` decimal(2,0) DEFAULT NULL,
  `RAM_INSTALADA` decimal(2,0) DEFAULT NULL,
  `RAM_MAX` decimal(2,0) DEFAULT NULL,
  `MICROPROCESADOR_ID` decimal(10,0) NOT NULL,
  `SISTEMA_OPERATIVO_ID` decimal(5,0) NOT NULL,
  PRIMARY KEY (`ACTIVO_ID`),
  KEY `FK_DISPO_INTELIGENTE_SISTEMA_OPERATIVO` (`SISTEMA_OPERATIVO_ID`),
  KEY `FK_DISPO_INTELIGENTE_MICROPROCESADOR` (`MICROPROCESADOR_ID`),
  CONSTRAINT `FK_DISPO_INTELIGENTE_ACTIVO` FOREIGN KEY (`ACTIVO_ID`) REFERENCES `activo` (`ACTIVO_ID`),
  CONSTRAINT `FK_DISPO_INTELIGENTE_MICROPROCESADOR` FOREIGN KEY (`MICROPROCESADOR_ID`) REFERENCES `microprocesador` (`MICROPROCESADOR_ID`),
  CONSTRAINT `FK_DISPO_INTELIGENTE_SISTEMA_OPERATIVO` FOREIGN KEY (`SISTEMA_OPERATIVO_ID`) REFERENCES `sistema_operativo` (`SISTEMA_OPERATIVO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dispo_inteliigente`
--

LOCK TABLES `dispo_inteliigente` WRITE;
/*!40000 ALTER TABLE `dispo_inteliigente` DISABLE KEYS */;
/*!40000 ALTER TABLE `dispo_inteliigente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dispo_ram`
--

DROP TABLE IF EXISTS `dispo_ram`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dispo_ram` (
  `DISPO_RAM_ID` decimal(10,0) NOT NULL,
  `ACTIVO_ID` decimal(10,0) NOT NULL,
  `RAM_ID` decimal(10,0) NOT NULL,
  PRIMARY KEY (`DISPO_RAM_ID`),
  KEY `FK_DISPO_RAM_DISPO_INTELIIGENTE` (`ACTIVO_ID`),
  KEY `FK_DISPO_RAM_RAM` (`RAM_ID`),
  CONSTRAINT `FK_DISPO_RAM_DISPO_INTELIIGENTE` FOREIGN KEY (`ACTIVO_ID`) REFERENCES `dispo_inteliigente` (`ACTIVO_ID`),
  CONSTRAINT `FK_DISPO_RAM_RAM` FOREIGN KEY (`RAM_ID`) REFERENCES `ram` (`RAM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dispo_ram`
--

LOCK TABLES `dispo_ram` WRITE;
/*!40000 ALTER TABLE `dispo_ram` DISABLE KEYS */;
/*!40000 ALTER TABLE `dispo_ram` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `division`
--

DROP TABLE IF EXISTS `division`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `division` (
  `DIVISION_ID` decimal(2,0) NOT NULL,
  `ACRONIMO` varchar(10) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  PRIMARY KEY (`DIVISION_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `division`
--

LOCK TABLES `division` WRITE;
/*!40000 ALTER TABLE `division` DISABLE KEYS */;
/*!40000 ALTER TABLE `division` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `edificio`
--

DROP TABLE IF EXISTS `edificio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `edificio` (
  `EDIFICIO_ID` decimal(5,0) NOT NULL,
  `NOMBRE` varchar(20) NOT NULL,
  PRIMARY KEY (`EDIFICIO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `edificio`
--

LOCK TABLES `edificio` WRITE;
/*!40000 ALTER TABLE `edificio` DISABLE KEYS */;
/*!40000 ALTER TABLE `edificio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `herramienta_consumible`
--

DROP TABLE IF EXISTS `herramienta_consumible`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `herramienta_consumible` (
  `ACTIVO_ID` decimal(10,0) NOT NULL,
  `FECHA_COMPRA` date NOT NULL,
  `FECHA_CONSUMO` date DEFAULT NULL,
  `CANTIDAD` decimal(3,0) NOT NULL,
  `CONTENIDO` varchar(10) DEFAULT NULL,
  `DESCRIPCION` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`ACTIVO_ID`),
  CONSTRAINT `FK_HERRAMIENTA_CONSUMIBLE_ACTIVO` FOREIGN KEY (`ACTIVO_ID`) REFERENCES `activo` (`ACTIVO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `herramienta_consumible`
--

LOCK TABLES `herramienta_consumible` WRITE;
/*!40000 ALTER TABLE `herramienta_consumible` DISABLE KEYS */;
/*!40000 ALTER TABLE `herramienta_consumible` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historico_activo_responsable`
--

DROP TABLE IF EXISTS `historico_activo_responsable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historico_activo_responsable` (
  `HISTORICO_ACTIVO_RESPONSABLE_ID` decimal(10,0) NOT NULL,
  `FECHA_CAMBIO_RESGUARDO` date NOT NULL,
  `RESPONSABLE_RESGUARDO_ID` decimal(10,0) NOT NULL,
  `ACTIVO_ID` decimal(10,0) NOT NULL,
  PRIMARY KEY (`HISTORICO_ACTIVO_RESPONSABLE_ID`),
  KEY `FK_HISTORICO_ACTIVO_RESPONSABLE_ACTIVO` (`ACTIVO_ID`),
  KEY `FK_HISTORICO_ACTIVO_RESPONSABLE_RESPONSABLE_RESGUARDO` (`RESPONSABLE_RESGUARDO_ID`),
  CONSTRAINT `FK_HISTORICO_ACTIVO_RESPONSABLE_ACTIVO` FOREIGN KEY (`ACTIVO_ID`) REFERENCES `activo` (`ACTIVO_ID`),
  CONSTRAINT `FK_HISTORICO_ACTIVO_RESPONSABLE_RESPONSABLE_RESGUARDO` FOREIGN KEY (`RESPONSABLE_RESGUARDO_ID`) REFERENCES `responsable_resguardo` (`RESPONSABLE_RESGUARDO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historico_activo_responsable`
--

LOCK TABLES `historico_activo_responsable` WRITE;
/*!40000 ALTER TABLE `historico_activo_responsable` DISABLE KEYS */;
/*!40000 ALTER TABLE `historico_activo_responsable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historico_activo_responsable_interno`
--

DROP TABLE IF EXISTS `historico_activo_responsable_interno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historico_activo_responsable_interno` (
  `HISTORICO_ACTIVO_RESPONSABLE_INT_ID` decimal(10,0) NOT NULL,
  `FECHA_PRESTAMO` date NOT NULL,
  `RESPONSABLE_INTERNO_ID` decimal(10,0) NOT NULL,
  `ACTIVO_ID` decimal(10,0) NOT NULL,
  PRIMARY KEY (`HISTORICO_ACTIVO_RESPONSABLE_INT_ID`),
  KEY `FK_HISTORICO_ACTIVO_RESPONSABLE_INTERNO_ACTIVO` (`ACTIVO_ID`),
  KEY `FK_HISTORICO_ACTIVO_RESPONSABLE_INTERNO__RESPONSABLE_INTERNO` (`RESPONSABLE_INTERNO_ID`),
  CONSTRAINT `FK_HISTORICO_ACTIVO_RESPONSABLE_INTERNO__RESPONSABLE_INTERNO` FOREIGN KEY (`RESPONSABLE_INTERNO_ID`) REFERENCES `responsable_interno` (`RESPONSABLE_INTERNO_ID`),
  CONSTRAINT `FK_HISTORICO_ACTIVO_RESPONSABLE_INTERNO_ACTIVO` FOREIGN KEY (`ACTIVO_ID`) REFERENCES `activo` (`ACTIVO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historico_activo_responsable_interno`
--

LOCK TABLES `historico_activo_responsable_interno` WRITE;
/*!40000 ALTER TABLE `historico_activo_responsable_interno` DISABLE KEYS */;
/*!40000 ALTER TABLE `historico_activo_responsable_interno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historico_activo_usuario`
--

DROP TABLE IF EXISTS `historico_activo_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historico_activo_usuario` (
  `HISTORICO_ACTIVO_USUARIO_ID` decimal(10,0) NOT NULL,
  `FECHA_PRESTAMO` date NOT NULL,
  `USUARIO_FINAL_ID` decimal(10,0) NOT NULL,
  `ACTIVO_ID` decimal(10,0) NOT NULL,
  PRIMARY KEY (`HISTORICO_ACTIVO_USUARIO_ID`),
  KEY `FK_HISTORICO_ACTIVO_USUARIO_ACTIVO` (`ACTIVO_ID`),
  KEY `FK_HISTORICO_ACTIVO_USUARIO_USUARIO_FINAL` (`USUARIO_FINAL_ID`),
  CONSTRAINT `FK_HISTORICO_ACTIVO_USUARIO_ACTIVO` FOREIGN KEY (`ACTIVO_ID`) REFERENCES `activo` (`ACTIVO_ID`),
  CONSTRAINT `FK_HISTORICO_ACTIVO_USUARIO_USUARIO_FINAL` FOREIGN KEY (`USUARIO_FINAL_ID`) REFERENCES `usuario_final` (`USUARIO_FINAL_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historico_activo_usuario`
--

LOCK TABLES `historico_activo_usuario` WRITE;
/*!40000 ALTER TABLE `historico_activo_usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `historico_activo_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historico_herramienta_consumible`
--

DROP TABLE IF EXISTS `historico_herramienta_consumible`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historico_herramienta_consumible` (
  `HISTORICO_HERRAMIENTA_CONSUMIBLE_ID` decimal(10,0) NOT NULL,
  `FECHA_CONSUMO` date NOT NULL,
  `ACTIVO_ID` decimal(10,0) NOT NULL,
  PRIMARY KEY (`HISTORICO_HERRAMIENTA_CONSUMIBLE_ID`),
  KEY `FK_HISTORICO_HERRAMIENTA_CONSUMIBLE_HERRAMIENTA_CONSUMIBLE` (`ACTIVO_ID`),
  CONSTRAINT `FK_HISTORICO_HERRAMIENTA_CONSUMIBLE_HERRAMIENTA_CONSUMIBLE` FOREIGN KEY (`ACTIVO_ID`) REFERENCES `herramienta_consumible` (`ACTIVO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historico_herramienta_consumible`
--

LOCK TABLES `historico_herramienta_consumible` WRITE;
/*!40000 ALTER TABLE `historico_herramienta_consumible` DISABLE KEYS */;
/*!40000 ALTER TABLE `historico_herramienta_consumible` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libro`
--

DROP TABLE IF EXISTS `libro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libro` (
  `ACTIVO_ID` decimal(10,0) NOT NULL,
  `EDITORIAL` varchar(40) DEFAULT NULL,
  `EDICION` varchar(40) DEFAULT NULL,
  `ANIO` decimal(4,0) DEFAULT NULL,
  `AUTOR` varchar(500) NOT NULL,
  PRIMARY KEY (`ACTIVO_ID`),
  CONSTRAINT `FK_LIBRO_ACTIVO` FOREIGN KEY (`ACTIVO_ID`) REFERENCES `activo` (`ACTIVO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libro`
--

LOCK TABLES `libro` WRITE;
/*!40000 ALTER TABLE `libro` DISABLE KEYS */;
/*!40000 ALTER TABLE `libro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marca`
--

DROP TABLE IF EXISTS `marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marca` (
  `MARCA_ID` decimal(5,0) NOT NULL,
  `NOMBRE` varchar(11) NOT NULL,
  PRIMARY KEY (`MARCA_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marca`
--

LOCK TABLES `marca` WRITE;
/*!40000 ALTER TABLE `marca` DISABLE KEYS */;
/*!40000 ALTER TABLE `marca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `microprocesador`
--

DROP TABLE IF EXISTS `microprocesador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `microprocesador` (
  `MICROPROCESADOR_ID` decimal(10,0) NOT NULL,
  `NOMBRE` varchar(35) NOT NULL,
  `ARQUITECTURA` varchar(10) NOT NULL,
  `GENERACION` varchar(20) NOT NULL,
  `MARCA` decimal(5,0) NOT NULL,
  PRIMARY KEY (`MICROPROCESADOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `microprocesador`
--

LOCK TABLES `microprocesador` WRITE;
/*!40000 ALTER TABLE `microprocesador` DISABLE KEYS */;
/*!40000 ALTER TABLE `microprocesador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modelo`
--

DROP TABLE IF EXISTS `modelo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modelo` (
  `MODELO_ID` decimal(11,0) NOT NULL,
  `NOMBRE` varchar(30) NOT NULL,
  `IMAGEN` varchar(100) NOT NULL,
  `MARCA_ID` decimal(5,0) NOT NULL,
  PRIMARY KEY (`MODELO_ID`),
  KEY `FK_MODELO_MARCA` (`MARCA_ID`),
  CONSTRAINT `FK_MODELO_MARCA` FOREIGN KEY (`MARCA_ID`) REFERENCES `marca` (`MARCA_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modelo`
--

LOCK TABLES `modelo` WRITE;
/*!40000 ALTER TABLE `modelo` DISABLE KEYS */;
/*!40000 ALTER TABLE `modelo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proyector_tv`
--

DROP TABLE IF EXISTS `proyector_tv`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proyector_tv` (
  `ACTIVO_ID` decimal(10,0) NOT NULL,
  `VGA` decimal(1,0) NOT NULL,
  `HDMI` decimal(1,0) NOT NULL,
  `USB` decimal(1,0) NOT NULL,
  `ETHERNET` decimal(1,0) NOT NULL,
  `CONTROL_REMOTO` varchar(2) NOT NULL,
  PRIMARY KEY (`ACTIVO_ID`),
  CONSTRAINT `FK_PROYECTOR_TV_ACTIVO` FOREIGN KEY (`ACTIVO_ID`) REFERENCES `activo` (`ACTIVO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proyector_tv`
--

LOCK TABLES `proyector_tv` WRITE;
/*!40000 ALTER TABLE `proyector_tv` DISABLE KEYS */;
/*!40000 ALTER TABLE `proyector_tv` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ram`
--

DROP TABLE IF EXISTS `ram`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ram` (
  `RAM_ID` decimal(10,0) NOT NULL,
  `MARCA` varchar(40) NOT NULL,
  `NUM_SERIE` varchar(40) NOT NULL,
  `TIPO` varchar(5) NOT NULL,
  `CAPACIDAD` decimal(3,0) NOT NULL,
  PRIMARY KEY (`RAM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ram`
--

LOCK TABLES `ram` WRITE;
/*!40000 ALTER TABLE `ram` DISABLE KEYS */;
/*!40000 ALTER TABLE `ram` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `responsable_interno`
--

DROP TABLE IF EXISTS `responsable_interno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `responsable_interno` (
  `RESPONSABLE_INTERNO_ID` decimal(10,0) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `AP_PATERNO` varchar(50) NOT NULL,
  `AP_MATERNO` varchar(50) NOT NULL,
  `NUM_TRB` decimal(7,0) NOT NULL,
  `RFC` varchar(15) NOT NULL,
  `TELEFONO` decimal(12,0) NOT NULL,
  `CORREO` varchar(70) NOT NULL,
  `DEPARTAMENTO_ID` decimal(3,0) NOT NULL,
  `TITULO_ID` decimal(5,0) NOT NULL,
  PRIMARY KEY (`RESPONSABLE_INTERNO_ID`),
  KEY `FK_RESPONSABLE_INTERNO_DEPARTAMENTO` (`DEPARTAMENTO_ID`),
  KEY `FK_RESPONSABLE_INTERNO_TITULO` (`TITULO_ID`),
  CONSTRAINT `FK_RESPONSABLE_INTERNO_DEPARTAMENTO` FOREIGN KEY (`DEPARTAMENTO_ID`) REFERENCES `departamento` (`DEPARTAMENTO_ID`),
  CONSTRAINT `FK_RESPONSABLE_INTERNO_TITULO` FOREIGN KEY (`TITULO_ID`) REFERENCES `titulo` (`TITULO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `responsable_interno`
--

LOCK TABLES `responsable_interno` WRITE;
/*!40000 ALTER TABLE `responsable_interno` DISABLE KEYS */;
/*!40000 ALTER TABLE `responsable_interno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `responsable_resguardo`
--

DROP TABLE IF EXISTS `responsable_resguardo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `responsable_resguardo` (
  `RESPONSABLE_RESGUARDO_ID` decimal(10,0) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `AP_PATERNO` varchar(50) NOT NULL,
  `AP_MATERNO` varchar(50) NOT NULL,
  `NUM_TRB` decimal(7,0) NOT NULL,
  `RFC` varchar(15) NOT NULL,
  `TELEFONO` decimal(12,0) NOT NULL,
  `CORREO` varchar(70) NOT NULL,
  `DEPARTAMENTO_ID` decimal(3,0) NOT NULL,
  `TITULO_ID` decimal(5,0) NOT NULL,
  PRIMARY KEY (`RESPONSABLE_RESGUARDO_ID`),
  KEY `FK_RESPONSABLE_RESGUARDO_DEPARTAMENTO` (`DEPARTAMENTO_ID`),
  KEY `FK_RESPONSABLE_RESGUARDO_TITULO` (`TITULO_ID`),
  CONSTRAINT `FK_RESPONSABLE_RESGUARDO_DEPARTAMENTO` FOREIGN KEY (`DEPARTAMENTO_ID`) REFERENCES `departamento` (`DEPARTAMENTO_ID`),
  CONSTRAINT `FK_RESPONSABLE_RESGUARDO_TITULO` FOREIGN KEY (`TITULO_ID`) REFERENCES `titulo` (`TITULO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `responsable_resguardo`
--

LOCK TABLES `responsable_resguardo` WRITE;
/*!40000 ALTER TABLE `responsable_resguardo` DISABLE KEYS */;
/*!40000 ALTER TABLE `responsable_resguardo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sector`
--

DROP TABLE IF EXISTS `sector`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sector` (
  `SECTOR_ID` decimal(5,0) NOT NULL,
  `NOMBRE` varchar(40) NOT NULL,
  PRIMARY KEY (`SECTOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sector`
--

LOCK TABLES `sector` WRITE;
/*!40000 ALTER TABLE `sector` DISABLE KEYS */;
/*!40000 ALTER TABLE `sector` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema_operativo`
--

DROP TABLE IF EXISTS `sistema_operativo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema_operativo` (
  `SISTEMA_OPERATIVO_ID` decimal(5,0) NOT NULL,
  `VERSION` varchar(40) NOT NULL,
  `ARQUITECTURA` varchar(15) NOT NULL,
  `TIPO_SO_ID` decimal(6,0) NOT NULL,
  PRIMARY KEY (`SISTEMA_OPERATIVO_ID`),
  KEY `FK_SISTEMA_OPERATIVO_TIPO_SO` (`TIPO_SO_ID`),
  CONSTRAINT `FK_SISTEMA_OPERATIVO_TIPO_SO` FOREIGN KEY (`TIPO_SO_ID`) REFERENCES `tipo_so` (`TIPO_SO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema_operativo`
--

LOCK TABLES `sistema_operativo` WRITE;
/*!40000 ALTER TABLE `sistema_operativo` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema_operativo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_so`
--

DROP TABLE IF EXISTS `tipo_so`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_so` (
  `TIPO_SO_ID` decimal(6,0) NOT NULL,
  `NOMBRE` varchar(40) NOT NULL,
  PRIMARY KEY (`TIPO_SO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_so`
--

LOCK TABLES `tipo_so` WRITE;
/*!40000 ALTER TABLE `tipo_so` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_so` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `titulo`
--

DROP TABLE IF EXISTS `titulo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `titulo` (
  `TITULO_ID` decimal(5,0) NOT NULL,
  `NOMBRE` varchar(60) NOT NULL,
  `ABREVIATURA` varchar(10) NOT NULL,
  PRIMARY KEY (`TITULO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `titulo`
--

LOCK TABLES `titulo` WRITE;
/*!40000 ALTER TABLE `titulo` DISABLE KEYS */;
/*!40000 ALTER TABLE `titulo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ubicacion`
--

DROP TABLE IF EXISTS `ubicacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ubicacion` (
  `UBICACION_ID` decimal(10,0) NOT NULL,
  `PISO` varchar(5) DEFAULT NULL,
  `NOMBRE` varchar(150) NOT NULL,
  `CUBICULO` varchar(10) DEFAULT NULL,
  `CORREO` varchar(60) DEFAULT NULL,
  `TELEFONO` decimal(12,0) DEFAULT NULL,
  `EDIFICIO_ID` decimal(5,0) NOT NULL,
  PRIMARY KEY (`UBICACION_ID`),
  KEY `FK_UBICACION_EDIFICIO` (`EDIFICIO_ID`),
  CONSTRAINT `FK_UBICACION_EDIFICIO` FOREIGN KEY (`EDIFICIO_ID`) REFERENCES `edificio` (`EDIFICIO_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ubicacion`
--

LOCK TABLES `ubicacion` WRITE;
/*!40000 ALTER TABLE `ubicacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `ubicacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_final`
--

DROP TABLE IF EXISTS `usuario_final`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_final` (
  `USUARIO_FINAL_ID` decimal(10,0) NOT NULL,
  `NOMBRE` decimal(5,0) NOT NULL,
  `SECTOR_ID` decimal(5,0) NOT NULL,
  `PERFIL` decimal(10,0) NOT NULL,
  PRIMARY KEY (`USUARIO_FINAL_ID`),
  KEY `FK_USUARIO_FINAL_SECTOR` (`SECTOR_ID`),
  CONSTRAINT `FK_USUARIO_FINAL_SECTOR` FOREIGN KEY (`SECTOR_ID`) REFERENCES `sector` (`SECTOR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_final`
--

LOCK TABLES `usuario_final` WRITE;
/*!40000 ALTER TABLE `usuario_final` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario_final` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-01 11:56:59
