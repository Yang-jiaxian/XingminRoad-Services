# -*- coding: utf-8 -*-
# @Author: Yang jiaxian
# @Date  : 2022/9/19
# @Desc  : 程序主入口
# @Email : 499706512@qq.com
import asyncio
import os
import random
from typing import List
# import contextvars
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_utils.tasks import repeat_every

from settings import settings
from src.common.logger import logger
from src.error import get_status, init_exception
from src.router import include_routers
from src.schemas import VersionResp, StatusCodeResp, HeartData
from src.services.operator import OperatorServices
from src.utils import delete_dir
from src.const import operator_list

app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
    version=settings.APP_VERSION,
    docs_url=settings.DOCS_URL,
    openapi_url=settings.OPENAPI_URL
)

# 跨域配置
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static")


@app.middleware("http")
async def gunicorn_logger(request: Request, call_next):
    response: Response = await call_next(request)
    logger.info(f'{request.client.host}:{request.client.port} - '
                f'"{request.method.upper()} {request.url.path}"  {response.status_code} ')
    return response


@app.on_event('startup')
async def startup_event():
    if not os.path.exists(settings.LOGS_DIR):
        logger.info("logs文件夹不存在，创建logs文件夹")
        os.mkdir(settings.LOGS_DIR)
    _, operators = OperatorServices().fetch_data(None, None)  # 获取到所有的操作人姓名
    operator_list.extend([operator["id"] for operator in operators])
    # 定时任务
    # scheduler = AsyncIOScheduler(timezone="Asia/Shanghai")
    # scheduler.add_job(send_massage, 'interval', minutes=1)
    # scheduler.add_job(send_massage, "cron", month="*", day=2, hour='*', minute="*", second="*")
    # scheduler.start()
    pass


@app.on_event('startup')
@repeat_every(seconds=6 * random.randint(600, 800), wait_first=False)
async def remove_file():
    """不断清理过期的文件

    """
    logger.info('检测过期文件')
    event_loop = asyncio.get_event_loop()
    event_loop.run_in_executor(None, delete_dir, settings.LOGS_DIR, settings.LOGS_KEEP_DAYS)


# 导入路由
include_routers(app)

# 异常处理
init_exception(app)


@app.get(settings.API_PREFIX + "/version", summary='获取系统版本号',
         response_model=VersionResp, tags=["基础服务"])
async def version_api():
    """获取系统版本号"""
    return {"version": settings.APP_VERSION}


@app.get(settings.API_PREFIX + "/status/code", summary='获取接口的异常状态码及说明',
         response_model=List[StatusCodeResp], tags=["基础服务"])
async def status_code_api():
    """获取系统的异常状态值及相应的说明\n
    该接口通常用于开发阶段，用于查询各个状态值及其意义\n
    说明：\n
    1. 返回的code值与HTTP状态码的对应关系，如code值为10603，
    对应的HTTP状态码应该为10603 % 1000 = 603，在实际处理的
    时候，大于等于600的值，会处理成500的状态码
    """
    return get_status()


@app.get(settings.API_PREFIX + "/heartbeat", summary='检测系统是否正常',
         response_model=HeartData, tags=["基础服务"])
async def check_heartbeat_api():
    """检测系统是否正常"""
    return {"info": "healthy"}


@app.get("/", summary='主页',
         response_class=HTMLResponse, include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
