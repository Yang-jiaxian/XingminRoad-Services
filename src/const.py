# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/14
from enum import IntEnum, Enum


class Gender(IntEnum):
    Man = 0
    Woman = 1


class CustomerType(IntEnum):
    """客户类型"""
    individual_customer = 0  # 个人客户
    institutional_customer = 1  # 机构客户


class ScaleOfManagement(str, Enum):
    zero_to_five = "0-5E"
    five_to_ten = "5-10E"
    ten_to_twenty = "10-20E"
    twenty_to_fifty = "20-50E"
    fifty_to_one_hundred = "50-100E"
    more_than_one_hundred = ">100E"


operator_list = []

DATE_REGEX = "^([1-2][0-9][0-9][0-9]-[0-1]{0,1}[0-9]-[0-3]{0,1}[0-9])$"
DATETIME_REGEX = "^([1-2][0-9][0-9][0-9]-[0-1]{0,1}[0-9]-[0-3]{0,1}[0-9])\s(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$"
