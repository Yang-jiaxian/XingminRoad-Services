# -*- coding: utf-8 -*-
# @Author: Yang jiaxian
# @Date  : 2022/11/15
# @Desc  :
# @Email : 499706512@qq.com
from src.common.OptionMysql import OptionMysql
from src.error import InternalException, status
from src.const import operator_list


class OperatorServices(object):

    @staticmethod
    def create(name, phone):
        """新增操作人

        """
        mysql = OptionMysql()
        affect_rows, operator_id = mysql.insert_dict("operator", {"name": name, "phone": phone}, True)
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="新增操作人失败")
        operator_list.append(operator_id)
        return operator_id

    @staticmethod
    def delete(operatorId):
        """删除操作人

        """
        mysql = OptionMysql()
        sql_statement = """UPDATE `operator` SET `is_delete`=1 WHERE `is_delete`=0 AND `id`=%s"""
        affect_rows = mysql.update_one(sql_statement, [operatorId])
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="删除操作人失败")
        operator_list.remove(operatorId)

    @staticmethod
    def fetch_one(operatorId):
        """获取一条操作人数据

        """
        mysql = OptionMysql()
        sql_statement = """SELECT `id`,`name`,`phone` FROM `operator` WHERE `is_delete`=0 AND `id`=%s"""
        result = mysql.fetch_one(sql_statement, [operatorId])
        return result

    @staticmethod
    def fetch_data(pageNo, pageSize):
        """获取多条操作人数据

        pageNo   : 页码
        pageSize : 页大小
        """
        mysql = OptionMysql()
        sql_statement = """SELECT COUNT(`id`) AS count FROM `operator` WHERE `is_delete`=0"""
        result = mysql.fetch_one(sql_statement)

        sql_statement = """SELECT `id`,`name`,`phone` FROM `operator` WHERE `is_delete`=0"""
        if pageNo and pageSize:
            sql_statement += """ LIMIT {}, {}""".format((pageNo - 1) * pageSize, pageSize)
        results = mysql.fetch_data(sql_statement)
        return result["count"], results
