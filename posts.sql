/*
Navicat MySQL Data Transfer

Source Server         : 1
Source Server Version : 50549
Source Host           : localhost:3306
Source Database       : internBlog

Target Server Type    : MYSQL
Target Server Version : 50549
File Encoding         : 65001

Date: 2016-07-01 14:47:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for posts
-- ----------------------------
DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `body` varchar(1000) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `authorId` int(11) DEFAULT NULL,
  `tmstmp` int(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=284 DEFAULT CHARSET=utf8;
SET FOREIGN_KEY_CHECKS=1;
