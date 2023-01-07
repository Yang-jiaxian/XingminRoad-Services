# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/9/21
import os
import time

import pandas as pd
from fastapi import Header, Request
from fastapi.responses import JSONResponse
from datetime import datetime, date
from src.common.logger import logger
from src.common.OptionMysql import OptionMysql
from src.const import operator_list
from src.error import InternalException, status

_MAPPING = (u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'十',
            u'十一', u'十二', u'十三', u'十四', u'十五', u'十六', u'十七', u'十八', u'十九')
_P0 = (u'', u'十', u'百', u'千',)
_S4 = 10 ** 4


def get_before_workday(date: str, n: int):
    """获取date日期的第前n个工作日

    """
    mysql = OptionMysql()
    sql = """SELECT `date` FROM `workday` WHERE date < %s ORDER BY `date` DESC LIMIT %s"""
    data = mysql.fetch_data(sql, [date, n])
    if not data:
        raise InternalException(status.HTTP_422_UNPROCESSABLE_ENTITY, "无法追溯到这么早的工作日，请联系管理员")
    return str(data[n - 1]["date"])


def to_chinese4(num):
    assert (0 <= num and num < _S4)
    if num < 20:
        return _MAPPING[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num = num / 10
        lst.append(num)
        c = len(lst)  # 位数
        result = u''
        for idx, val in enumerate(lst):
            val = int(val)
            if val != 0:
                result += _P0[idx] + _MAPPING[val]
                if idx < c - 1 and lst[idx + 1] == 0:
                    result += u'零'
        return result[::-1]


def format_data(data: list):
    """格式化数据

    """
    for item in data:
        for key, value in item.items():
            if isinstance(value, datetime) or isinstance(value, date):
                item[key] = str(value)
    return data


def output_json(data, message, code: int = 0, total=None, **kwargs):
    """格式化输出

    """
    if total is not None:
        content = {"code": code, 'message': message, 'data': data, 'total': total}
    else:

        content = {"code": code, 'message': message, 'data': data}
    content.update(**kwargs)
    return JSONResponse(content=content)


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


def export_data_to_excel(save_file, columns, excel_data):
    data_df = pd.DataFrame(data=excel_data, columns=columns)
    with pd.ExcelWriter(path=save_file, engine="xlsxwriter", options={'strings_to_urls': False}) as writer:
        data_df.to_excel(excel_writer=writer, sheet_name="Sheet1", encoding='utf8', header=False, index=False,
                         startcol=0, startrow=1)
        modify_excel_format(excel_data, writer, data_df)
        writer.save()
    writer.close()


def modify_excel_format(excel_data, writer, df, sheet_name='Sheet1'):
    # 调整excel格式
    workbook = writer.book
    fmt = workbook.add_format({"font_name": u"宋体"})
    col_fmt = workbook.add_format(
        {'bold': True, 'font_size': 11, 'font_name': u'宋体', 'border': 1, 'bg_color': '#0265CB', 'font_color': 'white',
         'valign': 'vcenter', 'align': 'center'})
    detail_fmt = workbook.add_format(
        {"font_name": u"宋体", 'valign': 'vcenter', 'align': 'center', 'font_size': 11, 'text_wrap': True})
    worksheet1 = writer.sheets[sheet_name]
    for col_num, value in enumerate(df.columns.values):
        worksheet1.write(0, col_num, value, col_fmt)
    # # 设置列宽行宽
    worksheet1.set_column('A:Z', 18, fmt)
    # worksheet1.set_column('F:F', 40, fmt)
    worksheet1.set_row(0, 30, fmt)
    for i in range(1, len(excel_data) + 1):
        worksheet1.set_row(i, 26, detail_fmt)

    return True


if __name__ == '__main__':
    # path = "C:\\Users\\yangj\\Desktop\\github\\Search-Service\\test"
    # delete_dir(path, 1)
    today = str(datetime(2023, 1, 13))
    # print(today)
    DATA = get_before_workday(today, 20)
    print(DATA)
    # mysql = OptionMysql()
    # sql = """SELECT `date` FROM `workday` WHERE date > %s ORDER BY `date` ASC LIMIT %s"""
    # data = mysql.fetch_data(sql, [today, 20])
    # # print(data)
    # print(str(data[20 - 1]))
