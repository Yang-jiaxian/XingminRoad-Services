# -- coding: utf-8 --
#
# Author: yang
# Email: yangjiaxian@ibbd.net
# Created Time: 2021/12/17
import json
from typing import List

import pymysql
from dbutils.pooled_db import PooledDB

from src.error import InternalException, status
from settings import settings


class OptionMysql(object):
    """
    Arg：
    ping: 检查是否服务可用(
        0:never,
        1:whenever it is requested,
        3:when a cursor is created,
        4:when a query is executed,
        7:always)
    creator: 使用链接数据库的模块
    mincached: 初始化时，链接池中至少创建的空闲的链接(0表示不创建)
    maxcached: 链接池中最多闲置的链接(0和None不限制)
    blocking: 连接池中如果没有可用连接后，是否阻塞等待(True:等待；False:不等待然后报错)
    maxusage: 一个链接最多被重复使用的次数(None表示无限制)
    setsession: 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    maxconnections: 连接池允许的最大连接数(0和None表示不限制连接数)
    """

    def __init__(self, mysql_cfg=settings.MYSQL_CONFIG):
        self.POOL = PooledDB(
            creator=pymysql,
            maxconnections=6,
            mincached=2,
            maxcached=5,
            blocking=True,
            maxusage=None,
            setsession=[],
            ping=1,
            host=mysql_cfg["HOST"],
            port=mysql_cfg["PORT"],
            user=mysql_cfg["USERNAME"],
            password=mysql_cfg["PASSWORD"],
            database=mysql_cfg["DATABASE"],
            charset='utf8'
        )

    def __new__(cls, *args, **kw):
        """单例模式"""
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def _connect(self):
        """连接"""
        conn = self.POOL.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

        return conn, cursor

    def _close(self, conn, cursor):
        """关闭连接"""
        cursor.close()
        conn.close()

    def fetch_one(self, sql, params=None) -> dict:
        """获取数据"""
        conn, cursor = self._connect()
        try:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as e:
            print("===========" * 5 + "\n" + sql + "\n" + "===========" * 5)
            if params:
                print(params)
            print(e)
            raise InternalException(status.HTTP_622_MYSQL_ERROR, 'mysql查询数据出错')
        self._close(conn, cursor)
        return result

    def fetch_data(self, sql, params=None) -> List[dict]:
        """获取数据"""
        conn, cursor = self._connect()
        try:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            print("===========" * 5 + "\n" + sql + "\n" + "===========" * 5)
            if params:
                print(params)
            print(e)
            raise InternalException(status.HTTP_622_MYSQL_ERROR, 'mysql查询数据出错')
        self._close(conn, cursor)
        return result

    def insert_one(self, sql, params=None, return_id=False) -> int:
        '''插入数据'''
        conn, cursor = self._connect()
        try:
            if params:
                affect_rows = cursor.execute(sql, params)
                id = cursor.lastrowid
            else:
                affect_rows = cursor.execute(sql)
                id = cursor.lastrowid
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
            raise InternalException(status.HTTP_622_MYSQL_ERROR, 'mysql插入数据出错')
        self._close(conn, cursor)
        if not return_id:
            return affect_rows
        return affect_rows, id

    def insert_dict(self, table: str, data: dict, return_id=False, ignore=False) -> int:
        """插入一个字典"""
        column, values = [], []
        for key in data.keys():
            column.append("`" + key + "`")
            if isinstance(data[key], dict) or isinstance(data[key], list):
                data[key] = json.dumps(data[key])
            values.append(data[key])
        sql = """INSERT"""
        if ignore:
            sql = """INSERT IGNORE"""
        sql += " INTO `" + table + "` (" + ",".join(column) + ") VALUES (" + ",".join(["%s"] * len(column)) + ")"
        conn, cursor = self._connect()
        try:
            affect_rows = cursor.execute(sql, values)
            id = cursor.lastrowid
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
            raise InternalException(status.HTTP_622_MYSQL_ERROR, 'mysql插入数据出错')
        self._close(conn, cursor)
        if return_id:
            return affect_rows, id
        return affect_rows

    def batch_insert(self, sql, params=None) -> int:
        """
        批量插入
        params:必须是元组或列表[(),()]或（（），（））
        """
        conn, cursor = self._connect()
        try:
            if params:
                affect_rows = cursor.executemany(sql, params)
            else:
                affect_rows = cursor.executemany(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
            raise InternalException(status.HTTP_622_MYSQL_ERROR, 'mysql批量插入数据出错')
        self._close(conn, cursor)
        return affect_rows

    def update_one(self, sql, params=None) -> int:
        """更新一条数据"""
        conn, cursor = self._connect()
        try:
            if params:
                affect_rows = cursor.execute(sql, params)
            else:
                affect_rows = cursor.execute(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
            raise InternalException(status.HTTP_622_MYSQL_ERROR, 'mysql更新数据出错')
        self._close(conn, cursor)
        return affect_rows

    def update_dict(self, table: str, where: str, data: dict) -> int:
        """根据字典更新"""
        column = []
        values = []
        # 提取更新的列及值
        for key in data.keys():
            column.append("`" + key + "`" + " = %s")
            if isinstance(data[key], dict) or isinstance(data[key], list):
                data[key] = json.dumps(data[key])
            values.append(data[key])
        sql = "UPDATE " + table + " SET " + ",".join(column) + " WHERE " + where

        conn, cursor = self._connect()
        try:
            affect_rows = cursor.execute(sql, values)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
            raise InternalException(status.HTTP_622_MYSQL_ERROR, 'mysql更新数据出错')
        self._close(conn, cursor)
        return affect_rows

    def batch_update(self, sql, params=None) -> int:
        """批量更新"""
        conn, cursor = self._connect()
        try:
            if params:
                affect_rows = cursor.executemany(sql, params)
            else:
                affect_rows = cursor.execute(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
            raise InternalException(status.HTTP_622_MYSQL_ERROR, 'mysql批量更新数据出错')
        self._close(conn, cursor)
        return affect_rows

    def delete_one(self, sql, params=None) -> int:
        """删除一行"""
        conn, cursor = self._connect()
        try:
            if params:
                affect_rows = cursor.execute(sql, params)
            else:
                affect_rows = cursor.execute(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
            raise InternalException(status.HTTP_622_MYSQL_ERROR, 'mysql删除数据出错')
        self._close(conn, cursor)
        return affect_rows

    def batch_delete(self, sql, params=None) -> int:
        """删除批量"""
        conn, cursor = self._connect()
        try:
            if params:
                affect_rows = cursor.executemany(sql, params)
            else:
                affect_rows = cursor.executemany(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
            raise InternalException(status.HTTP_622_MYSQL_ERROR, 'mysql删除批量数据出错')
        self._close(conn, cursor)
        return affect_rows

    def transaction(self, sqls: list):
        """
        事务
        :param sqls: 拼接好的sql语句列表
        :return:
        """
        conn, cursor = self._connect()
        try:
            for sql in sqls:
                cursor.execute(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
            raise InternalException(status.HTTP_622_MYSQL_ERROR)

    def insert_or_update(self, table, data: dict):
        """存在时更新，不存在时插入"""
        column = []
        column_tmp = []
        values = []
        # 提取更新的列及值
        for key in data.keys():
            column.append("`" + key + "`")
            column_tmp.append("`" + key + "`" + "=%s")
            if isinstance(data[key], dict) or isinstance(data[key], list):
                data[key] = json.dumps(data[key], lambda obj: obj.__dict__)
            values.append(data[key])

        sql = "INSERT INTO `" + table + "`(" + ",".join(column) + ") VALUES(" + ",".join(
            ["%s"] * len(column)) + ") ON DUPLICATE KEY UPDATE " + ",".join(column_tmp)
        conn, cursor = self._connect()
        try:
            affect_rows = cursor.execute(sql, values * 2)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
            raise InternalException(status.HTTP_622_MYSQL_ERROR, 'mysql插入或更新数据出错')
        self._close(conn, cursor)
        return affect_rows
