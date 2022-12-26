# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/12/26
from pydantic import BaseModel, Field


class FetchlogsResp(BaseModel):
    id: int = Field(..., title="日志ID")
    name: str = Field(..., title="操作人名")
    detail: str = Field(..., title="日志详情")
    is_delete: int = Field(..., title="是否被删除")
    created_at: str = Field(..., title="创建时间")
    updated_at: str = Field(..., title="更新时间")
