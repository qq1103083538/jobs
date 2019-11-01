
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for app_edu
-- ----------------------------
DROP TABLE IF EXISTS `app_edu`;
CREATE TABLE `app_edu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `graduate_start_time` datetime(6) DEFAULT NULL,
  `graduate_end_time` datetime(6) DEFAULT NULL,
  `major` varchar(32) NOT NULL,
  `colleges` varchar(32) NOT NULL,
  `education` int(11) NOT NULL,
  `degree` int(11) NOT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_edu_uid_id_3872feef_fk_app_user_id` (`uid_id`),
  CONSTRAINT `app_edu_uid_id_3872feef_fk_app_user_id` FOREIGN KEY (`uid_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_edu
-- ----------------------------
BEGIN;
INSERT INTO `app_edu` VALUES (1, '清华大学', '2017-09-01 00:00:00.000000', '2020-06-30 00:00:00.000000', '人工智能', '计算机系', 2, 3, 2);
INSERT INTO `app_edu` VALUES (2, '北京大学', '2019-11-01 00:00:00.000000', '2019-11-01 00:00:00.000000', '电子商务', '经管系', 7, 3, 5);
COMMIT;

-- ----------------------------
-- Table structure for app_educationinfo
-- ----------------------------
DROP TABLE IF EXISTS `app_educationinfo`;
CREATE TABLE `app_educationinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `graduate_school` varchar(200) NOT NULL,
  `graduate_time` datetime(6) NOT NULL,
  `education_type` varchar(100) NOT NULL,
  `degree` varchar(100) NOT NULL,
  `education` varchar(100) NOT NULL,
  `institutions` varchar(100) NOT NULL,
  `professional` varchar(100) NOT NULL,
  `work_experience` varchar(100) NOT NULL,
  `username_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_educationinfo_username_id_70f25521_fk_app_user_id` (`username_id`),
  CONSTRAINT `app_educationinfo_username_id_70f25521_fk_app_user_id` FOREIGN KEY (`username_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for app_enroll
-- ----------------------------
DROP TABLE IF EXISTS `app_enroll`;
CREATE TABLE `app_enroll` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `major_id` int(11) NOT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_enroll_major_id_78ed1335_fk_app_majorsecond_id` (`major_id`),
  KEY `app_enroll_uid_id_9c5a18b6_fk_app_user_id` (`uid_id`),
  CONSTRAINT `app_enroll_major_id_78ed1335_fk_app_majorsecond_id` FOREIGN KEY (`major_id`) REFERENCES `app_majorsecond` (`id`),
  CONSTRAINT `app_enroll_uid_id_9c5a18b6_fk_app_user_id` FOREIGN KEY (`uid_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_enroll
-- ----------------------------
BEGIN;
INSERT INTO `app_enroll` VALUES (1, 1, '2019-11-01 16:19:52.178057', '2019-11-01 16:19:52.178057', 3, 2);
INSERT INTO `app_enroll` VALUES (2, 1, '2019-11-01 19:29:34.901700', '2019-11-01 19:29:34.901737', 3, 5);
INSERT INTO `app_enroll` VALUES (3, 1, '2019-11-01 20:26:29.729011', '2019-11-01 20:26:29.729060', 3, 6);
COMMIT;

-- ----------------------------
-- Table structure for app_honour
-- ----------------------------
DROP TABLE IF EXISTS `app_honour`;
CREATE TABLE `app_honour` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `obtain_time` datetime(6) DEFAULT NULL,
  `level` int(11) NOT NULL,
  `extra` varchar(255) DEFAULT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_honour_uid_id_a19962e4_fk_app_user_id` (`uid_id`),
  CONSTRAINT `app_honour_uid_id_a19962e4_fk_app_user_id` FOREIGN KEY (`uid_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_honour
-- ----------------------------
BEGIN;
INSERT INTO `app_honour` VALUES (1, '荣誉奖章123', '2019-10-04 00:00:00.000000', 1, '/upload/img/2_1572501647_2_of_clubs.png#@#/upload/img/2_1572501691_3_of_diamonds.png', 2);
INSERT INTO `app_honour` VALUES (2, '职称/职鉴2', '2019-10-31 00:00:00.000000', 1, '/upload/img/2_1572526523_cancel-off.png', 2);
INSERT INTO `app_honour` VALUES (3, '职称/职鉴333', '2019-10-31 00:00:00.000000', 1, '/upload/img/2_1572526599_cancel-on.png', 2);
COMMIT;

-- ----------------------------
-- Table structure for app_majorclass
-- ----------------------------
DROP TABLE IF EXISTS `app_majorclass`;
CREATE TABLE `app_majorclass` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(16) NOT NULL,
  `weight` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_majorclass
-- ----------------------------
BEGIN;
INSERT INTO `app_majorclass` VALUES (1, '市场', 1, 1, '2019-11-01 01:13:56.018735', '2019-11-01 01:13:56.018762');
INSERT INTO `app_majorclass` VALUES (2, '技术', 1, 1, '2019-11-01 01:14:06.198856', '2019-11-01 01:14:06.198886');
COMMIT;

-- ----------------------------
-- Table structure for app_majorfirst
-- ----------------------------
DROP TABLE IF EXISTS `app_majorfirst`;
CREATE TABLE `app_majorfirst` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(16) NOT NULL,
  `weight` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `major_class_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_majorfirst_major_class_id_411c6927_fk_app_majorclass_id` (`major_class_id`),
  CONSTRAINT `app_majorfirst_major_class_id_411c6927_fk_app_majorclass_id` FOREIGN KEY (`major_class_id`) REFERENCES `app_majorclass` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_majorfirst
-- ----------------------------
BEGIN;
INSERT INTO `app_majorfirst` VALUES (1, '产业互联网产品专业', 1, 1, '2019-11-01 01:14:23.799130', '2019-11-01 01:14:23.799169', 1);
INSERT INTO `app_majorfirst` VALUES (2, '市场营销', 1, 1, '2019-11-01 01:14:36.595323', '2019-11-01 01:14:36.595358', 1);
INSERT INTO `app_majorfirst` VALUES (3, '个人及家庭互联网产品专业', 1, 1, '2019-11-01 01:14:49.309412', '2019-11-01 01:14:49.309448', 1);
INSERT INTO `app_majorfirst` VALUES (4, '其他', 1, 1, '2019-11-01 01:15:00.729189', '2019-11-01 01:15:00.729215', 1);
INSERT INTO `app_majorfirst` VALUES (5, 'IT', 1, 1, '2019-11-01 01:15:15.309938', '2019-11-01 01:15:15.309989', 2);
INSERT INTO `app_majorfirst` VALUES (6, '运行与维护', 1, 1, '2019-11-01 01:15:29.461912', '2019-11-01 01:15:29.461965', 2);
INSERT INTO `app_majorfirst` VALUES (7, '网络建设', 1, 1, '2019-11-01 01:15:40.789700', '2019-11-01 01:15:40.789726', 2);
COMMIT;

-- ----------------------------
-- Table structure for app_majorsecond
-- ----------------------------
DROP TABLE IF EXISTS `app_majorsecond`;
CREATE TABLE `app_majorsecond` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(16) NOT NULL,
  `weight` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `declare_start_time` datetime(6) NOT NULL,
  `declare_end_time` datetime(6) NOT NULL,
  `review_start_time` datetime(6) NOT NULL,
  `review_end_time` datetime(6) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `major_first_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_majorsecond_major_first_id_d2129e53_fk_app_majorfirst_id` (`major_first_id`),
  CONSTRAINT `app_majorsecond_major_first_id_d2129e53_fk_app_majorfirst_id` FOREIGN KEY (`major_first_id`) REFERENCES `app_majorfirst` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_majorsecond
-- ----------------------------
BEGIN;
INSERT INTO `app_majorsecond` VALUES (1, '规划与架构', 1, 1, '2019-01-01 01:01:00.000000', '2019-01-07 01:01:00.000000', '2019-02-01 01:01:00.000000', '2019-02-07 01:02:00.000000', '2019-11-01 01:16:53.622364', '2019-11-01 01:16:53.622376', 5);
INSERT INTO `app_majorsecond` VALUES (2, '业务与需求', 1, 1, '2019-01-01 12:01:00.000000', '2019-01-07 12:01:00.000000', '2019-02-07 12:01:00.000000', '2019-03-07 12:02:00.000000', '2019-11-01 01:18:13.820655', '2019-11-01 01:18:13.820667', 5);
INSERT INTO `app_majorsecond` VALUES (3, '研发与测试', 1, 1, '2019-11-01 12:11:00.000000', '2019-11-07 12:11:00.000000', '2019-12-01 12:12:00.000000', '2019-12-07 12:12:00.000000', '2019-11-01 01:19:09.651061', '2019-11-01 01:19:09.651080', 5);
INSERT INTO `app_majorsecond` VALUES (4, '生产与运维', 1, 1, '2019-12-01 12:12:00.000000', '2019-12-07 12:12:00.000000', '2019-12-14 12:12:00.000000', '2019-12-20 12:12:00.000000', '2019-11-01 20:18:19.441770', '2019-11-01 20:18:19.441789', 5);
INSERT INTO `app_majorsecond` VALUES (5, '大数据与云计算', 1, 1, '2019-10-31 12:10:00.000000', '2019-11-03 12:11:00.000000', '2019-11-09 12:11:00.000000', '2019-11-19 12:11:00.000000', '2019-11-01 20:19:03.739638', '2019-11-01 20:19:03.739657', 5);
INSERT INTO `app_majorsecond` VALUES (6, '网络监控', 1, 1, '2019-11-01 12:11:00.000000', '2019-11-04 12:11:00.000000', '2019-11-05 12:11:00.000000', '2019-11-15 12:11:00.000000', '2019-11-01 20:19:54.281806', '2019-11-01 20:19:54.281821', 6);
INSERT INTO `app_majorsecond` VALUES (7, '核心网', 1, 1, '2019-11-01 12:11:00.000000', '2019-11-06 12:11:00.000000', '2019-11-07 12:11:00.000000', '2019-11-11 12:11:00.000000', '2019-11-01 20:20:23.841818', '2019-11-01 20:20:23.841830', 6);
INSERT INTO `app_majorsecond` VALUES (8, '移动无线网', 1, 1, '2019-10-01 01:11:00.000000', '2019-10-02 01:10:00.000000', '2019-10-03 01:10:00.000000', '2019-10-04 01:10:00.000000', '2019-11-01 20:21:02.342873', '2019-11-01 20:21:02.342892', 6);
INSERT INTO `app_majorsecond` VALUES (9, 'IT', 1, 1, '2019-11-01 12:11:00.000000', '2019-11-04 12:11:00.000000', '2019-11-05 12:11:00.000000', '2019-11-09 12:11:00.000000', '2019-11-01 20:21:36.693767', '2019-11-01 20:21:36.693781', 6);
INSERT INTO `app_majorsecond` VALUES (10, '应急与安全', 1, 1, '2019-11-01 03:11:00.000000', '2019-11-06 03:11:00.000000', '2019-11-07 03:11:00.000000', '2019-11-17 03:11:00.000000', '2019-11-01 20:22:10.644428', '2019-11-01 20:22:10.644454', 6);
INSERT INTO `app_majorsecond` VALUES (11, '动力配套、局房', 1, 1, '2019-10-31 01:10:00.000000', '2019-11-08 03:11:00.000000', '2019-11-15 02:11:00.000000', '2019-11-17 02:11:00.000000', '2019-11-01 20:22:47.495780', '2019-11-01 20:22:47.495798', 6);
INSERT INTO `app_majorsecond` VALUES (12, '建设管理与创新', 1, 1, '2019-11-01 12:11:00.000000', '2019-11-02 01:11:00.000000', '2019-11-05 09:11:00.000000', '2019-11-22 03:11:00.000000', '2019-11-01 20:23:17.049354', '2019-11-01 20:23:17.049379', 7);
INSERT INTO `app_majorsecond` VALUES (13, '网络承载与接入', 1, 1, '2019-10-30 05:10:00.000000', '2019-11-02 07:11:00.000000', '2019-11-05 09:11:00.000000', '2019-11-15 11:11:00.000000', '2019-11-01 20:23:51.426850', '2019-11-01 20:23:51.426877', 7);
INSERT INTO `app_majorsecond` VALUES (14, '支撑及其他', 1, 1, '2019-10-29 05:10:00.000000', '2019-11-07 10:11:00.000000', '2019-11-19 01:11:00.000000', '2019-11-29 06:11:00.000000', '2019-11-01 20:24:29.966658', '2019-11-01 20:24:29.966684', 7);
COMMIT;

-- ----------------------------
-- Table structure for app_mark
-- ----------------------------
DROP TABLE IF EXISTS `app_mark`;
CREATE TABLE `app_mark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `professional_certification_or_qualification` double NOT NULL,
  `thesis_works` double NOT NULL,
  `national_patent` double NOT NULL,
  `technological_innovation` double NOT NULL,
  `skills_competition` double NOT NULL,
  `honour` double NOT NULL,
  `professional` double NOT NULL,
  `edu` double NOT NULL,
  `uid_id` int(11) NOT NULL,
  `sum` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_mark_uid_id_b8ea3cd0_fk_app_user_id` (`uid_id`),
  CONSTRAINT `app_mark_uid_id_b8ea3cd0_fk_app_user_id` FOREIGN KEY (`uid_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_mark
-- ----------------------------
BEGIN;
INSERT INTO `app_mark` VALUES (1, 10, 20, 5, 20, 20, 10, 5, 10, 2, 100);
INSERT INTO `app_mark` VALUES (2, 0, 0, 0, 0, 0, 0, 0, 10, 5, 10);
INSERT INTO `app_mark` VALUES (3, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0);
COMMIT;

-- ----------------------------
-- Table structure for app_nationalpatent
-- ----------------------------
DROP TABLE IF EXISTS `app_nationalpatent`;
CREATE TABLE `app_nationalpatent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `obtain_time` datetime(6) DEFAULT NULL,
  `level` int(11) NOT NULL,
  `extra` varchar(255) DEFAULT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_nationalpatent_uid_id_3e059ca9_fk_app_user_id` (`uid_id`),
  CONSTRAINT `app_nationalpatent_uid_id_3e059ca9_fk_app_user_id` FOREIGN KEY (`uid_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_nationalpatent
-- ----------------------------
BEGIN;
INSERT INTO `app_nationalpatent` VALUES (1, '国家专利1', '2019-10-31 00:00:00.000000', 1, '/upload/img/2_1572498706_red_joker.png#@#/upload/img/2_1572498710_black_joker.png', 2);
COMMIT;

-- ----------------------------
-- Table structure for app_professional
-- ----------------------------
DROP TABLE IF EXISTS `app_professional`;
CREATE TABLE `app_professional` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `obtain_time` datetime(6) DEFAULT NULL,
  `level` int(11) NOT NULL,
  `extra` varchar(255) DEFAULT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_professional_uid_id_98f39c4d_fk_app_user_id` (`uid_id`),
  CONSTRAINT `app_professional_uid_id_98f39c4d_fk_app_user_id` FOREIGN KEY (`uid_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_professional
-- ----------------------------
BEGIN;
INSERT INTO `app_professional` VALUES (1, '职称/职鉴###', '2019-10-31 00:00:00.000000', 3, '/upload/img/2_1572527783_star-on.png', 2);
INSERT INTO `app_professional` VALUES (2, '职称/职鉴999', '2019-10-31 00:00:00.000000', 1, '', 2);
INSERT INTO `app_professional` VALUES (3, '职称/职鉴1212121', '2019-10-31 00:00:00.000000', 1, '', 2);
COMMIT;

-- ----------------------------
-- Table structure for app_professionalcertificationorqualification
-- ----------------------------
DROP TABLE IF EXISTS `app_professionalcertificationorqualification`;
CREATE TABLE `app_professionalcertificationorqualification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `obtain_time` datetime(6) DEFAULT NULL,
  `level` int(11) NOT NULL,
  `extra` varchar(255) DEFAULT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_professionalcert_uid_id_918df12e_fk_app_user_` (`uid_id`),
  CONSTRAINT `app_professionalcert_uid_id_918df12e_fk_app_user_` FOREIGN KEY (`uid_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_professionalcertificationorqualification
-- ----------------------------
BEGIN;
INSERT INTO `app_professionalcertificationorqualification` VALUES (1, '专业认证或资质', '2019-10-30 00:00:00.000000', 6, '/upload/img/2_1572447357_cancel-off.png', 2);
INSERT INTO `app_professionalcertificationorqualification` VALUES (2, '专业认证或资质2', '2019-10-30 00:00:00.000000', 1, '/upload/img/2_1572447357_cancel-off.png', 2);
INSERT INTO `app_professionalcertificationorqualification` VALUES (3, '专业认证或资质10', '2019-10-30 00:00:00.000000', 1, '/upload/img/2_1572447357_cancel-off.png', 2);
INSERT INTO `app_professionalcertificationorqualification` VALUES (4, '专业认证或资质10', '2019-10-30 00:00:00.000000', 1, '/upload/img/2_1572447357_cancel-off.png', 2);
INSERT INTO `app_professionalcertificationorqualification` VALUES (5, '专业认证或资质10', '2019-10-30 00:00:00.000000', 1, '/upload/img/2_1572447357_cancel-off.png', 2);
INSERT INTO `app_professionalcertificationorqualification` VALUES (6, '专业认证或资质10', '2019-10-30 00:00:00.000000', 1, '/upload/img/2_1572447357_cancel-off.png', 2);
INSERT INTO `app_professionalcertificationorqualification` VALUES (7, '专业认证或资质10', '2019-10-30 00:00:00.000000', 1, '/upload/img/2_1572447357_cancel-off.png', 2);
INSERT INTO `app_professionalcertificationorqualification` VALUES (8, '专业认证或资质31', '2019-10-31 00:00:00.000000', 1, '', 2);
COMMIT;

-- ----------------------------
-- Table structure for app_skillscompetition
-- ----------------------------
DROP TABLE IF EXISTS `app_skillscompetition`;
CREATE TABLE `app_skillscompetition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `obtain_time` datetime(6) DEFAULT NULL,
  `level` int(11) NOT NULL,
  `extra` varchar(255) DEFAULT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_skillscompetition_uid_id_22aefd47_fk_app_user_id` (`uid_id`),
  CONSTRAINT `app_skillscompetition_uid_id_22aefd47_fk_app_user_id` FOREIGN KEY (`uid_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_skillscompetition
-- ----------------------------
BEGIN;
INSERT INTO `app_skillscompetition` VALUES (1, '技能竞赛1', '2019-10-03 00:00:00.000000', 1, '/upload/img/2_1572500046_6_of_diamonds.png#@#/upload/img/2_1572500049_6_of_hearts.png', 2);
INSERT INTO `app_skillscompetition` VALUES (2, '技能竞赛3', '2019-09-01 00:00:00.000000', 3, '', 2);
INSERT INTO `app_skillscompetition` VALUES (3, '荣誉奖章99', '2019-08-02 00:00:00.000000', 4, '/upload/img/2_1572500631_2_of_clubs.png', 2);
INSERT INTO `app_skillscompetition` VALUES (4, '荣誉奖章#', '2019-07-31 00:00:00.000000', 2, '/upload/img/2_1572500720_2_of_hearts.png', 2);
COMMIT;

-- ----------------------------
-- Table structure for app_technologicalinnovation
-- ----------------------------
DROP TABLE IF EXISTS `app_technologicalinnovation`;
CREATE TABLE `app_technologicalinnovation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `obtain_time` datetime(6) DEFAULT NULL,
  `level` int(11) NOT NULL,
  `extra` varchar(255) DEFAULT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_technologicalinnovation_uid_id_722ea949_fk_app_user_id` (`uid_id`),
  CONSTRAINT `app_technologicalinnovation_uid_id_722ea949_fk_app_user_id` FOREIGN KEY (`uid_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_technologicalinnovation
-- ----------------------------
BEGIN;
INSERT INTO `app_technologicalinnovation` VALUES (1, '科技创新2', '2019-10-01 00:00:00.000000', 1, '/upload/img/2_1572499436_queen_of_spades.png#@#/upload/img/2_1572499442_queen_of_hearts.png', 2);
COMMIT;

-- ----------------------------
-- Table structure for app_thesisworks
-- ----------------------------
DROP TABLE IF EXISTS `app_thesisworks`;
CREATE TABLE `app_thesisworks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `obtain_time` datetime(6) DEFAULT NULL,
  `level` int(11) NOT NULL,
  `extra` varchar(255) DEFAULT NULL,
  `uid_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_thesisworks_uid_id_d90aca4a_fk_app_user_id` (`uid_id`),
  CONSTRAINT `app_thesisworks_uid_id_d90aca4a_fk_app_user_id` FOREIGN KEY (`uid_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_thesisworks
-- ----------------------------
BEGIN;
INSERT INTO `app_thesisworks` VALUES (1, '论文著作2', '2019-10-31 00:00:00.000000', 1, '/upload/img/2_1572497502_2_of_clubs.png#@#/upload/img/2_1572497505_2_of_spades.png', 2);
COMMIT;

-- ----------------------------
-- Table structure for app_user
-- ----------------------------
DROP TABLE IF EXISTS `app_user`;
CREATE TABLE `app_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(16) NOT NULL,
  `password` varchar(32) NOT NULL,
  `nickname` varchar(16) DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `birthday` datetime(6) DEFAULT NULL,
  `enter_the_employment_time` datetime(6) DEFAULT NULL,
  `household_register_province` varchar(32) DEFAULT NULL,
  `household_register_city` varchar(32) DEFAULT NULL,
  `live_province` varchar(32) DEFAULT NULL,
  `live_city` varchar(32) DEFAULT NULL,
  `live_district` varchar(32) DEFAULT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `work_unit` varchar(32) DEFAULT NULL,
  `department` varchar(32) DEFAULT NULL,
  `marriage_status` varchar(32) DEFAULT NULL,
  `politics` varchar(32) DEFAULT NULL,
  `globetrotters` varchar(32) DEFAULT NULL,
  `id_card` varchar(18) NOT NULL,
  `portrait` varchar(300) DEFAULT NULL,
  `salt` varchar(36) NOT NULL,
  `type` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of app_user
-- ----------------------------
BEGIN;
INSERT INTO `app_user` VALUES (1, 'admin', '734ba5e4b85be86b6ba6da81d3c14396', '', 'male', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', '', NULL, NULL, NULL, NULL, NULL, '', '', '89534254-fb14-11e9-9b6b-3af9d3902217', 2, 1, '2019-10-30 20:55:23.372768', '2019-10-30 20:55:23.372818');
INSERT INTO `app_user` VALUES (2, 'a12345', '478795f472b72b01e4f354e426cd37b6', '德玛西亚', 'female', '2000-12-12 00:00:00.000000', '2019-10-30 00:00:00.000000', '美国', '锤子', 'LOL', '德玛西亚', '艾欧尼亚', '13111111111', '1@1.com', '拳头', '电竞', '未婚', '无党派人士', '有', '', '/upload/img/2_1572596929_2_of_hearts.png', 'cc654682-fb14-11e9-9b6b-3af9d3902217', 1, 1, '2019-10-30 20:57:15.916158', '2019-11-01 16:28:55.848709');
INSERT INTO `app_user` VALUES (3, 'a123456', 'f27ac715b16fa635ea9249d7e2306411', '', 'male', NULL, NULL, '', '', '', '', '', '', '', '', '', '未婚', '群众', '无', '', '', 'df881d34-fc81-11e9-9bb3-b8975a7447c3', 1, 1, '2019-11-01 16:30:34.331109', '2019-11-01 16:30:34.331109');
INSERT INTO `app_user` VALUES (4, 'b12345', '6dde2d837dca9eb801465e4112ad618f', '', 'male', NULL, NULL, '', '', '', '', '', '', '', '', '', '未婚', '群众', '无', '', '', 'e9904d48-fc99-11e9-9802-3af9d3902217', 1, 1, '2019-11-01 19:22:39.078980', '2019-11-01 19:22:39.079019');
INSERT INTO `app_user` VALUES (5, 'c123123', '3409ec6461b57465537545ed8c07fcf3', 'b123123', 'male', '2000-01-01 00:00:00.000000', '2019-11-01 00:00:00.000000', '北京', '北京', '北京', '北京', '北京', '13111111111', 'q@q.com', '腾讯', '天美', '未婚', '团员', '有', '', '/upload/img/5_1572607793_2.png', 'ae478a0c-fc9a-11e9-92b6-3af9d3902217', 1, 1, '2019-11-01 19:28:09.113044', '2019-11-01 19:29:56.981569');
INSERT INTO `app_user` VALUES (6, 'd12345', '22caaaf95ef8dfe9b175c1568cdc7e81', 'd1234', 'male', '2019-11-01 00:00:00.000000', '2019-11-01 00:00:00.000000', '湖南', '长沙市', '湖南省', '长沙市', '天心区', '13111111111', 'q@q.com', '草花互动', '研发', '未婚', '群众', '无', '', '/upload/img/6_1572611228_1.png', 'a2b87360-fca2-11e9-9f37-3af9d3902217', 1, 1, '2019-11-01 20:25:05.687466', '2019-11-01 20:27:12.029304');
COMMIT;

-- ----------------------------
-- Table structure for app_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `app_userinfo`;
CREATE TABLE `app_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `photo` varchar(100) NOT NULL,
  `nick` varchar(16) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `birth_time` datetime(6) NOT NULL,
  `id_card` varchar(18) NOT NULL,
  `political_landscape` varchar(20) NOT NULL,
  `native_place` varchar(20) NOT NULL,
  `work_units` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `username_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_userinfo_username_id_d1c4d112_fk_app_user_id` (`username_id`),
  CONSTRAINT `app_userinfo_username_id_d1c4d112_fk_app_user_id` FOREIGN KEY (`username_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (5, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (8, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (9, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (10, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (11, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (12, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (17, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (18, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (19, 'Can add user', 7, 'add_user');
INSERT INTO `auth_permission` VALUES (20, 'Can change user', 7, 'change_user');
INSERT INTO `auth_permission` VALUES (21, 'Can delete user', 7, 'delete_user');
INSERT INTO `auth_permission` VALUES (22, 'Can add edu', 8, 'add_edu');
INSERT INTO `auth_permission` VALUES (23, 'Can change edu', 8, 'change_edu');
INSERT INTO `auth_permission` VALUES (24, 'Can delete edu', 8, 'delete_edu');
INSERT INTO `auth_permission` VALUES (25, 'Can add professional', 9, 'add_professional');
INSERT INTO `auth_permission` VALUES (26, 'Can change professional', 9, 'change_professional');
INSERT INTO `auth_permission` VALUES (27, 'Can delete professional', 9, 'delete_professional');
INSERT INTO `auth_permission` VALUES (28, 'Can add honour', 10, 'add_honour');
INSERT INTO `auth_permission` VALUES (29, 'Can change honour', 10, 'change_honour');
INSERT INTO `auth_permission` VALUES (30, 'Can delete honour', 10, 'delete_honour');
INSERT INTO `auth_permission` VALUES (31, 'Can add skills competition', 11, 'add_skillscompetition');
INSERT INTO `auth_permission` VALUES (32, 'Can change skills competition', 11, 'change_skillscompetition');
INSERT INTO `auth_permission` VALUES (33, 'Can delete skills competition', 11, 'delete_skillscompetition');
INSERT INTO `auth_permission` VALUES (34, 'Can add technological innovation', 12, 'add_technologicalinnovation');
INSERT INTO `auth_permission` VALUES (35, 'Can change technological innovation', 12, 'change_technologicalinnovation');
INSERT INTO `auth_permission` VALUES (36, 'Can delete technological innovation', 12, 'delete_technologicalinnovation');
INSERT INTO `auth_permission` VALUES (37, 'Can add national patent', 13, 'add_nationalpatent');
INSERT INTO `auth_permission` VALUES (38, 'Can change national patent', 13, 'change_nationalpatent');
INSERT INTO `auth_permission` VALUES (39, 'Can delete national patent', 13, 'delete_nationalpatent');
INSERT INTO `auth_permission` VALUES (40, 'Can add thesis works', 14, 'add_thesisworks');
INSERT INTO `auth_permission` VALUES (41, 'Can change thesis works', 14, 'change_thesisworks');
INSERT INTO `auth_permission` VALUES (42, 'Can delete thesis works', 14, 'delete_thesisworks');
INSERT INTO `auth_permission` VALUES (43, 'Can add professional certification or qualification', 15, 'add_professionalcertificationorqualification');
INSERT INTO `auth_permission` VALUES (44, 'Can change professional certification or qualification', 15, 'change_professionalcertificationorqualification');
INSERT INTO `auth_permission` VALUES (45, 'Can delete professional certification or qualification', 15, 'delete_professionalcertificationorqualification');
INSERT INTO `auth_permission` VALUES (46, 'Can add user info', 16, 'add_userinfo');
INSERT INTO `auth_permission` VALUES (47, 'Can change user info', 16, 'change_userinfo');
INSERT INTO `auth_permission` VALUES (48, 'Can delete user info', 16, 'delete_userinfo');
INSERT INTO `auth_permission` VALUES (49, 'Can add education info', 17, 'add_educationinfo');
INSERT INTO `auth_permission` VALUES (50, 'Can change education info', 17, 'change_educationinfo');
INSERT INTO `auth_permission` VALUES (51, 'Can delete education info', 17, 'delete_educationinfo');
INSERT INTO `auth_permission` VALUES (52, 'Can add major class', 18, 'add_majorclass');
INSERT INTO `auth_permission` VALUES (53, 'Can change major class', 18, 'change_majorclass');
INSERT INTO `auth_permission` VALUES (54, 'Can delete major class', 18, 'delete_majorclass');
INSERT INTO `auth_permission` VALUES (55, 'Can add major first', 19, 'add_majorfirst');
INSERT INTO `auth_permission` VALUES (56, 'Can change major first', 19, 'change_majorfirst');
INSERT INTO `auth_permission` VALUES (57, 'Can delete major first', 19, 'delete_majorfirst');
INSERT INTO `auth_permission` VALUES (58, 'Can add major second', 20, 'add_majorsecond');
INSERT INTO `auth_permission` VALUES (59, 'Can change major second', 20, 'change_majorsecond');
INSERT INTO `auth_permission` VALUES (60, 'Can delete major second', 20, 'delete_majorsecond');
INSERT INTO `auth_permission` VALUES (61, 'Can add mark', 21, 'add_mark');
INSERT INTO `auth_permission` VALUES (62, 'Can change mark', 21, 'change_mark');
INSERT INTO `auth_permission` VALUES (63, 'Can delete mark', 21, 'delete_mark');
INSERT INTO `auth_permission` VALUES (64, 'Can add enroll', 22, 'add_enroll');
INSERT INTO `auth_permission` VALUES (65, 'Can change enroll', 22, 'change_enroll');
INSERT INTO `auth_permission` VALUES (66, 'Can delete enroll', 22, 'delete_enroll');
COMMIT;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (8, 'app', 'edu');
INSERT INTO `django_content_type` VALUES (17, 'app', 'educationinfo');
INSERT INTO `django_content_type` VALUES (22, 'app', 'enroll');
INSERT INTO `django_content_type` VALUES (10, 'app', 'honour');
INSERT INTO `django_content_type` VALUES (18, 'app', 'majorclass');
INSERT INTO `django_content_type` VALUES (19, 'app', 'majorfirst');
INSERT INTO `django_content_type` VALUES (20, 'app', 'majorsecond');
INSERT INTO `django_content_type` VALUES (21, 'app', 'mark');
INSERT INTO `django_content_type` VALUES (13, 'app', 'nationalpatent');
INSERT INTO `django_content_type` VALUES (9, 'app', 'professional');
INSERT INTO `django_content_type` VALUES (15, 'app', 'professionalcertificationorqualification');
INSERT INTO `django_content_type` VALUES (11, 'app', 'skillscompetition');
INSERT INTO `django_content_type` VALUES (12, 'app', 'technologicalinnovation');
INSERT INTO `django_content_type` VALUES (14, 'app', 'thesisworks');
INSERT INTO `django_content_type` VALUES (7, 'app', 'user');
INSERT INTO `django_content_type` VALUES (16, 'app', 'userinfo');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
COMMIT;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
BEGIN;
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2019-10-30 20:53:07.681185');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2019-10-30 20:53:10.377536');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2019-10-30 20:53:11.069801');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2019-10-30 20:53:11.311649');
INSERT INTO `django_migrations` VALUES (5, 'contenttypes', '0002_remove_content_type_name', '2019-10-30 20:53:11.922722');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0002_alter_permission_name_max_length', '2019-10-30 20:53:12.314667');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0003_alter_user_email_max_length', '2019-10-30 20:53:12.825129');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0004_alter_user_username_opts', '2019-10-30 20:53:13.070559');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0005_alter_user_last_login_null', '2019-10-30 20:53:13.424040');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0006_require_contenttypes_0002', '2019-10-30 20:53:13.665347');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0007_alter_validators_add_error_messages', '2019-10-30 20:53:13.898740');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0008_alter_user_username_max_length', '2019-10-30 20:53:14.468089');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0009_alter_user_last_name_max_length', '2019-10-30 20:53:14.872438');
INSERT INTO `django_migrations` VALUES (14, 'sessions', '0001_initial', '2019-10-30 20:53:15.358934');
INSERT INTO `django_migrations` VALUES (15, 'app', '0001_initial', '2019-10-30 20:54:32.048261');
INSERT INTO `django_migrations` VALUES (16, 'app', '0002_auto_20191030_2100', '2019-10-30 21:00:47.374638');
INSERT INTO `django_migrations` VALUES (17, 'app', '0003_auto_20191030_2123', '2019-10-30 21:23:59.557758');
INSERT INTO `django_migrations` VALUES (18, 'app', '0004_auto_20191030_2300', '2019-10-30 23:00:07.183060');
INSERT INTO `django_migrations` VALUES (19, 'app', '0005_auto_20191031_1254', '2019-10-31 12:54:55.219398');
INSERT INTO `django_migrations` VALUES (20, 'app', '0006_auto_20191031_1258', '2019-10-31 12:58:58.029976');
INSERT INTO `django_migrations` VALUES (21, 'app', '0007_auto_20191031_1316', '2019-10-31 13:16:43.196738');
INSERT INTO `django_migrations` VALUES (22, 'app', '0008_auto_20191031_1335', '2019-10-31 13:35:36.539399');
INSERT INTO `django_migrations` VALUES (23, 'app', '0009_auto_20191031_2106', '2019-10-31 21:06:39.302328');
INSERT INTO `django_migrations` VALUES (24, 'app', '0010_auto_20191031_2333', '2019-10-31 23:33:31.235660');
INSERT INTO `django_migrations` VALUES (25, 'app', '0011_enroll', '2019-11-01 01:34:22.454225');
INSERT INTO `django_migrations` VALUES (26, 'app', '0012_auto_20191101_2028', '2019-11-01 20:28:40.100710');
COMMIT;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
