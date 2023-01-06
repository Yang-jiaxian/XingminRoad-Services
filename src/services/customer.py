# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/14
import json
import datetime

from src.const import INTEREST_RATE_EXPIRY_REMIND_DURATION, CustomerType, RemindType
from src.utils import to_chinese4, get_before_workday
from src.common.OptionMysql import OptionMysql
from src.error import InternalException, status


class CustomerServices(object):

    @staticmethod
    def create(**kwargs):
        """新增客户

        """
        if date := kwargs["interest_rate_expiry_date"]:
            kwargs["interest_rate_expiry_remind_date"] = get_before_workday(date, INTEREST_RATE_EXPIRY_REMIND_DURATION)
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
        if kwargs["interest_rate_expiry_date"]:
            kwargs["interest_rate_expiry_remind_date"] = get_before_workday(kwargs["interest_rate_expiry_date"],
                                                                            INTEREST_RATE_EXPIRY_REMIND_DURATION)

        mysql = OptionMysql()
        affect_rows = mysql.update_dict("customer", where=f"`id`={customerId}", data=kwargs)

    @staticmethod
    def fetch_one(customerId):
        """获取一条数据

        """
        mysql = OptionMysql()
        sql_statement = """SELECT * FROM `customer` WHERE `is_delete`=0 AND `id`=%s"""
        result = mysql.fetch_one(sql_statement, [customerId])
        result["cash_treasure"] = result["cash_treasure"] == 1
        result["automatic_investment_plan"] = result["automatic_investment_plan"] == 1
        result["double_innovation_board"] = result["double_innovation_board"] == 1
        result["share_option"] = result["share_option"] == 1
        result["shenzhen_hong_kong_stock_connect"] = result["shenzhen_hong_kong_stock_connect"] == 1
        result["shanghai_hong_kong_stock_connect"] = result["shanghai_hong_kong_stock_connect"] == 1
        result["double_margin_account"] = result["double_margin_account"] == 1
        result["beijing_stock_exchange"] = result["beijing_stock_exchange"] == 1
        result["pension_account"] = result["pension_account"] == 1
        result["fund_demand"] = json.loads(result["fund_demand"]) if result["fund_demand"] else {}
        result["technical_demand"] = json.loads(result["technical_demand"]) if result["technical_demand"] else {}
        result["bond_source_demand"] = json.loads(result["bond_source_demand"]) if result["bond_source_demand"] else {}
        result["investment_research_demand"] = json.loads(result["investment_research_demand"]) if result[
            "investment_research_demand"] else {}
        result["private_placement_strategy"] = json.loads(result["private_placement_strategy"]) if result[
            "private_placement_strategy"] else {}
        if result["contact_status"] == 0:
            result["contact_status"] = "从未联系"
        else:
            result["contact_status"] = "第" + to_chinese4(result["contact_status"]) + "次"
        return result

    @staticmethod
    def fetch_data(remind_type, customer_id, capital_account, customer_type, name, contact_person, phone, developer,
                   assignmenter, is_internet_channel, follower, margin_account, gender, permissions, pageNo, pageSize):
        """

        """

        total = 0
        params = []
        fund_summary_tmp = {}
        all_fund_summary = 0
        mysql = OptionMysql()

        # 融资融券到期
        if remind_type == RemindType.interest_rate_expiry_customers:
            total_sql = """SELECT count(*) as total FROM `customer` WHERE `is_delete`=0 AND `interest_rate_expiry_remind_date` < %s AND `interest_rate_expiry_date`>=%s"""
            data_sql = """SELECT * FROM `customer` WHERE `is_delete`=0 AND `interest_rate_expiry_remind_date` < %s AND `interest_rate_expiry_date`>=%s"""
            params.extend([str(datetime.datetime.today().date()), str(datetime.datetime.today().date())])
        # 基金到期
        elif remind_type == RemindType.fund_expiry_customers:
            total_sql = """SELECT count(DISTINCT customer.id) as total FROM `customer` LEFT JOIN fund ON fund.customer_id=customer.id WHERE customer.is_delete=0 AND fund.is_delete=0 AND fund.remind_date=%s"""
            data_sql = """SELECT customer.* FROM `customer` LEFT JOIN fund ON fund.customer_id=customer.id WHERE customer.is_delete=0 AND fund.is_delete=0 AND fund.remind_date=%s"""
            params.append(str(datetime.datetime.today().date()))
        # 需要联系
        elif remind_type == RemindType.need_to_contact_customers:
            total_sql = """SELECT count(DISTINCT customer.id) as total FROM `customer` LEFT JOIN contact ON contact.customer_id=customer.id WHERE customer.is_delete=0 AND contact.is_delete=0 AND contact.remind_date < %s AND contact.next_contact_date >= %s"""
            data_sql = """SELECT customer.* FROM `customer` LEFT JOIN contact ON contact.customer_id=customer.id WHERE customer.is_delete=0 AND contact.is_delete=0 AND contact.remind_date < %s AND contact.next_contact_date >= %s"""
            params.extend([str(datetime.datetime.today().date()), str(datetime.datetime.today().date())])
        # 没有条件
        else:
            total_sql = """SELECT count(*) as total FROM `customer` WHERE `is_delete`=0"""
            data_sql = """SELECT * FROM `customer` WHERE `is_delete`=0"""

        if customer_id is not None:
            total_sql += """ AND customer.id=%s"""
            data_sql += """ AND customer.id=%s"""
            params.append(customer_id)
        if customer_type is not None:
            total_sql += """ AND customer.customer_type=%s"""
            data_sql += """ AND customer.customer_type=%s"""
            params.append(customer_type)
        if is_internet_channel is not None:
            total_sql += """ AND customer.is_internet_channel=%s"""
            data_sql += """ AND customer.is_internet_channel=%s"""
            params.append(is_internet_channel)
        if gender is not None:
            total_sql += """ AND customer.gender=%s"""
            data_sql += """ AND customer.gender=%s"""
            params.append(gender)
        if permissions is not None:
            permissions = permissions.name
            total_sql += f" AND customer.{permissions}=1"
            data_sql += f" AND customer.{permissions}=1"
        if capital_account is not None:
            total_sql += " AND customer.capital_account LIKE %s"
            data_sql += " AND customer.capital_account LIKE %s"
            params.append("%" + capital_account + "%")
        if name is not None:
            total_sql += " AND customer.name LIKE %s"
            data_sql += " AND customer.name LIKE %s"
            params.append("%" + name + "%")
        if contact_person is not None:
            total_sql += " AND customer.contact_person LIKE %s"
            data_sql += " AND customer.contact_person LIKE %s"
            params.append("%" + contact_person + "%")
        if phone is not None:
            total_sql += " AND customer.phone LIKE %s"
            data_sql += " AND customer.phone LIKE %s"
            params.append("%" + phone + "%")
        if developer is not None:
            total_sql += " AND customer.developer LIKE %s"
            data_sql += " AND customer.developer LIKE %s"
            params.append("%" + developer + "%")
        if assignmenter is not None:
            total_sql += " AND customer.assignmenter LIKE %s"
            data_sql += " AND customer.assignmenter LIKE %s"
            params.append("%" + assignmenter + "%")
        if follower is not None:
            total_sql += " AND customer.follower LIKE %s"
            data_sql += " AND customer.follower LIKE %s"
            params.append("%" + follower + "%")
        if margin_account is not None:
            total_sql += " AND customer.margin_account LIKE %s"
            data_sql += " AND customer.margin_account LIKE %s"
            params.append("%" + margin_account + "%")

        total_result = mysql.fetch_one(total_sql, params)
        if total_result:
            total = total_result["total"]

        pre_query_res = mysql.fetch_data(data_sql, params)
        id_list = [item["id"] for item in pre_query_res]
        if id_list:
            fund_summary_sql = """SELECT fund.customer_id,sum(fund.amount) as fund_amount_summary FROM `customer` RIGHT JOIN fund ON customer.id = fund.customer_id WHERE fund.is_delete=0 AND customer.is_delete=0 AND fund.customer_id IN %s GROUP BY fund.customer_id;"""
            fund_summary_res = mysql.fetch_data(fund_summary_sql, [tuple(id_list)])
            fund_summary_tmp = {item["customer_id"]: round(item["fund_amount_summary"], 2) for item in fund_summary_res}
            all_fund_summary = sum([item["fund_amount_summary"] for item in fund_summary_res])

        data_sql += f""" GROUP BY customer.id ORDER BY id DESC LIMIT {(pageNo - 1) * pageSize},{pageSize}"""
        data = mysql.fetch_data(data_sql, params)
        for result in data:
            result["cash_treasure"] = result["cash_treasure"] == 1
            result["automatic_investment_plan"] = result["automatic_investment_plan"] == 1
            result["double_innovation_board"] = result["double_innovation_board"] == 1
            result["share_option"] = result["share_option"] == 1
            result["shenzhen_hong_kong_stock_connect"] = result["shenzhen_hong_kong_stock_connect"] == 1
            result["shanghai_hong_kong_stock_connect"] = result["shanghai_hong_kong_stock_connect"] == 1
            result["double_margin_account"] = result["double_margin_account"] == 1
            result["beijing_stock_exchange"] = result["beijing_stock_exchange"] == 1
            result["pension_account"] = result["pension_account"] == 1

            result["fund_demand"] = json.loads(result["fund_demand"]) if result["fund_demand"] else {}
            result["fund_amount_summary"] = fund_summary_tmp.get(result["id"], 0)
            result["technical_demand"] = json.loads(result["technical_demand"]) if result["technical_demand"] else {}
            result["bond_source_demand"] = json.loads(result["bond_source_demand"]) if result[
                "bond_source_demand"] else {}
            result["investment_research_demand"] = json.loads(result["investment_research_demand"]) if result[
                "investment_research_demand"] else {}
            result["private_placement_strategy"] = json.loads(result["private_placement_strategy"]) if result[
                "private_placement_strategy"] else {}
            result["contact_status"] = "从未联系" if result["contact_status"] == 0 else "第" + to_chinese4(
                result["contact_status"]) + "次"

        return total, data, all_fund_summary

    @staticmethod
    def update_contact_status(customerId):
        """更新客户的联系状态

        幂等，去统计该客户现拥有的联系记录条数
        """
        mysql = OptionMysql()
        sql_statement = """SELECT COUNT(`id`) AS `count` FROM `contact` WHERE `customer_id`=%s AND `is_delete`=0"""
        result = mysql.fetch_one(sql_statement, [customerId])

        sql_statement = """UPDATE `customer` SET `contact_status`=%s WHERE `is_delete`=0 AND `id`=%s"""
        mysql.update_one(sql_statement, [result["count"], customerId])

    @staticmethod
    def get_remind_customers_count(date):
        """获取需提醒的客户数量统计"""
        mysql = OptionMysql()
        sql_statement = """SELECT
                                `customer_type`,
                                COUNT( `id` ) AS total 
                            FROM
                                `customer` 
                            WHERE
                                `interest_rate_expiry_remind_date` <% s
                                AND `interest_rate_expiry_date` >= %s 
                                AND `is_delete` = 0 
                            GROUP BY
                                `customer_type`"""
        interest_rate_expiry_remind_result = mysql.fetch_data(sql_statement, [date, date])
        interest_rate_expiry_remind_result_tmp = {item["customer_type"]: item["total"] for item in
                                                  interest_rate_expiry_remind_result}

        sql_statement = """SELECT
                                `customer_type`,
                                COUNT( `id` ) AS total 
                            FROM
                                `customer` 
                            WHERE
                                id IN ( SELECT `customer_id` FROM `fund` WHERE `remind_date` =% s AND `is_delete` = 0 GROUP BY `customer_id` ) 
                                AND `is_delete` = 0 
                            GROUP BY
                                `customer_type`"""
        fund_expiry_remind_result = mysql.fetch_data(sql_statement, [date])
        fund_expiry_remind_result_tmp = {item["customer_type"]: item["total"] for item in fund_expiry_remind_result}

        sql_statement = """SELECT
                                `customer_type`,
                                COUNT( `id` ) AS total 
                            FROM
                                `customer` 
                            WHERE
                                id IN ( SELECT `customer_id` FROM `contact` WHERE `remind_date` <% s AND `next_contact_date`>=%s AND `is_delete` = 0 GROUP BY `customer_id` ) 
                                AND `is_delete` = 0 
                            GROUP BY
                                `customer_type`"""
        need_to_contact_remind_result = mysql.fetch_data(sql_statement, [date, date])
        need_to_contact_remind_result_tmp = {item["customer_type"]: item["total"] for item in
                                             need_to_contact_remind_result}

        data = {
            CustomerType.individual_customer.name: {
                "interest_rate_expiry_customers_count": interest_rate_expiry_remind_result_tmp.get(
                    CustomerType.individual_customer.value, 0),
                "fund_expiry_customers_count": fund_expiry_remind_result_tmp.get(CustomerType.individual_customer.value,
                                                                                 0),
                "need_to_contact_customers_count": need_to_contact_remind_result_tmp.get(
                    CustomerType.individual_customer.value, 0),
            },
            CustomerType.institutional_customer.name: {
                "interest_rate_expiry_customers_count": interest_rate_expiry_remind_result_tmp.get(
                    CustomerType.institutional_customer.value, 0),
                "fund_expiry_customers_count": fund_expiry_remind_result_tmp.get(
                    CustomerType.institutional_customer.value, 0),
                "need_to_contact_customers_count": need_to_contact_remind_result_tmp.get(
                    CustomerType.institutional_customer.value, 0),
            }}
        return data
