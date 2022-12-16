# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/12/12
from fastapi import APIRouter, Query, Path, Depends

from src.api.v1.cooperation.schemas import CreateCooperationParams, UpdateCooperationParams
from src.error import InternalException, status
from src.services.cooperation import CooperationServices
from src.services.customer import CustomerServices
from src.services.log import LogServices
from src.utils import output_json, check_operator

cooperation_app = APIRouter(tags=["合作券商"])


@cooperation_app.post("/cooperations", summary="新增合作券商")
async def create_cooperation_api(
        params: CreateCooperationParams,
        operator_id: int = Depends(check_operator)

):
    # 检查客户ID是否存在
    if not CustomerServices().fetch_one(params.customer_id):
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="客户ID不存在")

    # 新增合作券商
    cooperation_id = CooperationServices().create(**params.dict())

    log = LogServices()
    log.create(operator_id, f"新增了ID为{cooperation_id}，客户ID为{params.customer_id}的合作券商", params.dict())
    return output_json(data={"cooperation_id": cooperation_id}, message="新增合作券商成功")


@cooperation_app.delete("/cooperations/{cooperationId}", summary="删除合作券商")
async def delete_cooperation_api(
        cooperationId: int = Path(..., title="合作券商ID"),
        operator_id: int = Depends(check_operator)
):
    result = CooperationServices().fetch_one(cooperationId)
    if not result:
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="合作券商ID已删除或不存在")

    # 删除合作券商
    CooperationServices().delete(cooperationId)

    LogServices().create(operator_id, f"删除了ID为{cooperationId}，客户ID为{result['customer_id']}的合作券商")
    return output_json(data={"cooperation_id": cooperationId}, message="删除合作券商成功")


@cooperation_app.put("/cooperations/{cooperationId}", summary="修改合作券商")
async def update_cooperation_api(
        params: UpdateCooperationParams,
        cooperationId: int = Path(..., title="合作券商ID"),
        operator_id: int = Depends(check_operator)

):
    result = CooperationServices().fetch_one(cooperationId)
    if not result:
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="合作券商ID已删除或不存在")

    CooperationServices().update(cooperationId, **params.dict())

    LogServices().create(operator_id, f"修改了ID为{cooperationId}的合作券商", params.dict())
    return output_json(data={"cooperation_id": cooperationId}, message="修改合作券商成功")


@cooperation_app.get("/cooperations", summary="获取合作券商")
async def fetch_cooperation_api(
        customerId: int = Query(None, title="客户ID"),
        pageNo: int = Query(1, ge=0, title="页码"),
        pageSize: int = Query(20, ge=0, title="页大小")
):
    if pageNo is not None:
        assert pageNo > 0
    if pageSize is not None:
        assert pageSize > 0

    total, cooperations = CooperationServices().fetch_date(customerId, pageNo, pageSize)
    return output_json(data=cooperations, total=total, message="获取合作券商成功")
