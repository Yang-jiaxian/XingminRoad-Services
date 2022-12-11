# -*- coding: utf-8 -*-
# @Author: Yang jiaxian
# @Date  : 2022/9/19
# @Desc  : 全局schemas
# @Email : 499706512@qq.com
from pydantic import BaseModel, Field


class MessageResp(BaseModel):
    message: str = Field(..., title='提示信息', description='提示信息')


class VersionResp(BaseModel):
    version: str = Field(..., title='版本信息', description='版本信息')


class StatusCodeResp(BaseModel):
    code: int = Field(..., title='异常状态值', description='异常状态值')
    message: str = Field(..., title='异常状态值说明', description='异常状态值说明')


class HeartData(BaseModel):
    info: str = Field(..., title="心跳状态")
