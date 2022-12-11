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

