# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/16
import chinese_calendar
from datetime import datetime

from src.common.OptionMysql import OptionMysql

start_time = datetime(2024, 1, 1)  # 指定开始时间
# start_time = datetime.date()
end_time = datetime(2024, 12, 30)  # 指定结束时间

data = chinese_calendar.get_workdays(start_time, end_time)

mysql = OptionMysql()
sql = """INSERT INTO `workday` (date) VALUES(%s) """

for row in data:
    affect_rows = mysql.insert_one(sql, [str(row)])
    print(affect_rows)
