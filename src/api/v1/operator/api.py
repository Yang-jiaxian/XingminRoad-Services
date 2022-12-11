# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/14
from fastapi import APIRouter, Query, Path, Body

from src.error import InternalException, status
from src.services.operator import OperatorServices
from src.utils import output_json

operator_app = APIRouter(tags=["操作人"])


@operator_app.post("/operators", summary="新增操作人")
async def create_operator_api(
        name: str = Body(..., title="操作人名字"),
        phone: str = Body(..., title="操作人名字"),

):
    operator_id = OperatorServices().create(name, phone)
    return output_json(data={"operator_id": operator_id}, message="新增操作人成功")


@operator_app.delete("/operators/{operatorId}", summary="删除操作人")
async def delete_operator_api(
        operatorId: int = Path(..., title="操作人ID")
):
    result = OperatorServices().fetch_one(operatorId)
    if not result:
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="操作人ID不存在")

    OperatorServices().delete(operatorId)
    return output_json(data={"operator_id": operatorId}, message="删除操作人成功")


@operator_app.get("/operators", summary="获取操作人")
async def fetch_operator_api(
        pageNo: int = Query(None, title="页码", description="非必填，不传获取所有"),
        pageSize: int = Query(None, title="页大小", description="非必填，不传获取所有")
):
    if pageNo is not None:
        assert pageNo > 0
    if pageSize is not None:
        assert pageSize > 0
    total, operators = OperatorServices().fetch_data(pageNo, pageSize)
    return output_json(data=operators, total=total, message="获取操作人成功")
