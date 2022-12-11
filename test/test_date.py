# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/16
from datetime import timedelta, datetime
import chinese_calendar

# start_time = datetime.date(2022, 1, 1)  # 指定开始时间
# end_time = datetime.date(2022, 12, 30)   # 指定结束时间
#
#
now = datetime.now()

last_week_start = now - timedelta(days=now.weekday() + 7)
last_week_end = now - timedelta(days=now.weekday() + 1)

print(chinese_calendar.get_workdays(last_week_start, last_week_end))