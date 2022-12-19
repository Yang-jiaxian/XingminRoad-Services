# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/15
from fastapi import APIRouter, Query, Path, Depends

from src.api.v1.contact.schemas import CreateContactParams, UpdateContactParams
from src.error import InternalException, status
from src.services.contact import ContactServices
from src.services.customer import CustomerServices
from src.services.log import LogServices
from src.utils import output_json, check_operator

contact_app = APIRouter(tags=["联系记录"])


@contact_app.post("/contacts", summary="新增联系记录")
async def create_contact_api(
        params: CreateContactParams,
        operator_id: int = Depends(check_operator)

):
    # 检查客户ID是否存在
    if not CustomerServices().fetch_one(params.customer_id):
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="客户ID不存在")

    # 新增联系记录
    _dict = params.dict().copy()
    _dict.update({"operator_id": operator_id})
    contact_id = ContactServices().create(**_dict)

    # 修改客户的联系状态
    CustomerServices().update_contact_status(params.customer_id)

    log = LogServices()
    log.create(operator_id, f"新增了ID为{contact_id}，客户ID为{params.customer_id}的联系记录", params.dict())
    return output_json(data={"contact_id": contact_id}, message="新增联系记录成功")


@contact_app.delete("/contacts/{contactId}", summary="删除联系记录")
async def delete_contact_api(
        contactId: int = Path(..., title="联系记录ID", description="联系记录ID"),
        operator_id: int = Depends(check_operator)
):
    result = ContactServices().fetch_one(contactId)
    if not result:
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="联系记录ID已删除或不存在")

    ContactServices().delete(contactId)
    # 修改客户的联系状态
    CustomerServices().update_contact_status(result["customer_id"])

    LogServices().create(operator_id, f"删除了ID为{contactId}，客户ID为{result['customer_id']}的联系记录")
    return output_json(data={"contact_id": contactId}, message="删除联系记录成功")


@contact_app.put("/contacts/{contactId}", summary="修改联系记录")
async def update_contact_api(
        params: UpdateContactParams,
        contactId: int = Path(..., title="联系记录ID", description="联系记录ID"),
        operator_id: int = Depends(check_operator)

):
    result = ContactServices().fetch_one(contactId)
    if not result:
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="联系记录ID已删除或不存在")

    ContactServices().update(contactId, **params.dict())

    LogServices().create(operator_id, f"修改了ID为{contactId}的联系记录", params.dict())
    return output_json(data={"contact_id": contactId}, message="修改联系记录成功")


@contact_app.get("/contacts", summary="获取联系记录")
async def fetch_contact_api(
        customerId: int = Query(None, title="客户ID", description="客户ID"),
        pageNo: int = Query(1, ge=0, title="页码", description="页码"),
        pageSize: int = Query(20, ge=0, title="页大小", description="页大小"),
        operator_id: int = Depends(check_operator)
):
    total, contacts = ContactServices().fetch_date(customerId, pageNo, pageSize)
    return output_json(data=contacts, total=total, message="获取联系记录成功")
