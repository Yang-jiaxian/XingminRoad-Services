/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : localhost:3306
 Source Schema         : xing_min_road_services

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 15/12/2022 18:37:34
*/

SET NAMES utf8mb4;
SET
FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for contact
-- ----------------------------
DROP TABLE IF EXISTS `contact`;
CREATE TABLE `contact`
(
    `id`                int(0) NOT NULL AUTO_INCREMENT COMMENT '联系记录ID',
    `customer_id`       int(0) NOT NULL COMMENT '客户ID',
    `contact_date`      date NULL DEFAULT NULL COMMENT '联系日期（拜访时间）',
    `contact_detail`    text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '联系详情（拜访内容）',
    `demand`            text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '需求',
    `next_contact_date` date NULL DEFAULT NULL COMMENT '预约下一次拜访时间',
    `remind_duration`   int(0) NOT NULL COMMENT '提醒时长',
    `remind_date`       date NULL DEFAULT NULL COMMENT '提醒日期',
    `main_appeal`       int(0) NULL DEFAULT NULL COMMENT '主要诉求',
    `operator_id`       int(0) NOT NULL COMMENT '登记人',
    `is_delete`         tinyint(0) NOT NULL DEFAULT 0 COMMENT '是否删除',
    `created_at`        datetime(0) NULL DEFAULT CURRENT_TIMESTAMP (0) COMMENT '创建时间',
    `updated_at`        datetime(0) NULL DEFAULT CURRENT_TIMESTAMP (0) ON UPDATE CURRENT_TIMESTAMP (0) COMMENT '更新时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '联系记录表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for cooperative_brokerage
-- ----------------------------
DROP TABLE IF EXISTS `cooperative_brokerage`;
CREATE TABLE `cooperative_brokerage`
(
    `id`                int(0) NOT NULL AUTO_INCREMENT COMMENT 'ID',
    `customer_id`       int(0) NOT NULL COMMENT '客户ID',
    `name`              varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '券商名称',
    `advantage_project` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '优势项目',
    `created_at`        datetime(0) NULL DEFAULT CURRENT_TIMESTAMP (0) COMMENT '创建时间',
    `updated_at`        datetime(0) NULL DEFAULT CURRENT_TIMESTAMP (0) ON UPDATE CURRENT_TIMESTAMP (0) COMMENT '更新时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '合作券商表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for customer
-- ----------------------------
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `capital_account` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT '0' COMMENT '个人客户时是资金账号，机构客户时是编号',
  `customer_type` tinyint(1) NOT NULL COMMENT '客户类型（0是个人客户，1是机构客户），默认个人客户',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '个人客户时是姓名，机构客户时是名称',
  `gender` tinyint(1) NULL DEFAULT NULL COMMENT '性别（0是男性，1是女性），机构客户时没有',
  `contact_person` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '联系人（机构客户时才有）',
  `phone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '联系方式',
  `occupation` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '职业',
  `birthday` date NULL DEFAULT NULL COMMENT '出生年月日',
  `certificate_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '证件类型',
  `certificate_number` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '证件号码',
  `existing_assets` float NULL DEFAULT NULL COMMENT '资产-现有资产',
  `historical_peak` float NULL DEFAULT NULL COMMENT '资产-历史峰值',
  `customer_source` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '客户情况-客户来源',
  `specific_channel` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '客户情况-具体渠道',
  `commission_rate` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '佣金费率',
  `risk_appetite` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '风险偏好',
  `contact_status` int(0) NULL DEFAULT 0 COMMENT '联系次数',
  `developer` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '开发关系（人名）',
  `is_internet_channel` tinyint(1) NULL DEFAULT NULL COMMENT '是否是互联网渠道',
  `assignmenter` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '服务包分配（人名）',
  `follower` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '跟进情况（人名）',
  `cash_treasure` tinyint(0) NULL DEFAULT 0 COMMENT '现金宝',
  `automatic_investment_plan` tinyint(0) NULL DEFAULT 0 COMMENT '基金定投',
  `double_innovation_board` tinyint(0) NULL DEFAULT 0 COMMENT '双创板',
  `share_option` tinyint(0) NULL DEFAULT 0 COMMENT '期权',
  `shenzhen_hong_kong_stock_connect` tinyint(0) NULL DEFAULT 0 COMMENT '深港通',
  `shanghai_hong_kong_stock_connect` tinyint(0) NULL DEFAULT 0 COMMENT '沪港通',
  `double_margin_account` tinyint(0) NULL DEFAULT 0 COMMENT '两融账户',
  `beijing_stock_exchange` tinyint(0) NULL DEFAULT 0 COMMENT '北交所',
  `pension_account` tinyint(0) NULL DEFAULT 0 COMMENT '养老金账户',
  `margin_account` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '融资融券-账号',
  `account_opening_date` date NULL DEFAULT NULL COMMENT '融资融券-开户日期',
  `preferential_interest_rate` float NULL DEFAULT NULL COMMENT '融资融券-优惠利率',
  `interest_rate_effective_date` date NULL DEFAULT NULL COMMENT '融资融券-利率生效日期',
  `interest_rate_expiry_date` date NULL DEFAULT NULL COMMENT '融资融券-利率失效日期',
  `interest_rate_expiry_remind_date` date NULL DEFAULT NULL COMMENT '融资融券-利率失效提醒日期',
  `remark` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '融资融券-备注',
  `operator_id` int(0) NULL DEFAULT NULL COMMENT '创建客户的操作人ID',
  `scale_of_management` char(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '管理规模',
  `private_placement_strategy` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '私募的策略类型',
  `fund_demand` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '资金需求',
  `technical_demand` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '技术需求',
  `bond_source_demand` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '券源需求',
  `investment_research_demand` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '投研需求',
  `is_delete` tinyint(0) NULL DEFAULT 0 COMMENT '是否删除',
  `created_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updated_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id`(`capital_account`, `margin_account`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '客户表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for fund
-- ----------------------------
DROP TABLE IF EXISTS `fund`;
CREATE TABLE `fund`
(
    `id`          int(0) NOT NULL AUTO_INCREMENT COMMENT '基金ID',
    `customer_id` int(0) NOT NULL COMMENT '客户ID',
    `name`        varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '购买产品',
    `amount`      float NULL DEFAULT NULL COMMENT '购买金额',
    `yield_rate`  float NULL DEFAULT NULL COMMENT '收益率',
    `buy_date`    date NULL DEFAULT NULL COMMENT '购买时间',
    `day_number`  int(0) NULL DEFAULT NULL COMMENT '产品天数',
    `due_date`    date NULL DEFAULT NULL COMMENT '到期日',
    `remind_date` date NULL DEFAULT NULL COMMENT '提醒日',
    `is_delete`   tinyint(0) NULL DEFAULT 0 COMMENT '是否删除',
    `created_at`  datetime(0) NULL DEFAULT CURRENT_TIMESTAMP (0) COMMENT '创建时间',
    `updated_at`  datetime(0) NULL DEFAULT CURRENT_TIMESTAMP (0) ON UPDATE CURRENT_TIMESTAMP (0) COMMENT '更新时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '基金理财、私募表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for log
-- ----------------------------
DROP TABLE IF EXISTS `log`;
CREATE TABLE `log`
(
    `id`          int(0) NOT NULL AUTO_INCREMENT COMMENT '日志ID',
    `operator_id` int(0) NOT NULL COMMENT '操作员ID',
    `detail`      text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '日志详情',
    `query`       text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '参数',
    `is_delete`   tinyint(0) NULL DEFAULT 0 COMMENT '是否删除',
    `created_at`  datetime(0) NULL DEFAULT CURRENT_TIMESTAMP (0) COMMENT '创建时间',
    `updated_at`  datetime(0) NULL DEFAULT CURRENT_TIMESTAMP (0) ON UPDATE CURRENT_TIMESTAMP (0) COMMENT '更新时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '操作日志表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for operator
-- ----------------------------
DROP TABLE IF EXISTS `operator`;
CREATE TABLE `operator`
(
    `id`         int(0) NOT NULL AUTO_INCREMENT COMMENT '操作员ID',
    `name`       varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '操作员',
    `phone`      varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '联系方式',
    `is_delete`  tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否删除',
    `created_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP (0) COMMENT '创建时间',
    `updated_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP (0) ON UPDATE CURRENT_TIMESTAMP (0) COMMENT '更新时间',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '操作员表' ROW_FORMAT = Dynamic;


-- ----------------------------
-- Records of operator
-- ----------------------------
INSERT INTO `operator`
VALUES (1, '测试', '13800138000', 0, '2022-12-14 15:43:24', '2022-12-14 15:43:24');


-- ----------------------------
-- Table structure for workday
-- ----------------------------
DROP TABLE IF EXISTS `workday`;
CREATE TABLE `workday`
(
    `date` date NULL DEFAULT NULL COMMENT '工作日日期'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of workday
-- ----------------------------
INSERT INTO `workday`
VALUES ('2022-01-04');
INSERT INTO `workday`
VALUES ('2022-01-05');
INSERT INTO `workday`
VALUES ('2022-01-06');
INSERT INTO `workday`
VALUES ('2022-01-07');
INSERT INTO `workday`
VALUES ('2022-01-10');
INSERT INTO `workday`
VALUES ('2022-01-11');
INSERT INTO `workday`
VALUES ('2022-01-12');
INSERT INTO `workday`
VALUES ('2022-01-13');
INSERT INTO `workday`
VALUES ('2022-01-14');
INSERT INTO `workday`
VALUES ('2022-01-17');
INSERT INTO `workday`
VALUES ('2022-01-18');
INSERT INTO `workday`
VALUES ('2022-01-19');
INSERT INTO `workday`
VALUES ('2022-01-20');
INSERT INTO `workday`
VALUES ('2022-01-21');
INSERT INTO `workday`
VALUES ('2022-01-24');
INSERT INTO `workday`
VALUES ('2022-01-25');
INSERT INTO `workday`
VALUES ('2022-01-26');
INSERT INTO `workday`
VALUES ('2022-01-27');
INSERT INTO `workday`
VALUES ('2022-01-28');
INSERT INTO `workday`
VALUES ('2022-01-29');
INSERT INTO `workday`
VALUES ('2022-01-30');
INSERT INTO `workday`
VALUES ('2022-02-07');
INSERT INTO `workday`
VALUES ('2022-02-08');
INSERT INTO `workday`
VALUES ('2022-02-09');
INSERT INTO `workday`
VALUES ('2022-02-10');
INSERT INTO `workday`
VALUES ('2022-02-11');
INSERT INTO `workday`
VALUES ('2022-02-14');
INSERT INTO `workday`
VALUES ('2022-02-15');
INSERT INTO `workday`
VALUES ('2022-02-16');
INSERT INTO `workday`
VALUES ('2022-02-17');
INSERT INTO `workday`
VALUES ('2022-02-18');
INSERT INTO `workday`
VALUES ('2022-02-21');
INSERT INTO `workday`
VALUES ('2022-02-22');
INSERT INTO `workday`
VALUES ('2022-02-23');
INSERT INTO `workday`
VALUES ('2022-02-24');
INSERT INTO `workday`
VALUES ('2022-02-25');
INSERT INTO `workday`
VALUES ('2022-02-28');
INSERT INTO `workday`
VALUES ('2022-03-01');
INSERT INTO `workday`
VALUES ('2022-03-02');
INSERT INTO `workday`
VALUES ('2022-03-03');
INSERT INTO `workday`
VALUES ('2022-03-04');
INSERT INTO `workday`
VALUES ('2022-03-07');
INSERT INTO `workday`
VALUES ('2022-03-08');
INSERT INTO `workday`
VALUES ('2022-03-09');
INSERT INTO `workday`
VALUES ('2022-03-10');
INSERT INTO `workday`
VALUES ('2022-03-11');
INSERT INTO `workday`
VALUES ('2022-03-14');
INSERT INTO `workday`
VALUES ('2022-03-15');
INSERT INTO `workday`
VALUES ('2022-03-16');
INSERT INTO `workday`
VALUES ('2022-03-17');
INSERT INTO `workday`
VALUES ('2022-03-18');
INSERT INTO `workday`
VALUES ('2022-03-21');
INSERT INTO `workday`
VALUES ('2022-03-22');
INSERT INTO `workday`
VALUES ('2022-03-23');
INSERT INTO `workday`
VALUES ('2022-03-24');
INSERT INTO `workday`
VALUES ('2022-03-25');
INSERT INTO `workday`
VALUES ('2022-03-28');
INSERT INTO `workday`
VALUES ('2022-03-29');
INSERT INTO `workday`
VALUES ('2022-03-30');
INSERT INTO `workday`
VALUES ('2022-03-31');
INSERT INTO `workday`
VALUES ('2022-04-01');
INSERT INTO `workday`
VALUES ('2022-04-02');
INSERT INTO `workday`
VALUES ('2022-04-06');
INSERT INTO `workday`
VALUES ('2022-04-07');
INSERT INTO `workday`
VALUES ('2022-04-08');
INSERT INTO `workday`
VALUES ('2022-04-11');
INSERT INTO `workday`
VALUES ('2022-04-12');
INSERT INTO `workday`
VALUES ('2022-04-13');
INSERT INTO `workday`
VALUES ('2022-04-14');
INSERT INTO `workday`
VALUES ('2022-04-15');
INSERT INTO `workday`
VALUES ('2022-04-18');
INSERT INTO `workday`
VALUES ('2022-04-19');
INSERT INTO `workday`
VALUES ('2022-04-20');
INSERT INTO `workday`
VALUES ('2022-04-21');
INSERT INTO `workday`
VALUES ('2022-04-22');
INSERT INTO `workday`
VALUES ('2022-04-24');
INSERT INTO `workday`
VALUES ('2022-04-25');
INSERT INTO `workday`
VALUES ('2022-04-26');
INSERT INTO `workday`
VALUES ('2022-04-27');
INSERT INTO `workday`
VALUES ('2022-04-28');
INSERT INTO `workday`
VALUES ('2022-04-29');
INSERT INTO `workday`
VALUES ('2022-05-05');
INSERT INTO `workday`
VALUES ('2022-05-06');
INSERT INTO `workday`
VALUES ('2022-05-07');
INSERT INTO `workday`
VALUES ('2022-05-09');
INSERT INTO `workday`
VALUES ('2022-05-10');
INSERT INTO `workday`
VALUES ('2022-05-11');
INSERT INTO `workday`
VALUES ('2022-05-12');
INSERT INTO `workday`
VALUES ('2022-05-13');
INSERT INTO `workday`
VALUES ('2022-05-16');
INSERT INTO `workday`
VALUES ('2022-05-17');
INSERT INTO `workday`
VALUES ('2022-05-18');
INSERT INTO `workday`
VALUES ('2022-05-19');
INSERT INTO `workday`
VALUES ('2022-05-20');
INSERT INTO `workday`
VALUES ('2022-05-23');
INSERT INTO `workday`
VALUES ('2022-05-24');
INSERT INTO `workday`
VALUES ('2022-05-25');
INSERT INTO `workday`
VALUES ('2022-05-26');
INSERT INTO `workday`
VALUES ('2022-05-27');
INSERT INTO `workday`
VALUES ('2022-05-30');
INSERT INTO `workday`
VALUES ('2022-05-31');
INSERT INTO `workday`
VALUES ('2022-06-01');
INSERT INTO `workday`
VALUES ('2022-06-02');
INSERT INTO `workday`
VALUES ('2022-06-06');
INSERT INTO `workday`
VALUES ('2022-06-07');
INSERT INTO `workday`
VALUES ('2022-06-08');
INSERT INTO `workday`
VALUES ('2022-06-09');
INSERT INTO `workday`
VALUES ('2022-06-10');
INSERT INTO `workday`
VALUES ('2022-06-13');
INSERT INTO `workday`
VALUES ('2022-06-14');
INSERT INTO `workday`
VALUES ('2022-06-15');
INSERT INTO `workday`
VALUES ('2022-06-16');
INSERT INTO `workday`
VALUES ('2022-06-17');
INSERT INTO `workday`
VALUES ('2022-06-20');
INSERT INTO `workday`
VALUES ('2022-06-21');
INSERT INTO `workday`
VALUES ('2022-06-22');
INSERT INTO `workday`
VALUES ('2022-06-23');
INSERT INTO `workday`
VALUES ('2022-06-24');
INSERT INTO `workday`
VALUES ('2022-06-27');
INSERT INTO `workday`
VALUES ('2022-06-28');
INSERT INTO `workday`
VALUES ('2022-06-29');
INSERT INTO `workday`
VALUES ('2022-06-30');
INSERT INTO `workday`
VALUES ('2022-07-01');
INSERT INTO `workday`
VALUES ('2022-07-04');
INSERT INTO `workday`
VALUES ('2022-07-05');
INSERT INTO `workday`
VALUES ('2022-07-06');
INSERT INTO `workday`
VALUES ('2022-07-07');
INSERT INTO `workday`
VALUES ('2022-07-08');
INSERT INTO `workday`
VALUES ('2022-07-11');
INSERT INTO `workday`
VALUES ('2022-07-12');
INSERT INTO `workday`
VALUES ('2022-07-13');
INSERT INTO `workday`
VALUES ('2022-07-14');
INSERT INTO `workday`
VALUES ('2022-07-15');
INSERT INTO `workday`
VALUES ('2022-07-18');
INSERT INTO `workday`
VALUES ('2022-07-19');
INSERT INTO `workday`
VALUES ('2022-07-20');
INSERT INTO `workday`
VALUES ('2022-07-21');
INSERT INTO `workday`
VALUES ('2022-07-22');
INSERT INTO `workday`
VALUES ('2022-07-25');
INSERT INTO `workday`
VALUES ('2022-07-26');
INSERT INTO `workday`
VALUES ('2022-07-27');
INSERT INTO `workday`
VALUES ('2022-07-28');
INSERT INTO `workday`
VALUES ('2022-07-29');
INSERT INTO `workday`
VALUES ('2022-08-01');
INSERT INTO `workday`
VALUES ('2022-08-02');
INSERT INTO `workday`
VALUES ('2022-08-03');
INSERT INTO `workday`
VALUES ('2022-08-04');
INSERT INTO `workday`
VALUES ('2022-08-05');
INSERT INTO `workday`
VALUES ('2022-08-08');
INSERT INTO `workday`
VALUES ('2022-08-09');
INSERT INTO `workday`
VALUES ('2022-08-10');
INSERT INTO `workday`
VALUES ('2022-08-11');
INSERT INTO `workday`
VALUES ('2022-08-12');
INSERT INTO `workday`
VALUES ('2022-08-15');
INSERT INTO `workday`
VALUES ('2022-08-16');
INSERT INTO `workday`
VALUES ('2022-08-17');
INSERT INTO `workday`
VALUES ('2022-08-18');
INSERT INTO `workday`
VALUES ('2022-08-19');
INSERT INTO `workday`
VALUES ('2022-08-22');
INSERT INTO `workday`
VALUES ('2022-08-23');
INSERT INTO `workday`
VALUES ('2022-08-24');
INSERT INTO `workday`
VALUES ('2022-08-25');
INSERT INTO `workday`
VALUES ('2022-08-26');
INSERT INTO `workday`
VALUES ('2022-08-29');
INSERT INTO `workday`
VALUES ('2022-08-30');
INSERT INTO `workday`
VALUES ('2022-08-31');
INSERT INTO `workday`
VALUES ('2022-09-01');
INSERT INTO `workday`
VALUES ('2022-09-02');
INSERT INTO `workday`
VALUES ('2022-09-05');
INSERT INTO `workday`
VALUES ('2022-09-06');
INSERT INTO `workday`
VALUES ('2022-09-07');
INSERT INTO `workday`
VALUES ('2022-09-08');
INSERT INTO `workday`
VALUES ('2022-09-09');
INSERT INTO `workday`
VALUES ('2022-09-13');
INSERT INTO `workday`
VALUES ('2022-09-14');
INSERT INTO `workday`
VALUES ('2022-09-15');
INSERT INTO `workday`
VALUES ('2022-09-16');
INSERT INTO `workday`
VALUES ('2022-09-19');
INSERT INTO `workday`
VALUES ('2022-09-20');
INSERT INTO `workday`
VALUES ('2022-09-21');
INSERT INTO `workday`
VALUES ('2022-09-22');
INSERT INTO `workday`
VALUES ('2022-09-23');
INSERT INTO `workday`
VALUES ('2022-09-26');
INSERT INTO `workday`
VALUES ('2022-09-27');
INSERT INTO `workday`
VALUES ('2022-09-28');
INSERT INTO `workday`
VALUES ('2022-09-29');
INSERT INTO `workday`
VALUES ('2022-09-30');
INSERT INTO `workday`
VALUES ('2022-10-08');
INSERT INTO `workday`
VALUES ('2022-10-09');
INSERT INTO `workday`
VALUES ('2022-10-10');
INSERT INTO `workday`
VALUES ('2022-10-11');
INSERT INTO `workday`
VALUES ('2022-10-12');
INSERT INTO `workday`
VALUES ('2022-10-13');
INSERT INTO `workday`
VALUES ('2022-10-14');
INSERT INTO `workday`
VALUES ('2022-10-17');
INSERT INTO `workday`
VALUES ('2022-10-18');
INSERT INTO `workday`
VALUES ('2022-10-19');
INSERT INTO `workday`
VALUES ('2022-10-20');
INSERT INTO `workday`
VALUES ('2022-10-21');
INSERT INTO `workday`
VALUES ('2022-10-24');
INSERT INTO `workday`
VALUES ('2022-10-25');
INSERT INTO `workday`
VALUES ('2022-10-26');
INSERT INTO `workday`
VALUES ('2022-10-27');
INSERT INTO `workday`
VALUES ('2022-10-28');
INSERT INTO `workday`
VALUES ('2022-10-31');
INSERT INTO `workday`
VALUES ('2022-11-01');
INSERT INTO `workday`
VALUES ('2022-11-02');
INSERT INTO `workday`
VALUES ('2022-11-03');
INSERT INTO `workday`
VALUES ('2022-11-04');
INSERT INTO `workday`
VALUES ('2022-11-07');
INSERT INTO `workday`
VALUES ('2022-11-08');
INSERT INTO `workday`
VALUES ('2022-11-09');
INSERT INTO `workday`
VALUES ('2022-11-10');
INSERT INTO `workday`
VALUES ('2022-11-11');
INSERT INTO `workday`
VALUES ('2022-11-14');
INSERT INTO `workday`
VALUES ('2022-11-15');
INSERT INTO `workday`
VALUES ('2022-11-16');
INSERT INTO `workday`
VALUES ('2022-11-17');
INSERT INTO `workday`
VALUES ('2022-11-18');
INSERT INTO `workday`
VALUES ('2022-11-21');
INSERT INTO `workday`
VALUES ('2022-11-22');
INSERT INTO `workday`
VALUES ('2022-11-23');
INSERT INTO `workday`
VALUES ('2022-11-24');
INSERT INTO `workday`
VALUES ('2022-11-25');
INSERT INTO `workday`
VALUES ('2022-11-28');
INSERT INTO `workday`
VALUES ('2022-11-29');
INSERT INTO `workday`
VALUES ('2022-11-30');
INSERT INTO `workday`
VALUES ('2022-12-01');
INSERT INTO `workday`
VALUES ('2022-12-02');
INSERT INTO `workday`
VALUES ('2022-12-05');
INSERT INTO `workday`
VALUES ('2022-12-06');
INSERT INTO `workday`
VALUES ('2022-12-07');
INSERT INTO `workday`
VALUES ('2022-12-08');
INSERT INTO `workday`
VALUES ('2022-12-09');
INSERT INTO `workday`
VALUES ('2022-12-12');
INSERT INTO `workday`
VALUES ('2022-12-13');
INSERT INTO `workday`
VALUES ('2022-12-14');
INSERT INTO `workday`
VALUES ('2022-12-15');
INSERT INTO `workday`
VALUES ('2022-12-16');
INSERT INTO `workday`
VALUES ('2022-12-19');
INSERT INTO `workday`
VALUES ('2022-12-20');
INSERT INTO `workday`
VALUES ('2022-12-21');
INSERT INTO `workday`
VALUES ('2022-12-22');
INSERT INTO `workday`
VALUES ('2022-12-23');
INSERT INTO `workday`
VALUES ('2022-12-26');
INSERT INTO `workday`
VALUES ('2022-12-27');
INSERT INTO `workday`
VALUES ('2022-12-28');
INSERT INTO `workday`
VALUES ('2022-12-29');
INSERT INTO `workday`
VALUES ('2022-12-30');
INSERT INTO `workday`
VALUES ('2023-01-03');
INSERT INTO `workday`
VALUES ('2023-01-04');
INSERT INTO `workday`
VALUES ('2023-01-05');
INSERT INTO `workday`
VALUES ('2023-01-06');
INSERT INTO `workday`
VALUES ('2023-01-09');
INSERT INTO `workday`
VALUES ('2023-01-10');
INSERT INTO `workday`
VALUES ('2023-01-11');
INSERT INTO `workday`
VALUES ('2023-01-12');
INSERT INTO `workday`
VALUES ('2023-01-13');
INSERT INTO `workday`
VALUES ('2023-01-16');
INSERT INTO `workday`
VALUES ('2023-01-17');
INSERT INTO `workday`
VALUES ('2023-01-18');
INSERT INTO `workday`
VALUES ('2023-01-19');
INSERT INTO `workday`
VALUES ('2023-01-20');
INSERT INTO `workday`
VALUES ('2023-01-28');
INSERT INTO `workday`
VALUES ('2023-01-29');
INSERT INTO `workday`
VALUES ('2023-01-30');
INSERT INTO `workday`
VALUES ('2023-01-31');
INSERT INTO `workday`
VALUES ('2023-02-01');
INSERT INTO `workday`
VALUES ('2023-02-02');
INSERT INTO `workday`
VALUES ('2023-02-03');
INSERT INTO `workday`
VALUES ('2023-02-06');
INSERT INTO `workday`
VALUES ('2023-02-07');
INSERT INTO `workday`
VALUES ('2023-02-08');
INSERT INTO `workday`
VALUES ('2023-02-09');
INSERT INTO `workday`
VALUES ('2023-02-10');
INSERT INTO `workday`
VALUES ('2023-02-13');
INSERT INTO `workday`
VALUES ('2023-02-14');
INSERT INTO `workday`
VALUES ('2023-02-15');
INSERT INTO `workday`
VALUES ('2023-02-16');
INSERT INTO `workday`
VALUES ('2023-02-17');
INSERT INTO `workday`
VALUES ('2023-02-20');
INSERT INTO `workday`
VALUES ('2023-02-21');
INSERT INTO `workday`
VALUES ('2023-02-22');
INSERT INTO `workday`
VALUES ('2023-02-23');
INSERT INTO `workday`
VALUES ('2023-02-24');
INSERT INTO `workday`
VALUES ('2023-02-27');
INSERT INTO `workday`
VALUES ('2023-02-28');
INSERT INTO `workday`
VALUES ('2023-03-01');
INSERT INTO `workday`
VALUES ('2023-03-02');
INSERT INTO `workday`
VALUES ('2023-03-03');
INSERT INTO `workday`
VALUES ('2023-03-06');
INSERT INTO `workday`
VALUES ('2023-03-07');
INSERT INTO `workday`
VALUES ('2023-03-08');
INSERT INTO `workday`
VALUES ('2023-03-09');
INSERT INTO `workday`
VALUES ('2023-03-10');
INSERT INTO `workday`
VALUES ('2023-03-13');
INSERT INTO `workday`
VALUES ('2023-03-14');
INSERT INTO `workday`
VALUES ('2023-03-15');
INSERT INTO `workday`
VALUES ('2023-03-16');
INSERT INTO `workday`
VALUES ('2023-03-17');
INSERT INTO `workday`
VALUES ('2023-03-20');
INSERT INTO `workday`
VALUES ('2023-03-21');
INSERT INTO `workday`
VALUES ('2023-03-22');
INSERT INTO `workday`
VALUES ('2023-03-23');
INSERT INTO `workday`
VALUES ('2023-03-24');
INSERT INTO `workday`
VALUES ('2023-03-27');
INSERT INTO `workday`
VALUES ('2023-03-28');
INSERT INTO `workday`
VALUES ('2023-03-29');
INSERT INTO `workday`
VALUES ('2023-03-30');
INSERT INTO `workday`
VALUES ('2023-03-31');
INSERT INTO `workday`
VALUES ('2023-04-03');
INSERT INTO `workday`
VALUES ('2023-04-04');
INSERT INTO `workday`
VALUES ('2023-04-06');
INSERT INTO `workday`
VALUES ('2023-04-07');
INSERT INTO `workday`
VALUES ('2023-04-10');
INSERT INTO `workday`
VALUES ('2023-04-11');
INSERT INTO `workday`
VALUES ('2023-04-12');
INSERT INTO `workday`
VALUES ('2023-04-13');
INSERT INTO `workday`
VALUES ('2023-04-14');
INSERT INTO `workday`
VALUES ('2023-04-17');
INSERT INTO `workday`
VALUES ('2023-04-18');
INSERT INTO `workday`
VALUES ('2023-04-19');
INSERT INTO `workday`
VALUES ('2023-04-20');
INSERT INTO `workday`
VALUES ('2023-04-21');
INSERT INTO `workday`
VALUES ('2023-04-23');
INSERT INTO `workday`
VALUES ('2023-04-24');
INSERT INTO `workday`
VALUES ('2023-04-25');
INSERT INTO `workday`
VALUES ('2023-04-26');
INSERT INTO `workday`
VALUES ('2023-04-27');
INSERT INTO `workday`
VALUES ('2023-04-28');
INSERT INTO `workday`
VALUES ('2023-05-04');
INSERT INTO `workday`
VALUES ('2023-05-05');
INSERT INTO `workday`
VALUES ('2023-05-06');
INSERT INTO `workday`
VALUES ('2023-05-08');
INSERT INTO `workday`
VALUES ('2023-05-09');
INSERT INTO `workday`
VALUES ('2023-05-10');
INSERT INTO `workday`
VALUES ('2023-05-11');
INSERT INTO `workday`
VALUES ('2023-05-12');
INSERT INTO `workday`
VALUES ('2023-05-15');
INSERT INTO `workday`
VALUES ('2023-05-16');
INSERT INTO `workday`
VALUES ('2023-05-17');
INSERT INTO `workday`
VALUES ('2023-05-18');
INSERT INTO `workday`
VALUES ('2023-05-19');
INSERT INTO `workday`
VALUES ('2023-05-22');
INSERT INTO `workday`
VALUES ('2023-05-23');
INSERT INTO `workday`
VALUES ('2023-05-24');
INSERT INTO `workday`
VALUES ('2023-05-25');
INSERT INTO `workday`
VALUES ('2023-05-26');
INSERT INTO `workday`
VALUES ('2023-05-29');
INSERT INTO `workday`
VALUES ('2023-05-30');
INSERT INTO `workday`
VALUES ('2023-05-31');
INSERT INTO `workday`
VALUES ('2023-06-01');
INSERT INTO `workday`
VALUES ('2023-06-02');
INSERT INTO `workday`
VALUES ('2023-06-05');
INSERT INTO `workday`
VALUES ('2023-06-06');
INSERT INTO `workday`
VALUES ('2023-06-07');
INSERT INTO `workday`
VALUES ('2023-06-08');
INSERT INTO `workday`
VALUES ('2023-06-09');
INSERT INTO `workday`
VALUES ('2023-06-12');
INSERT INTO `workday`
VALUES ('2023-06-13');
INSERT INTO `workday`
VALUES ('2023-06-14');
INSERT INTO `workday`
VALUES ('2023-06-15');
INSERT INTO `workday`
VALUES ('2023-06-16');
INSERT INTO `workday`
VALUES ('2023-06-19');
INSERT INTO `workday`
VALUES ('2023-06-20');
INSERT INTO `workday`
VALUES ('2023-06-21');
INSERT INTO `workday`
VALUES ('2023-06-25');
INSERT INTO `workday`
VALUES ('2023-06-26');
INSERT INTO `workday`
VALUES ('2023-06-27');
INSERT INTO `workday`
VALUES ('2023-06-28');
INSERT INTO `workday`
VALUES ('2023-06-29');
INSERT INTO `workday`
VALUES ('2023-06-30');
INSERT INTO `workday`
VALUES ('2023-07-03');
INSERT INTO `workday`
VALUES ('2023-07-04');
INSERT INTO `workday`
VALUES ('2023-07-05');
INSERT INTO `workday`
VALUES ('2023-07-06');
INSERT INTO `workday`
VALUES ('2023-07-07');
INSERT INTO `workday`
VALUES ('2023-07-10');
INSERT INTO `workday`
VALUES ('2023-07-11');
INSERT INTO `workday`
VALUES ('2023-07-12');
INSERT INTO `workday`
VALUES ('2023-07-13');
INSERT INTO `workday`
VALUES ('2023-07-14');
INSERT INTO `workday`
VALUES ('2023-07-17');
INSERT INTO `workday`
VALUES ('2023-07-18');
INSERT INTO `workday`
VALUES ('2023-07-19');
INSERT INTO `workday`
VALUES ('2023-07-20');
INSERT INTO `workday`
VALUES ('2023-07-21');
INSERT INTO `workday`
VALUES ('2023-07-24');
INSERT INTO `workday`
VALUES ('2023-07-25');
INSERT INTO `workday`
VALUES ('2023-07-26');
INSERT INTO `workday`
VALUES ('2023-07-27');
INSERT INTO `workday`
VALUES ('2023-07-28');
INSERT INTO `workday`
VALUES ('2023-07-31');
INSERT INTO `workday`
VALUES ('2023-08-01');
INSERT INTO `workday`
VALUES ('2023-08-02');
INSERT INTO `workday`
VALUES ('2023-08-03');
INSERT INTO `workday`
VALUES ('2023-08-04');
INSERT INTO `workday`
VALUES ('2023-08-07');
INSERT INTO `workday`
VALUES ('2023-08-08');
INSERT INTO `workday`
VALUES ('2023-08-09');
INSERT INTO `workday`
VALUES ('2023-08-10');
INSERT INTO `workday`
VALUES ('2023-08-11');
INSERT INTO `workday`
VALUES ('2023-08-14');
INSERT INTO `workday`
VALUES ('2023-08-15');
INSERT INTO `workday`
VALUES ('2023-08-16');
INSERT INTO `workday`
VALUES ('2023-08-17');
INSERT INTO `workday`
VALUES ('2023-08-18');
INSERT INTO `workday`
VALUES ('2023-08-21');
INSERT INTO `workday`
VALUES ('2023-08-22');
INSERT INTO `workday`
VALUES ('2023-08-23');
INSERT INTO `workday`
VALUES ('2023-08-24');
INSERT INTO `workday`
VALUES ('2023-08-25');
INSERT INTO `workday`
VALUES ('2023-08-28');
INSERT INTO `workday`
VALUES ('2023-08-29');
INSERT INTO `workday`
VALUES ('2023-08-30');
INSERT INTO `workday`
VALUES ('2023-08-31');
INSERT INTO `workday`
VALUES ('2023-09-01');
INSERT INTO `workday`
VALUES ('2023-09-04');
INSERT INTO `workday`
VALUES ('2023-09-05');
INSERT INTO `workday`
VALUES ('2023-09-06');
INSERT INTO `workday`
VALUES ('2023-09-07');
INSERT INTO `workday`
VALUES ('2023-09-08');
INSERT INTO `workday`
VALUES ('2023-09-11');
INSERT INTO `workday`
VALUES ('2023-09-12');
INSERT INTO `workday`
VALUES ('2023-09-13');
INSERT INTO `workday`
VALUES ('2023-09-14');
INSERT INTO `workday`
VALUES ('2023-09-15');
INSERT INTO `workday`
VALUES ('2023-09-18');
INSERT INTO `workday`
VALUES ('2023-09-19');
INSERT INTO `workday`
VALUES ('2023-09-20');
INSERT INTO `workday`
VALUES ('2023-09-21');
INSERT INTO `workday`
VALUES ('2023-09-22');
INSERT INTO `workday`
VALUES ('2023-09-25');
INSERT INTO `workday`
VALUES ('2023-09-26');
INSERT INTO `workday`
VALUES ('2023-09-27');
INSERT INTO `workday`
VALUES ('2023-09-28');
INSERT INTO `workday`
VALUES ('2023-10-07');
INSERT INTO `workday`
VALUES ('2023-10-08');
INSERT INTO `workday`
VALUES ('2023-10-09');
INSERT INTO `workday`
VALUES ('2023-10-10');
INSERT INTO `workday`
VALUES ('2023-10-11');
INSERT INTO `workday`
VALUES ('2023-10-12');
INSERT INTO `workday`
VALUES ('2023-10-13');
INSERT INTO `workday`
VALUES ('2023-10-16');
INSERT INTO `workday`
VALUES ('2023-10-17');
INSERT INTO `workday`
VALUES ('2023-10-18');
INSERT INTO `workday`
VALUES ('2023-10-19');
INSERT INTO `workday`
VALUES ('2023-10-20');
INSERT INTO `workday`
VALUES ('2023-10-23');
INSERT INTO `workday`
VALUES ('2023-10-24');
INSERT INTO `workday`
VALUES ('2023-10-25');
INSERT INTO `workday`
VALUES ('2023-10-26');
INSERT INTO `workday`
VALUES ('2023-10-27');
INSERT INTO `workday`
VALUES ('2023-10-30');
INSERT INTO `workday`
VALUES ('2023-10-31');
INSERT INTO `workday`
VALUES ('2023-11-01');
INSERT INTO `workday`
VALUES ('2023-11-02');
INSERT INTO `workday`
VALUES ('2023-11-03');
INSERT INTO `workday`
VALUES ('2023-11-06');
INSERT INTO `workday`
VALUES ('2023-11-07');
INSERT INTO `workday`
VALUES ('2023-11-08');
INSERT INTO `workday`
VALUES ('2023-11-09');
INSERT INTO `workday`
VALUES ('2023-11-10');
INSERT INTO `workday`
VALUES ('2023-11-13');
INSERT INTO `workday`
VALUES ('2023-11-14');
INSERT INTO `workday`
VALUES ('2023-11-15');
INSERT INTO `workday`
VALUES ('2023-11-16');
INSERT INTO `workday`
VALUES ('2023-11-17');
INSERT INTO `workday`
VALUES ('2023-11-20');
INSERT INTO `workday`
VALUES ('2023-11-21');
INSERT INTO `workday`
VALUES ('2023-11-22');
INSERT INTO `workday`
VALUES ('2023-11-23');
INSERT INTO `workday`
VALUES ('2023-11-24');
INSERT INTO `workday`
VALUES ('2023-11-27');
INSERT INTO `workday`
VALUES ('2023-11-28');
INSERT INTO `workday`
VALUES ('2023-11-29');
INSERT INTO `workday`
VALUES ('2023-11-30');
INSERT INTO `workday`
VALUES ('2023-12-01');
INSERT INTO `workday`
VALUES ('2023-12-04');
INSERT INTO `workday`
VALUES ('2023-12-05');
INSERT INTO `workday`
VALUES ('2023-12-06');
INSERT INTO `workday`
VALUES ('2023-12-07');
INSERT INTO `workday`
VALUES ('2023-12-08');
INSERT INTO `workday`
VALUES ('2023-12-11');
INSERT INTO `workday`
VALUES ('2023-12-12');
INSERT INTO `workday`
VALUES ('2023-12-13');
INSERT INTO `workday`
VALUES ('2023-12-14');
INSERT INTO `workday`
VALUES ('2023-12-15');
INSERT INTO `workday`
VALUES ('2023-12-18');
INSERT INTO `workday`
VALUES ('2023-12-19');
INSERT INTO `workday`
VALUES ('2023-12-20');
INSERT INTO `workday`
VALUES ('2023-12-21');
INSERT INTO `workday`
VALUES ('2023-12-22');
INSERT INTO `workday`
VALUES ('2023-12-25');
INSERT INTO `workday`
VALUES ('2023-12-26');
INSERT INTO `workday`
VALUES ('2023-12-27');
INSERT INTO `workday`
VALUES ('2023-12-28');
INSERT INTO `workday`
VALUES ('2023-12-29');

SET
FOREIGN_KEY_CHECKS = 1;


