# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/14
from src.schemas import StatusCodeResp
from typing import List
from pydantic import BaseModel, Field


class CreateOperatorResp(StatusCodeResp):
    operator_id: int = Field(..., title="操作人id", description="数据库中的操作人id")


class FetchOperatorsResp_Operator(BaseModel):
    id: int = Field(..., title="操作人id", description="操作人id")
    name: str = Field(..., title="操作人名字", description="操作人名字")
    phone: str = Field(..., title="操作人联系方式", description="操作人联系方式")


class FetchOperatorsResp(StatusCodeResp):
    total: int = Field(..., title="命中条数", description="符合条件的记录数")
    data: List[FetchOperatorsResp_Operator] = Field(..., title="数据")
