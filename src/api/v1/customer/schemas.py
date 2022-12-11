# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/14
from pydantic import BaseModel, Field
from src.const import CustomerType, DATE_REGEX


class Permissions(BaseModel):
    cash_treasure: bool = Field(False, title="现金宝")
    automatic_investment_plan: bool = Field(False, title="基金定投", description="AIP")
    double_innovation_board: bool = Field(False, title="双创板")
    share_option: bool = Field(False, title="期权")
    shenzhen_hong_kong_stock_connect: bool = Field(False, title="深港通")
    shanghai_hong_kong_stock_connect: bool = Field(False, title="沪港通")
    double_margin_account: bool = Field(False, title="两融账户")
    beijing_stock_exchange: bool = Field(False, title="北交所")


class CreateCustomerParams(BaseModel):
    capital_account: str = Field(None, title="资金账号")
    customer_type: CustomerType = Field(default=CustomerType.individual_customer, title="客户类型", description="默认个人客户")
    name: str = Field(None, title="名字", description="个人客户时是姓名，机构客户时是机构名")
    gender: int = Field(None, title="性别", description="0是男性，1是女性")
    phone: str = Field(None, title="手机")
    occupation: str = Field(None, title="职业")
    birthday: str = Field(None, regex=DATE_REGEX, title="出生年月日")
    certificate_type: str = Field(None, title="证件类型")
    certificate_number: str = Field(None, title="证件号码")
    existing_assets: int = Field(None, title="资产-现有资产")
    historical_peak: int = Field(None, title="资产-历史峰值")
    customer_source: str = Field(None, title="客户情况-客户来源")
    specific_channel: str = Field(None, title="客户情况-具体渠道")
    commission_rate: str = Field(None, title="佣金费率")
    risk_appetite: str = Field(None, title="风险偏好")
    developer: str = Field(None, title="开发关系", description="应该是一个人名")
    is_internet_channel: bool = Field(None, title="是否是互联网渠道")
    assignmenter: str = Field(None, title="服务包分配", description="应该是一个人名")
    follower: str = Field(None, title="跟进情况", description="应该是一个人名")
    permissions: Permissions = Field(None, title="开发关系")
    margin_account: str = Field(None, title="融资融券账号")
    account_opening_date: str = Field(None, regex=DATE_REGEX, title="融资融券开户日期")
    preferential_interest_rate: float = Field(None, title="融资融券优惠利率")
    interest_rate_effective_date: str = Field(None, regex=DATE_REGEX, title="融资融券优惠利率生效日期")
    interest_rate_expiry_date: str = Field(None, regex=DATE_REGEX, title="融资融券优惠利率失效日期")
    remarks: str = Field(None, title="融资融券-备注")


class UpdateCustomerParams(BaseModel):
    capital_account: str = Field(None, title="资金账号")
    customer_type: CustomerType = Field(None, title="客户类型", description="默认个人客户")
    name: str = Field(None, title="名字", description="个人客户时是姓名，机构客户时是机构名")
    gender: int = Field(None, title="性别", description="0是男性，1是女性")
    phone: str = Field(None, title="手机")
    occupation: str = Field(None, title="职业")
    birthday: str = Field(None, regex=DATE_REGEX, title="出生年月日")
    certificate_type: str = Field(None, title="证件类型")
    certificate_number: str = Field(None, title="证件号码")
    existing_assets: int = Field(None, title="资产-现有资产")
    historical_peak: int = Field(None, title="资产-历史峰值")
    customer_source: str = Field(None, title="客户情况-客户来源")
    specific_channel: str = Field(None, title="客户情况-具体渠道")
    commission_rate: str = Field(None, title="佣金费率")
    risk_appetite: str = Field(None, title="风险偏好")
    developer: str = Field(None, title="开发关系", description="应该是一个人名")
    is_internet_channel: bool = Field(None, title="是否是互联网渠道")
    assignmenter: str = Field(None, title="服务包分配", description="应该是一个人名")
    follower: str = Field(None, title="跟进情况", description="应该是一个人名")
    permissions: Permissions = Field(None, title="开发关系")
    margin_account: str = Field(None, title="融资融券账号")
    account_opening_date: str = Field(None, regex=DATE_REGEX, title="融资融券开户日期")
    preferential_interest_rate: float = Field(None, title="融资融券优惠利率")
    interest_rate_effective_date: str = Field(None, regex=DATE_REGEX, title="融资融券优惠利率生效日期")
    interest_rate_expiry_date: str = Field(None, regex=DATE_REGEX, title="融资融券优惠利率失效日期")
    remarks: str = Field(None, title="融资融券-备注")
