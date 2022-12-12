# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/14
import json
import datetime

from src.utils import to_chinese4
from src.common.OptionMysql import OptionMysql
from src.error import InternalException, status


class CustomerServices(object):


    @staticmethod
    def create(**kwargs):
        """新增客户

        """
        kwargs["created_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mysql = OptionMysql()
        affect_rows, customer_id = mysql.insert_dict("customer", kwargs, True)
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="新增客户失败")
        return customer_id

    @staticmethod
    def delete(customerId):
        """删除客户

        """
        mysql = OptionMysql()
        sql_statement = """UPDATE `customer` SET `is_delete`=1 WHERE `is_delete`=0 AND `id`=%s"""
        affect_rows = mysql.update_one(sql_statement, [customerId])
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="删除客户失败")

    @staticmethod
    def update(customerId, **kwargs):
        """更新客户信息

        """
        mysql = OptionMysql()
        affect_rows = mysql.update_dict("customer", where=f"`id`={customerId}", data=kwargs)
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="修改客户数据失败")

    @staticmethod
    def fetch_one(customerId):
        """获取一条数据

        """
        mysql = OptionMysql()
        sql_statement = """SELECT `id` FROM `customer` WHERE `is_delete`=0 AND `id`=%s"""
        result = mysql.fetch_one(sql_statement, [customerId])

        result["permissions"] = json.loads(result["permissions"])
        # result["fund_demand"] = json.loads(result["fund_demand"])
        # result["technical_demand"] = json.loads(result["technical_demand"])
        # result["bond_source_demand"] = json.loads(result["bond_source_demand"])
        # result["investment_research_demand"] = json.loads(result["investment_research_demand"])
        # result["private_placement_strategy"] = json.loads(result["private_placement_strategy"])
        if result["contact_status"] == 0:
            result["contact_status"] = "从未联系"
        else:
            result["contact_status"] = "第" + to_chinese4(result["contact_status"]) + "次"
        return result

    @staticmethod
    def fetch_data(self, ):
        mysql = OptionMysql()
        # TODO 暂时是*
        sql_statement = """SELECT * FROM `customer` WHERE `is_delete`=0"""


    @staticmethod
    def update_contact_status(customerId):
        """更新客户的联系状态

        幂等，去统计该客户现拥有的联系记录条数
        """
        mysql = OptionMysql()
        sql_statement = """SELECT COUNT(`id`) AS `count` FROM `contact` WHERE `customer_id`=%s AND `is_delete`=0"""
        result = mysql.fetch_one(sql_statement, [customerId])

        sql_statement = """UPDATE `customer` SET `contact_status`=%s WHERE `is_delete`=0 AND `id`=%s"""
        affect_rows = mysql.update_one(sql_statement, [result["count"], customerId])
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="修改客户联系状态失败")
