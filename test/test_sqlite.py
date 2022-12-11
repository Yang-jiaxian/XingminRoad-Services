# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/10
import time
from src.common import SqliteHelper
from settings import DATA_PATH

# _start_time = time.time()
# with SqliteHelper.Connect(DATA_PATH) as db:
#     pass
# data = db.table("mark_task").findAll()
# data = db.table('mark_task').where("`id` < 500").find(count=10, page=0)
# data = db.table('mark_task').where("article_id like '6%'").find(count=200)
# data = db.table('mark_task').where("`article_id`='61588c204048faf9a8f32414' ").findAll()
# print(time.time() - _start_time)
# print(len(data))  # 查询 47.5W 3.5S    95w 7.5S
# for row in data:
#     del row["id"]
#     print(row)
# 主键的索引是没用的, 索引的like没用


# _start_time = time.time()
# SqliteHelper.Connect(DATA_PATH).table("mark_task").data([data[0]]).add()
# print(time.time() - _start_time)
# 插入95W 65S
# 插入1条 0.03S


# 根据时间查询，180W，70条，1.4秒
_start_time = time.time()
with SqliteHelper.Connect(DATA_PATH) as db:
    data = db.table('mark_task').where("datetime(`created_at`) < datetime('2021-11-02 22:26:12')").findAll()
print(time.time() - _start_time)
print(len(data))
