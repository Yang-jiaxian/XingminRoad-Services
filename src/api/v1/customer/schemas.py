# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/11/14
from typing import List
from pydantic import BaseModel, Field
from src.schemas import StatusCodeResp
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


class PrivatePlacementStrategy(BaseModel):
    """私募的策略类型

    """
    subjective_long_position: bool = Field(False, title="主观多头")
    quantifying_long_positions: bool = Field(False, title="量化多头")
    neutral_strategy: bool = Field(False, title="中性策略")
    arbitrage_strategy: bool = Field(False, title="套利策略")
    forward_option: bool = Field(False, title="期货/期权")
    multi_strategy: bool = Field(False, title="多策略")
    other: str = Field(None, title="其他")


class FundDemand(BaseModel):
    """资金需求

    """
    sale_by_proxy: bool = Field(False, title="代销")
    other: str = Field(None, title="其他")


class TechnicalDemand(BaseModel):
    """技术需求

    """
    is_need_specific_counter: bool = Field(False, title="是否需要特定柜台")
    is_need_top_speed_market: bool = Field(False, title="是否需要极速行情")
    is_need_customization: bool = Field(False, title="是否需要定制化")
    is_need_tripartite_algorithms: bool = Field(False, title="是否有三方算法需求")


class BondSourceDemand(BaseModel):
    """券源需求

    """
    sector_basket_stocks: bool = Field(False, title="行业篮子股票券源")
    wide_base_basket_stocks: bool = Field(False, title="宽基篮子股票券源")
    individual_share: bool = Field(False, title="个股券源")
    other: str = Field(None, title="其他")


class InvestmentResearchDemand(BaseModel):
    """投研需求

    """
    research_report_of_the_institute: bool = Field(False, title="研究所研报")
    research_institute_whitelist: bool = Field(False, title="研究所白名单")
    institute_annual_fee_service: bool = Field(False, title="研究所年费服务")
    participate_in_the_institute_road_show: bool = Field(False, title="参与研究所路演")
    annual_meeting: bool = Field(False, title="半年度/年度会议")
    other: str = Field(None, title="其他")


class CreateCustomerParams(BaseModel):
    capital_account: str = Field(..., title="资金账号", description="个人客户是资金账号，机构客户是私募编码")
    customer_type: CustomerType = Field(default=CustomerType.individual_customer.value, title="客户类型",
                                        description="0是个人客户，1是机构客户，默认个人客户")
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
    private_placement_strategy: PrivatePlacementStrategy = Field(None, title="私募的策略类型")
    fund_demand: FundDemand = Field(None, title="资金需求")
    technical_demand: TechnicalDemand = Field(None, title="技术需求")
    bond_source_demand: BondSourceDemand = Field(None, title="券源需求")
    investment_research_demand: InvestmentResearchDemand = Field(None, title="投研需求")


class CreateCustomerResp(StatusCodeResp):
    customer_id: int = Field(..., title="客户id", description="数据库中的id")


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
    private_placement_strategy: PrivatePlacementStrategy = Field(None, title="私募的策略类型")
    fund_demand: FundDemand = Field(None, title="资金需求")
    technical_demand: TechnicalDemand = Field(None, title="技术需求")
    bond_source_demand: BondSourceDemand = Field(None, title="券源需求")
    investment_research_demand: InvestmentResearchDemand = Field(None, title="投研需求")


class GetRemindCustomersCountResp_IndividualCustomer(BaseModel):
    interest_rate_expiry_customers_count: int = Field(0, title="利率失效客户数")
    fund_expiry_customers_count: int = Field(0, title="基金过期客户数")
    need_to_contact_customers_count: int = Field(0, title="需要联系客户数")


class GetRemindCustomersCountResp(StatusCodeResp):
    individual_customer: GetRemindCustomersCountResp_IndividualCustomer = Field(..., title="个人客户")
    institutional_customer: GetRemindCustomersCountResp_IndividualCustomer = Field(..., title="机构客户")


class FetchCustomersResp_Customer(BaseModel):
    id: int = Field(..., title="客户ID", description="客户ID")
    capital_account: str = Field(..., title="资金账号", description="资金账号")
    customer_type: int = Field(..., title="客户类型", description="0是个人客户，1是机构客户")
    name: str = Field(..., title="名字", description="个人客户是名字，机构客户时是机构名")
    gender: int = Field(..., title="性别", description="0是男性，1是女性")
    contact_person: str = Field(..., title="联系人", description="机构客户才需要填写的字段，机构的联系人")
    phone: str = Field(..., title="联系方式", description="手机号码")
    occupation: str = Field(..., title="职业", description="职业")
    birthday: str = Field(..., title="出生年月日", description="出生年月日")
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
    scale_of_management: ScaleOfManagement = Field(None, title="管理规模")
    private_placement_strategy: PrivatePlacementStrategy = Field({}, title="私募的策略类型")
    fund_demand: FundDemand = Field({}, title="资金需求")
    technical_demand: TechnicalDemand = Field({}, title="技术需求")
    bond_source_demand: BondSourceDemand = Field({}, title="券源需求")
    investment_research_demand: InvestmentResearchDemand = Field({}, title="投研需求")

    operator_id: int = Field(..., title="创建此客户的操作人ID")
    is_delete: int = Field(..., title="是否删除")
    created_at: str = Field(..., title="创建时间")
    updated_at: str = Field(..., title="更新时间")


class FetchCustomersResp(StatusCodeResp):
    total: int = Field(..., title="命中条数", description="符合条件的记录数")
    data: List[FetchCustomersResp_Customer] = Field(..., title="数据")
