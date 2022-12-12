# -*- coding: utf-8 -*-
#
# @Author  : Yang
# @Email  : yangjiaxian@ibbd.net
# @Time    : 2022/12/12
# 个人客户：
data1 = {
  "capital_account": "string",                      # 资金账号   必填
  "customer_type": 0,                               # 客户类型   必填
  "name": "string",                                 # 姓名      必填
  "gender": 0,                                      # 性别
  "phone": "string",                                # 联系方式
  "occupation": "string",                           # 职业
  "birthday": "1761-17-24",                         # 出生年月日
  "certificate_type": "string",                     # 证件类型
  "certificate_number": "string",                   # 证件号码
  "existing_assets": 0,                             # 资产-现有资产
  "historical_peak": 0,                             # 资产-历史峰值
  "customer_source": "string",                      # 客户情况-客户来源
  "specific_channel": "string",                     # 客户情况-具体渠道
  "commission_rate": "string",                      # 佣金费率
  "risk_appetite": "string",                        # 风险偏好
  "developer": "string",                            # 开发关系
  "is_internet_channel": True,                      # 是否是互联网渠道
  "assignmenter": "string",                         # 服务包分配
  "follower": "string",                             # 跟进情况
  "permissions": {                                  # 权限情况
    "cash_treasure": False,
    "automatic_investment_plan": False,
    "double_innovation_board": False,
    "share_option": False,
    "shenzhen_hong_kong_stock_connect": False,
    "shanghai_hong_kong_stock_connect": False,
    "double_margin_account": False,
    "beijing_stock_exchange": False
  },
  "margin_account": "string",                       # 融资融券账号
  "account_opening_date": "2358-7-22",              # 融资融券开户日期
  "preferential_interest_rate": 0,                  # 融资融券优惠利率
  "interest_rate_effective_date": "2852-6-9",       # 融资融券利率生效日期
  "interest_rate_expiry_date": "1441-6-8",          # 融资融券利率失效日期
  "remarks": "string"                               # 备注
}