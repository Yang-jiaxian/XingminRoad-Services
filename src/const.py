# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/14
from enum import IntEnum, Enum

operator_list = []


class Gender(IntEnum):
    """性别枚举"""
    Man = 0
    Woman = 1


class CustomerType(IntEnum):
    """客户类型"""
    individual_customer = 0  # 个人客户
    institutional_customer = 1  # 机构客户


class ScaleOfManagement(str, Enum):
    """机构客户管理规模枚举"""
    zero_to_five = "0-5E"
    five_to_ten = "5-10E"
    ten_to_twenty = "10-20E"
    twenty_to_fifty = "20-50E"
    fifty_to_one_hundred = "50-100E"
    more_than_one_hundred = ">100E"


class RemindType(str, Enum):
    """提醒类型枚举"""
    interest_rate_expiry_customers = "融资融券利率到期客户"
    fund_expiry_customers = "基金到期客户"
    need_to_contact_customers = "需要联系客户"


# 日期正则
DATE_REGEX = "^([1-2][0-9][0-9][0-9]-[0-1]{0,1}[0-9]-[0-3]{0,1}[0-9])$"

# 时间正则
DATETIME_REGEX = "^([1-2][0-9][0-9][0-9]-[0-1]{0,1}[0-9]-[0-3]{0,1}[0-9])\s(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$"

# 利率失效前多少天提醒
INTEREST_RATE_EXPIRY_REMIND_DURATION = 20

# 基金失效前多少天提醒
FUND_REMIND_DURATION = 1