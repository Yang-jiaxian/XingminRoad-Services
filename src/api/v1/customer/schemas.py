# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/14
from pydantic import BaseModel, Field
from typing import List
from src.const import CustomerType, DATE_REGEX, Gender, ScaleOfManagement


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
    capital_account: str = Field(..., title="资金账号")
    customer_type: CustomerType = Field(default=CustomerType.individual_customer.value, title="客户类型",
                                        description="默认个人客户")
    name: str = Field(..., title="名字", description="个人客户时是姓名，机构客户时是机构名")
    gender: Gender = Field(Gender.Man.value, title="性别", description="0是男性，1是女性")
    contact_person: str = Field(None, title="联系人")
    phone: str = Field(None, title="联系方式")
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
    remark: str = Field(None, title="备注")

    scale_of_management: ScaleOfManagement = Field(ScaleOfManagement.zero_to_five.value, title="管理规模")
    private_placement_strategy: List[str] = Field(['主观多头', '量化多头', '中性策略', '套利策略', '期货/期权', '多策略'], title="私募的策略类型")
    fund_demand: List[str] = Field(['代销'], title="资金需求")
    technical_demand: List[str] = Field(['是否需要特定柜台', '是否需要极速行情', '是否需要定制化', '是否有三方算法需求'], title="技术需求")
    bond_source_demand: List[str] = Field(['行业篮子股票券源', '宽基篮子股票券源', '个股券源'], title="券源需求")
    investment_research_demand: List[str] = Field(['研究所研报', '研究所白名单', '研究所年费服务', '参与研究所路演', '半年度/年度会议'], title="投研需求")


class UpdateCustomerParams(BaseModel):
    name: str = Field(..., title="名字", description="个人客户时是姓名，机构客户时是机构名")
    gender: Gender = Field(None, title="性别", description="0是男性，1是女性")
    contact_person: str = Field(None, title="联系人")
    phone: str = Field(None, title="联系方式")
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
    remark: str = Field(None, title="备注")

    scale_of_management: ScaleOfManagement = Field(ScaleOfManagement.zero_to_five.value, title="管理规模")
    private_placement_strategy: List[str] = Field(['主观多头', '量化多头', '中性策略', '套利策略', '期货/期权', '多策略'], title="私募的策略类型")
    fund_demand: List[str] = Field(['代销'], title="资金需求")
    technical_demand: List[str] = Field(['是否需要特定柜台', '是否需要极速行情', '是否需要定制化', '是否有三方算法需求'], title="技术需求")
    bond_source_demand: List[str] = Field(['行业篮子股票券源', '宽基篮子股票券源', '个股券源'], title="券源需求")
    investment_research_demand: List[str] = Field(['研究所研报', '研究所白名单', '研究所年费服务', '参与研究所路演', '半年度/年度会议'], title="投研需求")