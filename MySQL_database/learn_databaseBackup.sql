-- MySQL dump 10.13  Distrib 5.7.22, for Win64 (x86_64)
--
-- Host: localhost    Database: learn
-- ------------------------------------------------------
-- Server version	5.7.22-log

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
-- Current Database: `learn`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `learn` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `learn`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add area',7,'add_area'),(26,'Can change area',7,'change_area'),(27,'Can delete area',7,'delete_area'),(28,'Can view area',7,'view_area'),(29,'Can add bbs section',8,'add_bbssection'),(30,'Can change bbs section',8,'change_bbssection'),(31,'Can delete bbs section',8,'delete_bbssection'),(32,'Can view bbs section',8,'view_bbssection'),(33,'Can add comp class',9,'add_compclass'),(34,'Can change comp class',9,'change_compclass'),(35,'Can delete comp class',9,'delete_compclass'),(36,'Can view comp class',9,'view_compclass'),(37,'Can add comp info',10,'add_compinfo'),(38,'Can change comp info',10,'change_compinfo'),(39,'Can delete comp info',10,'delete_compinfo'),(40,'Can view comp info',10,'view_compinfo'),(41,'Can add comp record',11,'add_comprecord'),(42,'Can change comp record',11,'change_comprecord'),(43,'Can delete comp record',11,'delete_comprecord'),(44,'Can view comp record',11,'view_comprecord'),(45,'Can add user message',12,'add_usermessage'),(46,'Can change user message',12,'change_usermessage'),(47,'Can delete user message',12,'delete_usermessage'),(48,'Can view user message',12,'view_usermessage'),(49,'Can add mark message',13,'add_markmessage'),(50,'Can change mark message',13,'change_markmessage'),(51,'Can delete mark message',13,'delete_markmessage'),(52,'Can view mark message',13,'view_markmessage'),(53,'Can add bbs topic',14,'add_bbstopic'),(54,'Can change bbs topic',14,'change_bbstopic'),(55,'Can delete bbs topic',14,'delete_bbstopic'),(56,'Can view bbs topic',14,'view_bbstopic'),(57,'Can add bbs reply',15,'add_bbsreply'),(58,'Can change bbs reply',15,'change_bbsreply'),(59,'Can delete bbs reply',15,'delete_bbsreply'),(60,'Can view bbs reply',15,'view_bbsreply');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$2QZDXAxLdgOP$GFLonHuXOVZUhfV5q94XHf0NpcKaZpTmSJqFtahBCnU=',NULL,0,'xzh121','','','1432564581@qq.com',0,1,'2019-09-04 08:20:38.855872'),(2,'pbkdf2_sha256$150000$F9X9iCd4VMiB$CgQeGHL6DMJq6NRRQZ+WJvwrtY3kXpBZS7uJA8PJhnY=',NULL,0,'xzh131','','','1432564581@qq.com',0,1,'2019-09-04 08:21:53.244355'),(3,'pbkdf2_sha256$150000$4urm4hfjlLMk$Q0fHh7jjPQ88L4bixYPtOnLSlDgYBFPRJc7exHYYfmY=',NULL,0,'xzh141','','','1432564581@qq.com',0,1,'2019-09-04 08:25:32.876741'),(4,'pbkdf2_sha256$150000$kx6wQg4rheLh$SMt8sQQoE4ZnCl+D6XctxBG2qcqUCk4XDVyI6nfe7Es=',NULL,0,'xzh151','','','1432564581@qq.com',0,1,'2019-09-04 08:27:40.590060'),(5,'pbkdf2_sha256$150000$xP33l9vvpNYT$JDP3TRU6kXP9bEwBhoqO+4z2UBGEQ6hvcYiqPiIuVTs=',NULL,0,'xzh161','','','1432564581@qq.com',0,1,'2019-09-04 08:34:19.600533'),(6,'pbkdf2_sha256$150000$4WUCUOvA1cwv$HRLnxsWEtfNDHpQLkMQW3zjbX9tcbJKlOrkJ+F5q2jM=',NULL,0,'xzh112','','','1432564581@qq.com',0,1,'2019-09-04 08:39:04.537040'),(7,'pbkdf2_sha256$150000$e87I7pJzu0Lx$KCtvpz1Oq6Rag3R8o0+P+1mamOAamzjxKLTcjPGTq48=',NULL,0,'xzh113','','','1432564581@qq.com',0,1,'2019-09-04 08:40:51.729352'),(8,'pbkdf2_sha256$150000$xtOqww5S8z1D$F10Y40OuoU1hXp6yk0iZJ0Pz410gC1hRB8p3tre4RF0=',NULL,0,'xzhsg1','','','1432564581@qq.com',0,1,'2019-09-04 09:06:07.686213');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_area`
--

DROP TABLE IF EXISTS `backend_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backend_area` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(5) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_area`
--

LOCK TABLES `backend_area` WRITE;
/*!40000 ALTER TABLE `backend_area` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_bbsreply`
--

DROP TABLE IF EXISTS `backend_bbsreply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backend_bbsreply` (
  `Rid` int(11) NOT NULL AUTO_INCREMENT,
  `RTime` date NOT NULL,
  `RContent` longtext NOT NULL,
  `RLevelNum` smallint(5) unsigned NOT NULL,
  `RSid_id` int(11) NOT NULL,
  `RTid_id` int(11) NOT NULL,
  `RUid_id` int(11) NOT NULL,
  PRIMARY KEY (`Rid`),
  KEY `backend_bbsreply_RSid_id_41e718d2_fk_backend_bbssection_Sid` (`RSid_id`),
  KEY `backend_bbsreply_RTid_id_52795aa2_fk_backend_bbstopic_Tid` (`RTid_id`),
  KEY `backend_bbsreply_RUid_id_10e52513_fk_backend_usermessage_id` (`RUid_id`),
  CONSTRAINT `backend_bbsreply_RSid_id_41e718d2_fk_backend_bbssection_Sid` FOREIGN KEY (`RSid_id`) REFERENCES `backend_bbssection` (`Sid`),
  CONSTRAINT `backend_bbsreply_RTid_id_52795aa2_fk_backend_bbstopic_Tid` FOREIGN KEY (`RTid_id`) REFERENCES `backend_bbstopic` (`Tid`),
  CONSTRAINT `backend_bbsreply_RUid_id_10e52513_fk_backend_usermessage_id` FOREIGN KEY (`RUid_id`) REFERENCES `backend_usermessage` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_bbsreply`
--

LOCK TABLES `backend_bbsreply` WRITE;
/*!40000 ALTER TABLE `backend_bbsreply` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_bbsreply` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_bbssection`
--

DROP TABLE IF EXISTS `backend_bbssection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backend_bbssection` (
  `Sid` int(11) NOT NULL AUTO_INCREMENT,
  `SName` varchar(10) NOT NULL,
  `SStatement` varchar(200) NOT NULL,
  `SClickCount` smallint(5) unsigned NOT NULL,
  `SRepCount` smallint(5) unsigned NOT NULL,
  `STopicCount` smallint(5) unsigned NOT NULL,
  `SClassId_id` int(11) NOT NULL,
  PRIMARY KEY (`Sid`),
  KEY `backend_bbssection_SClassId_id_a81b07d2_fk_backend_compclass_Cid` (`SClassId_id`),
  CONSTRAINT `backend_bbssection_SClassId_id_a81b07d2_fk_backend_compclass_Cid` FOREIGN KEY (`SClassId_id`) REFERENCES `backend_compclass` (`Cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_bbssection`
--

LOCK TABLES `backend_bbssection` WRITE;
/*!40000 ALTER TABLE `backend_bbssection` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_bbssection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_bbstopic`
--

DROP TABLE IF EXISTS `backend_bbstopic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backend_bbstopic` (
  `Tid` int(11) NOT NULL AUTO_INCREMENT,
  `TReplyCount` smallint(5) unsigned NOT NULL,
  `TTopic` varchar(50) NOT NULL,
  `TContents` longtext,
  `TClickCount` smallint(5) unsigned NOT NULL,
  `TTime` date NOT NULL,
  `TLastClickT` date NOT NULL,
  `TSid_id` int(11) NOT NULL,
  `TUid_id` int(11) NOT NULL,
  PRIMARY KEY (`Tid`),
  KEY `backend_bbstopic_TSid_id_583e1ad5_fk_backend_bbssection_Sid` (`TSid_id`),
  KEY `backend_bbstopic_TUid_id_5a1af97d_fk_backend_usermessage_id` (`TUid_id`),
  CONSTRAINT `backend_bbstopic_TSid_id_583e1ad5_fk_backend_bbssection_Sid` FOREIGN KEY (`TSid_id`) REFERENCES `backend_bbssection` (`Sid`),
  CONSTRAINT `backend_bbstopic_TUid_id_5a1af97d_fk_backend_usermessage_id` FOREIGN KEY (`TUid_id`) REFERENCES `backend_usermessage` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_bbstopic`
--

LOCK TABLES `backend_bbstopic` WRITE;
/*!40000 ALTER TABLE `backend_bbstopic` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_bbstopic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_compclass`
--

DROP TABLE IF EXISTS `backend_compclass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backend_compclass` (
  `Cid` int(11) NOT NULL AUTO_INCREMENT,
  `CName` varchar(10) NOT NULL,
  `CStatement` varchar(100) DEFAULT NULL,
  `CCount` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`Cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_compclass`
--

LOCK TABLES `backend_compclass` WRITE;
/*!40000 ALTER TABLE `backend_compclass` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_compclass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_compinfo`
--

DROP TABLE IF EXISTS `backend_compinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backend_compinfo` (
  `Iid` int(11) NOT NULL AUTO_INCREMENT,
  `IName` varchar(60) NOT NULL,
  `IApplyStartTime` date NOT NULL,
  `IApplyEndTime` date NOT NULL,
  `IOrganizers` varchar(100) NOT NULL,
  `IObject` longtext NOT NULL,
  `IMethods` longtext NOT NULL,
  `ISchedule` longtext NOT NULL,
  `IStatement` longtext NOT NULL,
  `Iurls` varchar(200) NOT NULL,
  `IAreaID_id` int(11) NOT NULL,
  `IClass_id` int(11) NOT NULL,
  PRIMARY KEY (`Iid`),
  KEY `backend_compinfo_IAreaID_id_3aa5e5fc_fk_backend_area_ID` (`IAreaID_id`),
  KEY `backend_compinfo_IClass_id_34433cc4_fk_backend_compclass_Cid` (`IClass_id`),
  CONSTRAINT `backend_compinfo_IAreaID_id_3aa5e5fc_fk_backend_area_ID` FOREIGN KEY (`IAreaID_id`) REFERENCES `backend_area` (`ID`),
  CONSTRAINT `backend_compinfo_IClass_id_34433cc4_fk_backend_compclass_Cid` FOREIGN KEY (`IClass_id`) REFERENCES `backend_compclass` (`Cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_compinfo`
--

LOCK TABLES `backend_compinfo` WRITE;
/*!40000 ALTER TABLE `backend_compinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_compinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_comprecord`
--

DROP TABLE IF EXISTS `backend_comprecord`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backend_comprecord` (
  `RID` int(11) NOT NULL AUTO_INCREMENT,
  `RTitle` varchar(60) NOT NULL,
  `RStatement` varchar(100) NOT NULL,
  `RTime` date NOT NULL,
  `RClickCount` smallint(5) unsigned NOT NULL,
  `RMarkCount` smallint(5) unsigned NOT NULL,
  `RClassID_id` int(11) NOT NULL,
  `RContentID_id` int(11) NOT NULL,
  `RPromulgatorID_id` int(11) NOT NULL,
  PRIMARY KEY (`RID`),
  UNIQUE KEY `RContentID_id` (`RContentID_id`),
  KEY `backend_comprecord_RClassID_id_c8e29e31_fk_backend_compclass_Cid` (`RClassID_id`),
  KEY `backend_comprecord_RPromulgatorID_id_020a0d2f_fk_backend_u` (`RPromulgatorID_id`),
  CONSTRAINT `backend_comprecord_RClassID_id_c8e29e31_fk_backend_compclass_Cid` FOREIGN KEY (`RClassID_id`) REFERENCES `backend_compclass` (`Cid`),
  CONSTRAINT `backend_comprecord_RContentID_id_80850178_fk_backend_c` FOREIGN KEY (`RContentID_id`) REFERENCES `backend_compinfo` (`Iid`),
  CONSTRAINT `backend_comprecord_RPromulgatorID_id_020a0d2f_fk_backend_u` FOREIGN KEY (`RPromulgatorID_id`) REFERENCES `backend_usermessage` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_comprecord`
--

LOCK TABLES `backend_comprecord` WRITE;
/*!40000 ALTER TABLE `backend_comprecord` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_comprecord` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_markmessage`
--

DROP TABLE IF EXISTS `backend_markmessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backend_markmessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `MarkTime` date NOT NULL,
  `CompRecordId_id` int(11) NOT NULL,
  `UsersId_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `backend_markmessage_CompRecordId_id_f49cf79b_fk_backend_c` (`CompRecordId_id`),
  KEY `backend_markmessage_UsersId_id_68d570e1_fk_backend_u` (`UsersId_id`),
  CONSTRAINT `backend_markmessage_CompRecordId_id_f49cf79b_fk_backend_c` FOREIGN KEY (`CompRecordId_id`) REFERENCES `backend_comprecord` (`RID`),
  CONSTRAINT `backend_markmessage_UsersId_id_68d570e1_fk_backend_u` FOREIGN KEY (`UsersId_id`) REFERENCES `backend_usermessage` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_markmessage`
--

LOCK TABLES `backend_markmessage` WRITE;
/*!40000 ALTER TABLE `backend_markmessage` DISABLE KEYS */;
/*!40000 ALTER TABLE `backend_markmessage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backend_usermessage`
--

DROP TABLE IF EXISTS `backend_usermessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backend_usermessage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `UBirthday` date DEFAULT NULL,
  `USex` varchar(2) DEFAULT NULL,
  `UStatement` varchar(150) DEFAULT NULL,
  `Unickname` varchar(10) NOT NULL,
  `UPostCount` smallint(5) unsigned NOT NULL,
  `URepCount` smallint(5) unsigned NOT NULL,
  `UserBase_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UserBase_id` (`UserBase_id`),
  CONSTRAINT `backend_usermessage_UserBase_id_96b45a5c_fk_auth_user_id` FOREIGN KEY (`UserBase_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backend_usermessage`
--

LOCK TABLES `backend_usermessage` WRITE;
/*!40000 ALTER TABLE `backend_usermessage` DISABLE KEYS */;
INSERT INTO `backend_usermessage` VALUES (1,NULL,'','','',0,0,2),(2,NULL,'','','',0,0,3),(3,NULL,'','','',0,0,4),(4,NULL,'','','',0,0,5),(5,NULL,'','','',0,0,6),(6,NULL,'','','',0,0,7),(7,NULL,'','','',0,0,8);
/*!40000 ALTER TABLE `backend_usermessage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'backend','area'),(15,'backend','bbsreply'),(8,'backend','bbssection'),(14,'backend','bbstopic'),(9,'backend','compclass'),(10,'backend','compinfo'),(11,'backend','comprecord'),(13,'backend','markmessage'),(12,'backend','usermessage'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-09-04 08:19:14.207149'),(2,'auth','0001_initial','2019-09-04 08:19:14.399631'),(3,'admin','0001_initial','2019-09-04 08:19:14.934820'),(4,'admin','0002_logentry_remove_auto_add','2019-09-04 08:19:15.066137'),(5,'admin','0003_logentry_add_action_flag_choices','2019-09-04 08:19:15.078104'),(6,'contenttypes','0002_remove_content_type_name','2019-09-04 08:19:15.180829'),(7,'auth','0002_alter_permission_name_max_length','2019-09-04 08:19:15.198781'),(8,'auth','0003_alter_user_email_max_length','2019-09-04 08:19:15.225708'),(9,'auth','0004_alter_user_username_opts','2019-09-04 08:19:15.237680'),(10,'auth','0005_alter_user_last_login_null','2019-09-04 08:19:15.290534'),(11,'auth','0006_require_contenttypes_0002','2019-09-04 08:19:15.294523'),(12,'auth','0007_alter_validators_add_error_messages','2019-09-04 08:19:15.308487'),(13,'auth','0008_alter_user_username_max_length','2019-09-04 08:19:15.342395'),(14,'auth','0009_alter_user_last_name_max_length','2019-09-04 08:19:15.365333'),(15,'auth','0010_alter_group_name_max_length','2019-09-04 08:19:15.397247'),(16,'auth','0011_update_proxy_permissions','2019-09-04 08:19:15.408218'),(17,'backend','0001_initial','2019-09-04 08:19:15.942785'),(18,'sessions','0001_initial','2019-09-04 08:19:16.817958');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-09-04 17:39:38
