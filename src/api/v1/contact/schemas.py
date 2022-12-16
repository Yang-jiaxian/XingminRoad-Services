# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/15
from typing import Optional
from pydantic import BaseModel, Field
from src.const import DATE_REGEX


class CreateContactParams(BaseModel):
    """新增联系记录参数"""
    customer_id: int = Field(..., title="客户ID")
    contact_date: str = Field(..., regex=DATE_REGEX, title="联系时间（拜访时间）")
    contact_detail: str = Field(..., title="联系情况说明（拜访情况说明）")
    demand: str = Field(None, title="需求")
    next_contact_date: str = Field(..., regex=DATE_REGEX, title="预约下次拜访时间")
    remind_duration: int = Field(..., gt=0, title="提醒时长", description="前N个工作日")


class UpdateContactParams(BaseModel):
    """更新联系记录参数"""
    contact_date: str = Field(None, regex=DATE_REGEX, title="联系时间（拜访时间）")
    contact_detail: str = Field(None, title="联系情况说明（拜访情况说明）")
    demand: str = Field(None, title="需求")
    next_contact_date: str = Field(None, regex=DATE_REGEX, title="预约下次拜访时间")
    remind_duration: int = Field(..., gt=0, title="提醒时长", description="前N个工作日")
