# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/16
from fastapi import APIRouter, Query, Path, Depends

from src.api.v1.fund.schemas import CreateFundParams, UpdateFundParams, CreateFundResp, FetchFundsResp
from src.error import InternalException, status
from src.services.customer import CustomerServices
from src.services.fund import FundServices
from src.services.log import LogServices
from src.utils import output_json, check_operator

fund_app = APIRouter(tags=["基金"])


@fund_app.post("/funds", summary="新增客户基金数据", response_model=CreateFundResp)
async def create_fund_api(
        params: CreateFundParams,
        operator_id: int = Depends(check_operator)
):
    # 检查客户ID是否存在
    if not CustomerServices().fetch_one(params.customer_id):
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="客户ID不存在")

    # 新增客户基金数据
    fund_id = FundServices().create(**params.dict())

    LogServices().create(operator_id, f"新增了ID为{fund_id}，客户ID为{params.customer_id}的客户基金数据", params.dict())
    return output_json(data={"fund_id": fund_id}, message="")


@fund_app.delete("/funds/{fundId}", summary="删除客户基金数据", response_model=CreateFundResp)
async def delete_fund_api(
        fundId: int = Path(..., title="客户基金数据ID", description="客户基金数据ID"),
        operator_id: int = Depends(check_operator)
):
    result = FundServices().fetch_one(fundId)
    if not result:
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="客户基金数据ID已删除或不存在")

    FundServices().delete(fundId)
    LogServices().create(operator_id, f"删除了ID为{fundId}，客户ID为{result['customer_id']}的客户基金数据")
    return output_json(data={"fund_id": fundId}, message="")


@fund_app.put("/funds/{fundId}", summary="修改客户基金数据", response_model=CreateFundResp)
async def update_fund_api(
        params: CreateFundParams,
        fundId: int = Path(..., title="客户基金数据ID", description="客户基金数据ID"),
        operator_id: int = Depends(check_operator)
):
    result = FundServices().fetch_one(fundId)
    if not result:
        raise InternalException(status.HTTP_601_ID_NOT_EXIST, message="客户基金数据ID已删除或不存在")

    FundServices().update(fundId, **params.dict())

    LogServices().create(operator_id, f"修改了ID为{fundId}的客户基金数据", params.dict())
    return output_json(data={"fund_id": fundId}, message="")


@fund_app.get("/funds", summary="获取客户基金数据", response_model=FetchFundsResp)
async def fetch_fund_api(
        customerId: int = Query(None, title="客户ID", description="客户ID"),
        pageNo: int = Query(1, ge=0, title="页码", description="页码"),
        pageSize: int = Query(20, ge=0, title="页大小", description="页大小"),
        operator_id: int = Depends(check_operator)
):
    total, funds = FundServices().fetch_date(customerId, pageNo, pageSize)
    return output_json(data=funds, total=total, message="")
