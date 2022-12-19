# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/14
import datetime
import json

from fastapi import APIRouter, Path, Query, Depends

from src.api.v1.customer.schemas import CreateCustomerParams, UpdateCustomerParams, GetRemindCustomersCountResp, \
    CreateCustomerResp, FetchCustomersResp
from typing import Optional
from src.const import CustomerType, RemindType
from src.error import InternalException, status
from src.services.customer import CustomerServices
from src.services.log import LogServices
from src.utils import output_json, check_operator

customer_app = APIRouter(tags=["客户"])


@customer_app.post("/customers", summary="新增客户", response_model=CreateCustomerResp)
async def create_customers_api(
        params: CreateCustomerParams,
        operator_id: int = Depends(check_operator)
):
    if params.permissions:
        params.permissions = json.dumps(params.permissions.dict())
    if params.private_placement_strategy:
        params.private_placement_strategy = json.dumps(params.private_placement_strategy.dict())
    if params.fund_demand:
        params.fund_demand = json.dumps(params.fund_demand.dict())
    if params.technical_demand:
        params.technical_demand = json.dumps(params.technical_demand.dict())
    if params.bond_source_demand:
        params.bond_source_demand = json.dumps(params.bond_source_demand.dict())
    if params.investment_research_demand:
        params.investment_research_demand = json.dumps(params.investment_research_demand.dict())

    # 个人客户
    if params.customer_type.value == CustomerType.individual_customer.value:
        if params.gender is None:
            raise InternalException(status.HTTP_422_UNPROCESSABLE_ENTITY, message="缺少性别参数")
        if params.assignmenter:
            if not params.developer:
                raise InternalException(status.HTTP_422_UNPROCESSABLE_ENTITY, message="缺少开发关系参数")
            if params.assignmenter != params.developer:
                raise InternalException(status.HTTP_422_UNPROCESSABLE_ENTITY, message="服务包分配应该和开发关系一致")
        # 清空这些机构客户选项
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
    # 处理枚举类型
    params.customer_type = params.customer_type.value
    params.gender = params.gender.value
    customer_id = CustomerServices().create(**params.dict())

    LogServices().create(operator_id, f"新增了ID为{customer_id}的客户", params.dict())
    return output_json(data={"customer_id": customer_id}, message="")


@customer_app.put(path="/customers/{customerId}", summary="修改客户信息", response_model=CreateCustomerResp)
async def update_customer_api(
        params: UpdateCustomerParams,
        customerId: int = Path(..., title="客户ID", description="客户ID"),
        operator_id: int = Depends(check_operator)

):
    # 检查客户ID是否存在
    if not CustomerServices().fetch_one(customerId):
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="客户ID不存在")

    if params.permissions:
        params.permissions = json.dumps(params.permissions.dict())
    if params.customer_type:
        params.customer_type = params.customer_type.value

    CustomerServices().update(customerId, **params.dict())

    LogServices().create(operator_id, f"修改了ID为{customerId}的客户", params.dict())
    return output_json(data={"customer_id": customerId}, message="")


@customer_app.delete(path="/customers/{customerId}", summary="删除客户", response_model=CreateCustomerResp)
async def delete_customer_api(
        customerId: int = Path(..., title="客户ID", description="客户ID"),
        operator_id: int = Depends(check_operator)
):
    # 检查客户ID是否存在
    if not CustomerServices().fetch_one(customerId):
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="客户ID不存在")

    CustomerServices().delete(customerId)

    LogServices().create(operator_id, f"删除了ID为{customerId}的客户")
    return output_json(data={"customer_id": customerId}, message="删除客户成功")


@customer_app.get(path="/customers/remind/count", summary="获取提醒的客户数量", response_model=GetRemindCustomersCountResp)
async def get_remind_customers_count_api(
        operator_id: int = Depends(check_operator)
):
    today = str(datetime.datetime.today().date())
    data = CustomerServices().get_remind_customers_count(today)
    return output_json(data=data, message="")


@customer_app.get(path="/customers", summary="查询客户", response_model=FetchCustomersResp)
async def fetch_customers_api(
        customer_id: int = Query(None, title="客户ID", description="客户ID"),
        capital_account: str = Query(None, title="资金账号", description="资金账号"),
        customer_type: CustomerType = Query(None, title="客户类型", description="客户类型"),
        name: str = Query(None, title="名称", description="名称/名字"),
        contact_person: str = Query(None, title="联系人", description="联系人（人名）"),
        phone: str = Query(None, title="联系方式（手机号码）", description="联系方式（手机号码）"),
        developer: str = Query(None, title="开发关系（开发人）", description="开发关系（开发人）"),
        assignmenter: str = Query(None, title="服务包分配", description="服务包分配"),
        follower: str = Query(None, title="跟进情况", description="跟进情况"),
        is_internet_channel: bool = Query(None, title="是否是互联网渠道", description="是否是互联网渠道"),
        margin_account: str = Query(None, title="融资融券账号", description="融资融券账号"),
        remind_type: Optional[RemindType] = Query(None, title="提醒的类型", description="提醒的类型, 不填就不过滤"),
        pageNo: int = Query(1, ge=0, title="页码", description="页码"),
        pageSize: int = Query(20, ge=0, title="页大小", description="页大小"),
        operator_id: int = Depends(check_operator)
):
    """
    提醒类型（三种）：融资融券失效客户、基金到期客户、需要联系的客户\n
    说明：这种提醒类型配合客户类型查询出符合条件的客户
    """
    total, data = CustomerServices().fetch_data(remind_type, customer_id, capital_account, customer_type, name,
                                                contact_person,
                                                phone, developer, assignmenter, is_internet_channel, follower,
                                                margin_account,
                                                pageNo, pageSize)
    return output_json(data=data, message='', total=total)
