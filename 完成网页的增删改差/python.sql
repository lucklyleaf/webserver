-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: jing_dong
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.16.04.1

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
-- Table structure for table `focus`
--

DROP TABLE IF EXISTS `focus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `focus` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `beizhu` varchar(50) DEFAULT NULL,
  `goods_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `focus`
--

LOCK TABLES `focus` WRITE;
/*!40000 ALTER TABLE `focus` DISABLE KEYS */;
INSERT INTO `focus` VALUES (20,'您好',2),(21,'大使馆的发',1),(25,'xcvcxzvxcvx',6),(26,NULL,3);
/*!40000 ALTER TABLE `focus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `cate_id` int(10) unsigned NOT NULL,
  `brand_id` int(10) unsigned NOT NULL,
  `price` decimal(10,3) NOT NULL DEFAULT '0.000',
  `is_now` bit(1) NOT NULL DEFAULT b'1',
  `is_saleoff` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`id`),
  KEY `cate_id` (`cate_id`),
  KEY `brand_id` (`brand_id`),
  CONSTRAINT `goods_ibfk_1` FOREIGN KEY (`cate_id`) REFERENCES `goods_cates` (`id`),
  CONSTRAINT `goods_ibfk_2` FOREIGN KEY (`brand_id`) REFERENCES `goods_brands` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES (1,'r510vc 15.6英寸笔记本',5,2,3399.000,_binary '',_binary '\0'),(2,'y400h 14.0英寸笔记本嗲电脑',5,7,4999.000,_binary '',_binary '\0'),(3,'g150th 15.6英寸笔记本嗲电脑',4,9,8499.000,_binary '',_binary '\0'),(4,'x550cc 15.6英寸笔记本',5,2,2799.000,_binary '',_binary '\0'),(5,'x240 超级本',7,7,4880.000,_binary '',_binary '\0'),(6,'u330p 13.3英寸超级本',7,7,4299.000,_binary '',_binary '\0'),(7,'svp13226scb 触控笔记本',7,6,7999.000,_binary '',_binary '\0'),(8,'ipad mini 7.9英寸平本电脑',2,8,1998.000,_binary '',_binary '\0'),(9,'ipad air 9.7英寸平板电脑',2,8,3388.000,_binary '',_binary '\0'),(10,'ipad mini 配备retina显示屏',2,8,2788.000,_binary '',_binary '\0'),(11,'ideacentre c340 20英寸一体电脑',1,7,3499.000,_binary '',_binary '\0'),(12,'vostro 3800-r1206 台式电脑',1,5,2899.000,_binary '',_binary '\0'),(13,'ipad air 9.7英寸平板电脑',2,8,3388.000,_binary '',_binary '\0'),(14,'imac me086ch/a 21.5英寸一体电脑',1,8,9188.000,_binary '',_binary '\0'),(15,'at7-7414lp 台式电脑 linux',1,3,3699.000,_binary '',_binary '\0'),(16,'z220sff f4f06pa工作站',3,4,4288.000,_binary '',_binary '\0'),(17,'poweredge li服务器',3,5,5388.000,_binary '',_binary '\0'),(18,'mac pro专业级台式电脑',3,8,28888.000,_binary '',_binary '\0'),(19,'hmz-t3w 头戴显示设备',6,6,6299.000,_binary '',_binary '\0'),(20,'商务双肩背包',6,6,99.000,_binary '',_binary '\0'),(21,'x3250 m4机架式服务器',3,1,6888.000,_binary '',_binary '\0'),(22,'商务双肩背包',6,6,99.000,_binary '',_binary '\0');
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_brands`
--

DROP TABLE IF EXISTS `goods_brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_brands` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_brands`
--

LOCK TABLES `goods_brands` WRITE;
/*!40000 ALTER TABLE `goods_brands` DISABLE KEYS */;
INSERT INTO `goods_brands` VALUES (1,'ibm'),(2,'华硕'),(3,'宏基'),(4,'惠普'),(5,'戴尔'),(6,'索尼'),(7,'联想'),(8,'苹果'),(9,'雷神'),(10,'硬盘'),(12,'外星人');
/*!40000 ALTER TABLE `goods_brands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_cates`
--

DROP TABLE IF EXISTS `goods_cates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_cates` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_cates`
--

LOCK TABLES `goods_cates` WRITE;
/*!40000 ALTER TABLE `goods_cates` DISABLE KEYS */;
INSERT INTO `goods_cates` VALUES (1,'台式机'),(2,'平板电脑'),(3,'服务器/工作站'),(4,'游戏本'),(5,'笔记本'),(6,'笔记本配件'),(7,'超级本'),(8,'路由器');
/*!40000 ALTER TABLE `goods_cates` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-27 10:10:19
