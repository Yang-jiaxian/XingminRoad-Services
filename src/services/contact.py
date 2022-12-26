# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/15
from src.common.OptionMysql import OptionMysql
from src.error import InternalException, status
from src.utils import format_data, get_before_workday


class ContactServices(object):

    @staticmethod
    def create(**kwargs):
        """新增联系记录

        """
        kwargs["remind_date"] = get_before_workday(kwargs["next_contact_date"], kwargs["remind_duration"])
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
        # 如果改了下次联系的时间
        if kwargs["next_contact_date"]:
            if kwargs["remind_duration"]:
                kwargs["remind_date"] = get_before_workday(kwargs["next_contact_date"], kwargs["remind_duration"])
            else:
                the_contact = ContactServices().fetch_one(contactId)
                kwargs["remind_date"] = get_before_workday(kwargs["next_contact_date"], the_contact["remind_duration"])
        if kwargs["remind_duration"]:
            the_contact = ContactServices().fetch_one(contactId)
            kwargs["remind_date"] = get_before_workday(the_contact["next_contact_date"], kwargs["remind_duration"])

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
                            `remind_duration`,
                            `remind_date` 
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
