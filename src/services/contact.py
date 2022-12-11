# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/15
from src.common.OptionMysql import OptionMysql
from src.error import InternalException, status
from src.utils import format_data


class ContactServices(object):

    @staticmethod
    def create(**kwargs):
        """新增联系记录

        """
        mysql = OptionMysql()
        affect_rows, contact_id = mysql.insert_dict("contact", kwargs, True)
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="新增联系记录失败")
        return contact_id

    @staticmethod
    def delete(contactId):
        """删除联系记录

        """
        mysql = OptionMysql()
        sql_statement = """UPDATE `contact` SET `is_delete`=1 WHERE `is_delete`=0 AND `id`=%s"""
        affect_rows = mysql.update_one(sql_statement, [contactId])
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="删除联系记录失败")

    @staticmethod
    def update(contactId, **kwargs):
        """更新联系记录

        """
        mysql = OptionMysql()
        affect_rows = mysql.update_dict("contact", where=f"`id`={contactId}", data=kwargs)
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="修改联系记录失败")

    @staticmethod
    def fetch_one(contactId):
        """获取一条联系记录

        """
        mysql = OptionMysql()
        sql_statement = """SELECT * FROM `contact` WHERE `is_delete`=0 AND `id`=%s"""
        result = mysql.fetch_one(sql_statement, [contactId])
        return result

    @staticmethod
    def fetch_date(customerId, pageNo, pageSize):
        """获取联系记录

        """
        mysql = OptionMysql()
        sql_statement = """SELECT COUNT(`id`) AS count FROM `contact` WHERE `is_delete`=0"""
        params = []
        if customerId is not None:
            sql_statement += """ AND `customer_id`=%s"""
            params.append(customerId)
        result = mysql.fetch_one(sql_statement, [customerId])

        sql_statement = """SELECT
                            `id`,
                            `customer_id`,
                            `contact_date`,
                            `contact_detail`,
                            `demand`,
                            `next_contact_date`,
                            `remind_freq` 
                        FROM
                            `contact` 
                        WHERE
                            `is_delete` = 0 
                            """
        if customerId is not None:
            sql_statement += """ AND `customer_id`=%s"""
        if pageNo and pageSize:
            sql_statement += """ LIMIT {}, {}""".format((pageNo - 1) * pageSize, pageSize)
        results = mysql.fetch_data(sql_statement, params)
        return result["count"], format_data(results)
