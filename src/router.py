# -*- coding: utf-8 -*-
# @Author: Yang jiaxian
# @Date  : 2022/9/19
# @Desc  : 全局路由管理
# @Email : 499706512@qq.com
from settings import settings
from src.api.v1.customer.api import customer_app
from src.api.v1.operator.api import operator_app
from src.api.v1.contact.api import contact_app
from src.api.v1.fund.api import fund_app
from src.api.v1.cooperation.api import cooperation_app


def include_routers(app):
    app.include_router(customer_app, prefix=settings.API_PREFIX)
    app.include_router(contact_app, prefix=settings.API_PREFIX)
    app.include_router(fund_app, prefix=settings.API_PREFIX)
    app.include_router(operator_app, prefix=settings.API_PREFIX)
    app.include_router(cooperation_app, prefix=settings.API_PREFIX)
