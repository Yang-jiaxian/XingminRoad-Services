# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/9/21
import os
import time
from fastapi import Header, Request
from fastapi.responses import JSONResponse
from datetime import datetime, date
from src.common.logger import logger
from src.const import operator_list
from src.error import InternalException, status


def format_data(data: list):
    """格式化数据

    """
    for item in data:
        for key, value in item.items():
            if isinstance(value, datetime) or isinstance(value, date):
                item[key] = str(value)
    return data


def output_json(data, message, code: int = 0, total=None):
    """格式化输出

    """
    if total is not None:
        return JSONResponse(content={"code": code, 'message': message, 'data': data, 'total': total})
    return JSONResponse(content={"code": code, 'message': message, 'data': data})


def delete_dir(dir_path, keep_day):
    """删除日志文件夹下的所有过期的文件及文件夹，会保留dir_path文件夹

    """
    for root, dirs, files in os.walk(dir_path, topdown=False):
        # 第一步：删除文件
        for name in files:
            path = os.path.join(root, name)
            create_time = os.path.getctime(path)  # 文件创建时间
            current_time = time.time()
            result = (current_time - create_time) / 60 / 60 / 24
            if result >= keep_day:
                logger.info(f'清理文件:{path}')
                os.remove(path)

        # 第二步：删除空文件夹
        for name in dirs:
            path = os.path.join(root, name)
            if not os.listdir(path):
                logger.info(f'清理文件夹:{path}')
                os.rmdir(path)  # 删除一个空目录


def check_operator(operator_id: int = Header(...), requests: Request = None):
    """校验操作员ID"""
    if operator_id not in operator_list:
        raise InternalException(status.HTTP_401_UNAUTHORIZED, "No Auth")
    return operator_id


if __name__ == '__main__':
    path = "C:\\Users\\yangj\\Desktop\\github\\Search-Service\\test"
    delete_dir(path, 1)
