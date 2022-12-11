# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email   : yangjiaxian@ibbd.net
# @Time    : 2022/9/20
# @Desc    : 初始化数据库
from src.common import SqliteHelper

# 有则连接 无则创建
Db = SqliteHelper.Connect("Search-Service.db")

# 创建表（存在则跳过）
if not Db.table("user").tableExists():
    # TODO
    Db.table('user').create({
        'id': 'INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT',
        'username': 'TEXT NOT NULL',
        'password': 'TEXT NOT NULL'
    })

print("Done!")
