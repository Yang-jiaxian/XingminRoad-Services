# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/14
from enum import IntEnum, Enum


class CustomerType(IntEnum):
    """客户类型"""
    individual_customer = 0  # 个人客户
    institutional_customer = 1  # 机构客户


class RemindFreq(str, Enum):
    """提醒频率"""
    weekly = "1w"  # 每周
    monthly = "1m"  # 每月
    quarterly = "1q"  # 每年


operator_list = []

DATE_REGEX = "^([1-2][0-9][0-9][0-9]-[0-1]{0,1}[0-9]-[0-3]{0,1}[0-9])$"
DATETIME_REGEX = "^([1-2][0-9][0-9][0-9]-[0-1]{0,1}[0-9]-[0-3]{0,1}[0-9])\s(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d$"
