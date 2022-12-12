# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/15
from pydantic import BaseModel, Field


class CreateCooperationParams(BaseModel):
    """新增合作券商参数"""
    customer_id: int = Field(..., title="客户ID")
    name: str = Field(..., title="券商名称")
    advantage_project: str = Field(..., title="优势项目")


class UpdateCooperationParams(BaseModel):
    """更新合作券商参数"""
    name: str = Field(..., title="券商名称")
    advantage_project: str = Field(..., title="优势项目")
