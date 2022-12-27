# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/15
from pydantic import BaseModel, Field
from src.const import DATE_REGEX
from src.schemas import StatusCodeResp
from typing import List


class CreateFundParams(BaseModel):
    customer_id: int = Field(..., title="客户ID")
    name: str = Field(..., title="产品名称")
    amount: float = Field(..., title="购买金额")
    yield_rate: float = Field(..., title="收益率")
    buy_date: str = Field(..., regex=DATE_REGEX, title="购买时间")
    day_number: int = Field(..., title="产品天数")
    due_date: str = Field(..., regex=DATE_REGEX, title="到期日")


class UpdateFundParams(BaseModel):
    name: str = Field(None, title="产品名称")
    amount: float = Field(None, title="购买金额")
    yield_rate: float = Field(None, title="收益率")
    buy_date: str = Field(None, regex=DATE_REGEX, title="购买时间")
    day_number: int = Field(None, title="产品天数")
    due_date: str = Field(None, regex=DATE_REGEX, title="到期日")


class CreateFundResp(StatusCodeResp):
    fund_id: int = Field(..., title="操作人id", description="数据库中的操作人id")


class FetchFundsResp_Fund(BaseModel):
    id: int = Field(..., title="基金id", description="基金id")
    customer_id: int = Field(..., title="客户ID")
    name: str = Field(..., title="产品名称")
    amount: float = Field(..., title="购买金额")
    yield_rate: float = Field(..., title="收益率")
    buy_date: str = Field(..., regex=DATE_REGEX, title="购买时间")
    day_number: int = Field(..., title="产品天数")
    due_date: str = Field(..., regex=DATE_REGEX, title="到期日")


class FetchFundsResp(StatusCodeResp):
    total: int = Field(..., title="命中条数", description="符合条件的记录数")
    data: List[FetchFundsResp_Fund] = Field(..., title="数据")
