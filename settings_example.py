# -*- coding: utf-8 -*-
# @Author: Yang jiaxian
# @Date  : 2022/9/20
# @Desc  : 配置模板
# @Email : 499706512@qq.com

import os
from typing import Optional

from pydantic import BaseSettings

try:
    with open(r"C:\Users\yangj\Desktop\github\app_demo\README.md", encoding='utf8') as f:
        description = f.read()

    _idx = description.index('\n')
    title = description[:_idx].strip('# ')
    description = description[_idx + 1:].strip()
except:
    title = ""
    description = ""


class DeveSettings(BaseSettings):
    # 开发模式配置

    # 应用版本
    APP_VERSION = "1.0.1"
    # 是否开启DEBUG
    DEBUG: bool = True
    # 项目文档
    TITLE: str = title
    # 描述
    DESCRIPTION: str = description
    # 文档地址 默认为docs
    DOCS_URL: str = "/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = "/redoc"
    # token过期时间s
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 60 * 8
    # 生成token的加密算法
    ALGORITHM: str = "HS256"
    # 生产环境保管好 SECRET_KEY
    SECRET_KEY: str = 'Xingmin-Road@Services'
    # 项目根路径
    BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
    # 日志文件夹
    LOGS_DIR: str = r"F:\code\XingminRoad-Service\logs"
    # MYSQL数据库配置
    MYSQL_CONFIG: dict = {
        'HOST': "127.0.0.1",
        'PORT': 3306,
        'USERNAME': "root",
        'PASSWORD': "123456",
        'DATABASE': "xing_min_road_services"
    }
    # 日志自存10天时间
    LOGS_KEEP_DAYS: int = 10
    # API前缀
    API_PREFIX: str = "/api/v1"


class ProdSettings(BaseSettings):
    # 生产模式配置

    # 应用版本
    APP_VERSION = "1.0.1"
    # 是否开启DEBUG
    DEBUG: bool = False
    # 项目文档
    TITLE: str = title
    # 描述
    DESCRIPTION: str = description
    # 文档地址 默认为docs
    DOCS_URL: str = "/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = "/redoc"
    # token过期时间s
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 60 * 8
    # 生成token的加密算法
    ALGORITHM: str = "HS256"
    # 生产环境保管好 SECRET_KEY
    SECRET_KEY: str = 'Xingmin-Road@Services'
    # 项目根路径
    BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__)))))
    # 日志文件夹
    LOGS_DIR: str = r""  # TODO
    # MYSQL数据库配置
    MYSQL_CONFIG: dict = {  # TODO
        'HOST': "127.0.0.1",
        'PORT': 3306,
        'USERNAME': "root",
        'PASSWORD': "123456",
        'DATABASE': "xing_min_road_services"
    }
    # 日志自存10天时间
    LOGS_KEEP_DAYS: int = 10
    # API前缀
    API_PREFIX: str = "/api/v1"


settings = ProdSettings()
