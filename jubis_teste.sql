CREATE DATABASE  IF NOT EXISTS `patrimonio` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `patrimonio`;
-- MySQL dump 10.13  Distrib 5.7.20, for Linux (x86_64)
--
-- Host: localhost    Database: patrimonio
-- ------------------------------------------------------
-- Server version	5.7.28-0ubuntu0.16.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bem`
--

DROP TABLE IF EXISTS `bem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bem` (
  `numero_patrimonio` int(11) NOT NULL,
  `descricao` tinytext,
  `sala` varchar(10) DEFAULT NULL,
  `verificado_por` varchar(15) DEFAULT NULL,
  `status` enum('Não encontrado','Bom','Ocioso','Inservivel') DEFAULT NULL,
  `verificado_em` datetime DEFAULT NULL,
  PRIMARY KEY (`numero_patrimonio`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bem`
--

LOCK TABLES `bem` WRITE;
/*!40000 ALTER TABLE `bem` DISABLE KEYS */;
INSERT INTO `bem` VALUES (1,'teste de insert',NULL,'caspar','Bom','2019-12-29 01:20:41'),(102,'Carteira','ddd','CHT','Inservivel','2020-01-03 01:37:17'),(109,'Carteira','V34','NULL','Não encontrado',NULL),(198,'Carteira','V32','NULL','Não encontrado',NULL),(919,'luminaria','V23','CHT','Não encontrado','2020-01-03 03:01:04'),(928,'Carteira','V23','NULL','Não encontrado',NULL),(2933,'luminaria','S23','NULL','Não encontrado',NULL),(3937,'Mesa','V23','NULL','Não encontrado',NULL),(9227,'Mesa','S23','NULL','Não encontrado',NULL),(9287,'Carteira','S23','NULL','Não encontrado',NULL),(9373,'Mesa','V32','NULL','Não encontrado',NULL),(9384,'Carteira','V32','NULL','Não encontrado',NULL),(9837,'Mesa','V34','NULL','Não encontrado',NULL),(9948,'luminaria','V32','NULL','Não encontrado',NULL),(83723,'luminaria','V34','NULL','Não encontrado',NULL),(84720,'luminaria','V32','NULL','Não encontrado',NULL),(84740,'Mesa','S23','NULL','Não encontrado',NULL),(928373,'Carteira','V34','NULL','Não encontrado',NULL);
/*!40000 ALTER TABLE `bem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `id` varchar(15) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `email` varchar(62) DEFAULT NULL,
  `senha` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES ('Cascao','Cascao sujinho','cascao@hun.co','$2b$12$0XGk9tha./ww3u./ffHrw.t76bmfDqepz1zNlg5Er9Zkg2AEPoyTy'),('Cebola','Cebola Cebolinha',NULL,'$2b$12$UTEfkVC3W.6dxC/eFyatVOIrwjxvPY/2xu5D52v0A.1sQClYIepem'),('CHT','carlos Tonhatti',NULL,'$2b$12$B54BNVM1GbH65U94JI9Dm.BHqLvrron9iN2RwmoYDzmgR3duMkJDe'),('franjinha','franjinha bidu','franjinha@nnh.com','$2b$12$LtKJKyMFy6FK3dqUfKi2tujr773kfvv.x27vD/nldqb5O4Q3Wtsey'),('Magali','Magali Melancia',NULL,'$2b$12$TGM797/9iLKOuUJjUCO0y.EuKhFmz7Zj42u0zw8y3y0fLJfN5.bEq'),('Monica','Monica Turma',NULL,'$2b$12$DI/SAKyfIrhJ/9Pdpxd/S.caDjsDOHNnyF/tvyBXa3iVW7N1omgca');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'patrimonio'
--

--
-- Dumping routines for database 'patrimonio'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-03 22:08:28
