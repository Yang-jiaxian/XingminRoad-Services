# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/16
from src.const import FUND_REMIND_DURATION
from src.common.OptionMysql import OptionMysql
from src.error import InternalException, status
from src.utils import format_data, get_before_workday


class FundServices(object):

    @staticmethod
    def create(**kwargs):
        """新增客户基金数据

        """
        kwargs["remind_date"] = get_before_workday(kwargs["due_date"], FUND_REMIND_DURATION)
        mysql = OptionMysql()
        affect_rows, fund_id = mysql.insert_dict("fund", kwargs, True)
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="新增客户基金数据失败")
        return fund_id

    @staticmethod
    def delete(fundId):
        """删除客户基金数据

        """
        mysql = OptionMysql()
        sql_statement = """UPDATE `fund` SET `is_delete`=1 WHERE `is_delete`=0 AND `id`=%s"""
        affect_rows = mysql.update_one(sql_statement, [fundId])
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="删除客户基金数据失败")

    @staticmethod
    def update(fundId, **kwargs):
        """更新客户基金数据

        """
        # 如果改了基金过期的时间，则对应修改提醒时间
        if kwargs["due_date"]:
            kwargs["remind_date"] = get_before_workday(kwargs["due_date"], FUND_REMIND_DURATION)
        mysql = OptionMysql()
        affect_rows = mysql.update_dict("fund", where=f"`id`={fundId}", data=kwargs)
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="修改客户基金数据失败")

    @staticmethod
    def fetch_one(fundId):
        """获取客户基金数据

        """
        mysql = OptionMysql()
        sql_statement = """SELECT * FROM `fund` WHERE `is_delete`=0 AND `id`=%s"""
        result = mysql.fetch_one(sql_statement, [fundId])
        return result

    @staticmethod
    def fetch_date(customerId, pageNo, pageSize):
        """

        """
        mysql = OptionMysql()
        sql_statement = """SELECT COUNT(`id`) AS count FROM `fund` WHERE `is_delete`=0"""
        params = []
        if customerId is not None:
            sql_statement += """ AND `customer_id`=%s"""
            params.append(customerId)
        result = mysql.fetch_one(sql_statement, params)

        sql_statement = """SELECT
                            `id`,
                            `customer_id`,
                            `name`,
                            `amount`,
                            `yield_rate`,
                            `buy_date`,
                            `day_number`,
                            `due_date` 
                        FROM
                            `fund` 
                        WHERE
                            `is_delete` = 0 
                           """
        if customerId is not None:
            sql_statement += """ AND `customer_id`=%s"""
        if pageNo and pageSize:
            sql_statement += """ LIMIT {}, {}""".format((pageNo - 1) * pageSize, pageSize)
        results = mysql.fetch_data(sql_statement, params)

        return result["count"], format_data(results)
