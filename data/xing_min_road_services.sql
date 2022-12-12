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

 Date: 12/12/2022 15:19:02
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for contact
-- ----------------------------
DROP TABLE IF EXISTS `contact`;
CREATE TABLE `contact`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '联系记录ID',
  `customer_id` int(0) NOT NULL COMMENT '客户ID',
  `contact_date` date NULL DEFAULT NULL COMMENT '联系日期（拜访时间）',
  `contact_detail` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '联系详情（拜访内容）',
  `demand` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '需求',
  `next_contact_date` date NULL DEFAULT NULL COMMENT '预约下一次拜访时间',
  `remind_freq` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '预约提醒频率',
  `main_appeal` int(0) NULL DEFAULT NULL COMMENT '主要诉求',
  `operator` int(0) NOT NULL COMMENT '登记人',
  `is_delete` tinyint(0) NOT NULL DEFAULT 0 COMMENT '是否删除',
  `created_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updated_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '联系记录表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for cooperative_brokerage
-- ----------------------------
DROP TABLE IF EXISTS `cooperative_brokerage`;
CREATE TABLE `cooperative_brokerage`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `customer_id` int(0) NOT NULL COMMENT '客户ID',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '券商名称',
  `advantage_project` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '优势项目',
  `created_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updated_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '合作券商表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for customer
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
  `existing_assets` int(0) NULL DEFAULT NULL COMMENT '资产-现有资产',
  `historical_peak` int(0) NULL DEFAULT NULL COMMENT '资产-历史峰值',
  `customer_source` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '客户情况-客户来源',
  `specific_channel` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '客户情况-具体渠道',
  `commission_rate` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '佣金费率',
  `risk_appetite` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '风险偏好',
  `contact_status` int(0) NULL DEFAULT 0 COMMENT '联系次数',
  `developer` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '开发关系（人名）',
  `is_internet_channel` tinyint(1) NULL DEFAULT NULL COMMENT '是否是互联网渠道',
  `assignmenter` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '服务包分配（人名）',
  `follower` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '跟进情况（人名）',
  `permissions` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '权限开通(存json)',
  `margin_account` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '融资融券-账号',
  `account_opening_date` date NULL DEFAULT NULL COMMENT '融资融券-开户日期',
  `preferential_interest_rate` float NULL DEFAULT NULL COMMENT '融资融券-优惠利率',
  `interest_rate_effective_date` date NULL DEFAULT NULL COMMENT '融资融券-利率生效日期',
  `interest_rate_expiry_date` date NULL DEFAULT NULL COMMENT '融资融券-利率失效日期',
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
) ENGINE = InnoDB AUTO_INCREMENT = 0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '客户表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for fund
-- ----------------------------
DROP TABLE IF EXISTS `fund`;
CREATE TABLE `fund`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '基金ID',
  `customer_id` int(0) NOT NULL COMMENT '客户ID',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL DEFAULT NULL COMMENT '购买产品',
  `amount` int(0) NULL DEFAULT NULL COMMENT '购买金额',
  `yield_rate` float NULL DEFAULT NULL COMMENT '收益率',
  `buy_date` date NULL DEFAULT NULL COMMENT '购买时间',
  `day_number` int(0) NULL DEFAULT NULL COMMENT '产品天数',
  `due_date` date NULL DEFAULT NULL COMMENT '到期日',
  `is_delete` tinyint(0) NULL DEFAULT 0 COMMENT '是否删除',
  `created_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updated_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '基金理财、私募表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for log
-- ----------------------------
DROP TABLE IF EXISTS `log`;
CREATE TABLE `log`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '日志ID',
  `operator_id` int(0) NOT NULL COMMENT '操作员ID',
  `detail` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '日志详情',
  `query` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NULL COMMENT '参数',
  `is_delete` tinyint(0) NULL DEFAULT 0 COMMENT '是否删除',
  `created_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updated_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '操作日志表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for operator
-- ----------------------------
DROP TABLE IF EXISTS `operator`;
CREATE TABLE `operator`  (
  `id` int(0) NOT NULL AUTO_INCREMENT COMMENT '操作员ID',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '操作员',
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL COMMENT '联系方式',
  `is_delete` tinyint(1) NOT NULL DEFAULT 0 COMMENT '是否删除',
  `created_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) COMMENT '创建时间',
  `updated_at` datetime(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin COMMENT = '操作员表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

-- ----------------------------
-- insert data
-- ----------------------------
INSERT INTO `xing_min_road_services`.`operator`(`name`, `phone`) VALUES ('测试', '13800138000')
