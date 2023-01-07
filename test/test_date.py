# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/16
from datetime import datetime

import chinese_calendar

from src.common.OptionMysql import OptionMysql

mysql = OptionMysql()
sql = """DELETE FROM `workday` WHERE 1=1"""
affect_rows = mysql.delete_one(sql)

sql = """INSERT INTO `workday` (date) VALUES(%s) """
start_time = datetime(2004, 1, 1)  # 指定开始时间
end_time = datetime(2023, 12, 31)  # 指定结束时间

data = chinese_calendar.get_workdays(start_time, end_time)

for row in data:
    affect_rows = mysql.insert_one(sql, [str(row)])
    print(affect_rows)
