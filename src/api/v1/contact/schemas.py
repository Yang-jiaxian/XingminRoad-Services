# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/15
from typing import List
from src.schemas import StatusCodeResp
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


class CreateContactResp(StatusCodeResp):
    contact_id: int = Field(..., title="联系记录id", description="数据库中的联系记录id")


class FetchContactsResp_Contact(BaseModel):
    id: int = Field(..., title="联系记录ID", description="联系记录ID")
    customer_id: int = Field(..., title="客户ID", description="客户ID")
    contact_date: str = Field(..., title="联系日期", description="联系日期")
    contact_detail: str = Field(..., title="联系详情", description="联系详情")
    demand: str = Field(..., title="需求", description="需求")
    next_contact_date: str = Field(None, regex=DATE_REGEX, title="预约下次联系时间")
    remind_date: str = Field(None, regex=DATE_REGEX, title="提醒时间")


class FetchContactsResp(StatusCodeResp):
    total: int = Field(..., title="命中条数", description="符合条件的记录数")
    data: List[FetchContactsResp_Contact] = Field(..., title="数据")
