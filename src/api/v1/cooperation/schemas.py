# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/15
from pydantic import BaseModel, Field
from src.schemas import StatusCodeResp
from typing import List


class CreateCooperationParams(BaseModel):
    """新增合作券商参数"""
    customer_id: int = Field(..., title="客户ID")
    name: str = Field(..., title="券商名称")
    advantage_project: str = Field(..., title="优势项目")


class UpdateCooperationParams(BaseModel):
    """更新合作券商参数"""
    name: str = Field(..., title="券商名称")
    advantage_project: str = Field(..., title="优势项目")


class CreateCooperationResp(StatusCodeResp):
    cooperation_id: int = Field(..., title="操作人id", description="数据库中的操作人id")


class FetchCooperationsResp_Cooperation(BaseModel):
    id: int = Field(..., title="基金id", description="基金id")
    customer_id: int = Field(..., title="客户ID")
    name: str = Field(..., title="券商名称")
    advantage_project: str = Field(..., title="优势项目")


class FetchCooperationsResp(StatusCodeResp):
    total: int = Field(..., title="命中条数", description="符合条件的记录数")
    data: List[FetchCooperationsResp_Cooperation] = Field(..., title="数据")
