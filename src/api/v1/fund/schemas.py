# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/15
from pydantic import BaseModel, Field
from src.const import DATE_REGEX


class CreateFundParams(BaseModel):
    customer_id: int = Field(..., title="客户ID")
    name: str = Field(..., title="产品名称")
    amount: int = Field(..., title="购买金额")
    yield_rate: float = Field(..., title="收益率")
    buy_date: str = Field(..., regex=DATE_REGEX, title="购买时间")
    day_number: int = Field(..., title="产品天数")
    due_date: str = Field(..., regex=DATE_REGEX, title="到期日")


class UpdateFundParams(BaseModel):
    name: str = Field(None, title="产品名称")
    amount: int = Field(None, title="购买金额")
    yield_rate: float = Field(None, title="收益率")
    buy_date: str = Field(None, regex=DATE_REGEX, title="购买时间")
    day_number: int = Field(None, title="产品天数")
    due_date: str = Field(None, regex=DATE_REGEX, title="到期日")
