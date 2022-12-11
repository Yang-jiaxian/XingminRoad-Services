# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/15
from pydantic import BaseModel, Field
from src.const import RemindFreq, DATE_REGEX


class CreateContactParams(BaseModel):
    customer_id: int = Field(..., title="客户ID")
    contact_date: str = Field(..., regex=DATE_REGEX, title="联系时间（拜访时间）")
    contact_detail: str = Field(..., title="联系详情（拜访内容）")
    demand: str = Field(None, title="需求")
    next_contact_date: str = Field(..., regex=DATE_REGEX, title="预约下次拜访时间")
    remind_freq: RemindFreq = Field(..., title="提醒频率")


class UpdateContactParams(BaseModel):
    contact_date: str = Field(None, regex=DATE_REGEX, title="联系时间（拜访时间）")
    contact_detail: str = Field(None, title="联系详情（拜访内容）")
    demand: str = Field(None, title="需求")
    next_contact_date: str = Field(None, regex=DATE_REGEX, title="预约下次拜访时间")
    remind_freq: RemindFreq = Field(None, title="提醒频率")
