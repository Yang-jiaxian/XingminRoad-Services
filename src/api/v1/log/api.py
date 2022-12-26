# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/12/26
import os
import datetime

from fastapi import APIRouter, Query
from fastapi.responses import FileResponse

from src.api.v1.log.schemas import FetchlogsResp
from src.utils import output_json, export_data_to_excel
from src.services.log import LogServices
from settings import settings

log_app = APIRouter(tags=["日志"])


@log_app.get("/logs", summary="获取日志", response_model=FetchlogsResp)
async def fetch_log_api(
        operator_name: str = Query(None, title="操作人名字", description="模糊查询"),
        start_time: str = Query(None, title="开始时间", description="开始时间"),
        end_time: str = Query(None, title="结束时间", description="结束时间"),
        pageNo: int = Query(1, title="页码", description="页码"),
        pageSize: int = Query(20, title="页大小", description="页大小")
):
    total, logs = LogServices().fetch_data(operator_name, start_time, end_time, pageNo, pageSize)
    return output_json(data=logs, total=total, message="")


@log_app.get("/logs/export", summary="导出日志")
async def fetch_log_api(
        operator_name: str = Query(None, title="操作人名字", description="模糊查询"),
        start_time: str = Query(None, title="开始时间", description="开始时间"),
        end_time: str = Query(None, title="结束时间", description="结束时间")
):
    total, logs = LogServices().fetch_data(operator_name, start_time, end_time, None, None)
    now = datetime.datetime.now()
    filename = f"{now.year}年{now.month}月{now.day}日{now.hour}时{now.minute}分.xlsx"
    file_path = os.path.join(settings.LOGS_DIR, filename)
    export_data_to_excel(file_path, columns=["日志ID", "详情", "创建时间", "更新时间"],
                         excel_data=[[row["id"], row["detail"], row["created_at"], row["updated_at"]] for row in logs])
    return FileResponse(file_path, filename=filename)
