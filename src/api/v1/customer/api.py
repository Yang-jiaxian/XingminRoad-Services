# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/14

import json

from fastapi import APIRouter, Path, Query, Depends

from src.api.v1.customer.schemas import CreateCustomerParams, UpdateCustomerParams
from src.const import CustomerType
from src.error import InternalException, status
from src.services.customer import CustomerServices
from src.services.log import LogServices
from src.utils import output_json, check_operator

customer_app = APIRouter(tags=["客户"])


@customer_app.post("/customers", summary="新增客户")
async def create_customer_api(
        params: CreateCustomerParams,
        operator_id: int = Depends(check_operator)
):

    if params.permissions:
        params.permissions = json.dumps(params.permissions.dict())

    # 个人客户
    if params.customer_type.value == CustomerType.individual_customer.value:
        if params.gender is None:
            raise InternalException(status.HTTP_422_UNPROCESSABLE_ENTITY, message="缺少性别参数")
        if params.assignmenter:
            if not params.developer:
                raise InternalException(status.HTTP_422_UNPROCESSABLE_ENTITY, message="缺少开发关系参数")
            if params.assignmenter != params.developer:
                raise InternalException(status.HTTP_422_UNPROCESSABLE_ENTITY, message="服务包分配应该和开发关系一致")
        params.scale_of_management = None
        params.private_placement_strategy = None
        params.fund_demand = None
        params.technical_demand = None
        params.bond_source_demand = None
        params.investment_research_demand = None

    # 机构客户
    if params.customer_type.value == CustomerType.institutional_customer.value:
        if not params.contact_person:
            raise InternalException(status.HTTP_422_UNPROCESSABLE_ENTITY, message="缺少联系人参数")

    params.customer_type = params.customer_type.value
    params.gender = params.gender.value
    customer_id = CustomerServices().create(**params.dict())

    LogServices().create(operator_id, f"新增了ID为{customer_id}的客户", params.dict())
    return output_json(data={"customer_id": customer_id}, message="新增客户成功")


@customer_app.put(path="/customers/{customerId}", summary="修改客户信息")
async def update_customer_api(
        params: UpdateCustomerParams,
        customerId: int = Path(..., title="客户ID"),
        operator_id: int = Depends(check_operator)

):
    # 检查客户ID是否存在
    if not CustomerServices().fetch_one(customerId):
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="客户ID不存在")

    if params.permissions:
        params.permissions = json.dumps(params.permissions.dict())
    if params.customer_type:
        params.customer_type = params.customer_type.value

    # kwargs = {k: v for k, v in params.dict().items() if v is not None}
    # if not kwargs:
    #     return output_json(data={"customer_id": customerId}, message="修改客户数据成功")

    CustomerServices().update(customerId, **params.dict())

    LogServices().create(operator_id, f"修改了ID为{customerId}的客户", params.dict())
    return output_json(data={"customer_id": customerId}, message="修改客户数据成功")


@customer_app.delete(path="/customers/{customerId}", summary="删除客户")
async def delete_customer_api(
        customerId: int = Path(..., title="客户ID"),
        operator_id: int = Depends(check_operator)
):
    # 检查客户ID是否存在
    if not CustomerServices().fetch_one(customerId):
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="客户ID不存在")

    CustomerServices().delete(customerId)

    LogServices().create(operator_id, f"删除了ID为{customerId}的客户")
    return output_json(data={"customer_id": customerId}, message="删除客户成功")


@customer_app.get(path="/customers", summary="查询客户")
async def fetch_customer_api(
        customer_id: int = Query(None, title="客户ID"),
        capital_account: str = Query(None, title="资金账号"),
        customer_type: CustomerType = Query(None, title="客户类型"),
        name: str = Query(None, title="名称"),
        contact_person: str = Query(None, title="联系人"),
        phone: str = Query(None, title="联系方式"),
        developer: str = Query(None, title="开发关系（开发人）"),
        assignmenter: str = Query(None, title="服务包分配"),
        is_internet_channel: bool = Query(None, title="是否是互联网渠道"),
        follower: str = Query(None, title="跟进情况"),
        margin_account: str = Query(None, title="融资融券账号"),

        contact_remind: bool = Query(None, title="联系提醒"),
        fund_expire_remind: bool = Query(None, title="基金到期提醒"),
        interest_rate_expiry_remind: bool = Query(None, title="融资融券利率失效提醒"),

        pageNo: int = Query(None, title="页码", description="非必填，不传获取所有"),
        pageSize: int = Query(None, title="页大小", description="非必填，不传获取所有")
):
    pass
