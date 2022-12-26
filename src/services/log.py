# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/16
import json
from src.common.OptionMysql import OptionMysql
from src.error import InternalException, status


class LogServices():

    @staticmethod
    def create(operator_id: int, detail: str, query: dict = None):
        """新增日志记录

        """
        mysql = OptionMysql()

        data = {"operator_id": operator_id, "detail": detail}
        if query:
            data.update({"query": json.dumps(query)})
        affect_rows, log_id = mysql.insert_dict("log", data, True)
        if affect_rows != 1:
            raise InternalException(status.HTTP_622_MYSQL_ERROR, message="新增客户失败")

    @staticmethod
    def fetch_data(operator_name: str, start_time, end_time, pageNo, pageSize):
        """获取日志记录

        """
        mysql = OptionMysql()
        total_sql = """SELECT COUNT(log.`id`) AS `total` FROM `log` left join `operator` on `log`.operator_id=`operator`.id WHERE log.`is_delete`=0"""
        data_sql = """SELECT log.`id`,operator.`name`,log.`detail`,log.`created_at`,log.`updated_at` FROM `log` left join `operator` on `log`.operator_id=`operator`.id WHERE log.`is_delete`=0"""
        params = []
        if operator_name is not None:
            total_sql += """ AND `operator`.name LIKE %s"""
            data_sql += """ AND `operator`.name LIKE %s"""
            params.append("%" + str(operator_name) + "%")
        if start_time and end_time:
            total_sql += """ AND `log`.created_at >%s AND `log`.created_at <%s"""
            data_sql += """ AND `log`.created_at >%s AND `log`.created_at <%s"""
            params.extend([start_time, end_time])
        total_res = mysql.fetch_one(total_sql, params)
        if pageNo and pageSize:
            data_sql += f""" LIMIT {(pageNo - 1) * pageSize},{pageSize}"""
        data = mysql.fetch_data(data_sql, params)
        return total_res["total"], data
