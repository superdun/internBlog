/*
Navicat MySQL Data Transfer

Source Server         : 1
Source Server Version : 50549
Source Host           : localhost:3306
Source Database       : internBlog

Target Server Type    : MYSQL
Target Server Version : 50549
File Encoding         : 65001

Date: 2016-07-01 14:47:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT '',
  `department` varchar(255) DEFAULT NULL,
  `team` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;
SET FOREIGN_KEY_CHECKS=1;
