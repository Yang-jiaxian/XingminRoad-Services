# -*- coding: utf-8 -*-
# @Author: Yang jiaxian
# @Date  : 2022/9/19
# @Desc  : 日志处理
# @Email : 499706512@qq.com
import os
import time
from settings import settings
from loguru import logger

log_path_info = os.path.join(settings.LOGS_DIR, f'{time.strftime("%Y-%m-%d")}.log')

# 日志简单配置 文件区分不同级别的日志
logger.add(log_path_info, rotation="10 MB", encoding='utf-8', enqueue=True, level='INFO')

__all__ = ["logger"]
