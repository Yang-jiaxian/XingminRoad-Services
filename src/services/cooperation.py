# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/12/12
from src.common.OptionMysql import OptionMysql
from src.error import InternalException, status
from src.utils import format_data


class CooperationServices(object):

    @staticmethod
    def create(**kwargs):
        """新增合作券商

        """
        mysql = OptionMysql()
        affect_rows, cooperation_id = mysql.insert_dict("cooperative_brokerage", kwargs, True)
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="新增合作券商失败")
        return cooperation_id

    @staticmethod
    def delete(cooperationId: int):
        """删除合作券商

        """
        mysql = OptionMysql()
        sql_statement = """DELETE FROM `cooperative_brokerage` WHERE `id`=%s"""
        affect_rows = mysql.update_one(sql_statement, [cooperationId])
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="删除合作券商失败")

    @staticmethod
    def update(cooperationId: int, **kwargs):
        """更新合作券商

        """
        mysql = OptionMysql()
        mysql.update_dict("cooperative_brokerage", where=f"`id`={cooperationId}", data=kwargs)


    @staticmethod
    def fetch_one(cooperationId: int):
        """获取一条合作券商数据

        """
        mysql = OptionMysql()
        sql_statement = """SELECT * FROM `cooperative_brokerage` WHERE `id`=%s"""
        result = mysql.fetch_one(sql_statement, [cooperationId])
        return result

    @staticmethod
    def fetch_date(customerId: int, pageNo: int, pageSize: int):
        """获取多条合作券商数据

        """
        total = 0
        mysql = OptionMysql()
        sql_statement = """SELECT COUNT(`id`) AS count FROM `cooperative_brokerage` WHERE `customer_id`=%s"""
        params = [customerId]
        result = mysql.fetch_one(sql_statement, [customerId])
        if result:
            total = result["count"]

        sql_statement = """SELECT * FROM `cooperative_brokerage` WHERE `customer_id`=%s"""
        if pageNo and pageSize:
            sql_statement += """ ORDER BY id DESC LIMIT {}, {}""".format((pageNo - 1) * pageSize, pageSize)
        results = mysql.fetch_data(sql_statement, params)
        return total, format_data(results)
