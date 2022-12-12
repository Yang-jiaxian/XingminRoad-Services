# -*- coding: utf-8 -*-
# @Author: Yang jiaxian
# @Date  : 2022/9/19
# @Desc  : 异常处理
# @Email : 499706512@qq.com
from traceback import format_exc
from typing import Any

from fastapi import FastAPI, Request
from fastapi import status as fastapiStatus, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from src.common.logger import logger

SYSTEM_CODE_BASE = 10000

# 状态码基数应该符合这两个条件
assert SYSTEM_CODE_BASE >= 1000
assert SYSTEM_CODE_BASE % 1000 == 0


class status:
    """自定义异常状态码常量，尽量重用http状态码
    """
    # 4XX: 来自客户端错误的响应
    HTTP_400_BAD_REQUEST = fastapiStatus.HTTP_400_BAD_REQUEST
    HTTP_401_UNAUTHORIZED = fastapiStatus.HTTP_401_UNAUTHORIZED
    HTTP_404_NOT_FOUND = fastapiStatus.HTTP_404_NOT_FOUND
    HTTP_422_UNPROCESSABLE_ENTITY = fastapiStatus.HTTP_422_UNPROCESSABLE_ENTITY

    # 5XX：来自服务器端错误的响应
    HTTP_500_INTERNAL_SERVER_ERROR = fastapiStatus.HTTP_500_INTERNAL_SERVER_ERROR

    # 自定义常量值应该取值在600-999
    HTTP_601_ID_NOT_EXIST = 601
    HTTP_622_MYSQL_ERROR = 622


# 状态码对应的异常信息(默认)
messages = {
    # 4XX
    status.HTTP_400_BAD_REQUEST: '客户端请求的语法错误，服务器无法理解',
    status.HTTP_404_NOT_FOUND: '请求的资源无法找到',
    status.HTTP_401_UNAUTHORIZED: '权限校验不通过',
    status.HTTP_422_UNPROCESSABLE_ENTITY: '请求参数不通过',
    # 5XX
    status.HTTP_500_INTERNAL_SERVER_ERROR: '服务器内部错误，无法完成请求',
    status.HTTP_601_ID_NOT_EXIST: "请求ID不存在",
    status.HTTP_622_MYSQL_ERROR: 'SQL执行失败'

}


def get_status():
    """获取接口状态值列表"""
    data = [{'code': status.__dict__[key] + SYSTEM_CODE_BASE,
             'message': messages[status.__dict__[key]]}
            for key in status.__dict__ if key.startswith('HTTP_')]
    data = sorted(data, key=lambda x: x['code'])
    return data


class BaseException(HTTPException):
    """自定义异常基类
    程序内部抛出的异常应该给予该基类
    """

    def __init__(self, code: int, message: str = None, detail: Any = None) -> None:
        self.code = code
        self.message = message
        if not self.message:
            self.message = messages.get(code)
        status_code = code if code < 600 else fastapiStatus.HTTP_500_INTERNAL_SERVER_ERROR
        super().__init__(status_code, detail)

    def __str__(self) -> str:
        return f"code={self.code} message={self.message} data={self.detail}"


class InternalException(BaseException):
    """内部错误异常"""

    def __str__(self) -> str:
        """为了celery保存的格式"""
        return f"code={self.code + SYSTEM_CODE_BASE} message={self.message} detail={self.detail}"


class ErrorResponse(JSONResponse):
    """接口异常响应类型
    异常时可以指定一个状态，这个状态码应该尽量重用http标准的状态码，
    对于超过范围的值，可以定义到600到999的范围，大于等于600的时候，
    在响应时会自动重置为500.
    响应给前端的异常信息结构(假设SYSTEM_CODE_BASE的值为1000)：
    Example1:
    {
        "code": 10401,
        "message": "这是自定义错误信息"
    }
    这时http响应的状态码应该时401
    Example2:
    {
        "code": 10602,
        "message": "这是自定义错误信息"
    }
    这时http响应的状态码应该时500（大于等于600时自动重置为500）
    其中：
    code值是完整的异常状态码，message是异常描述信息。
    """

    def __init__(self, code: int, message: str = None, detail: Any = None) -> None:
        """
        :param code 响应状态码，取值0-999，若该值大于等于600，则http code会自动重置为500
        :param message 异常信息，如果该值为空，则会默认为code值对应的异常信息
        :param detail 详细的异常信息，通常用于开发者排除定位问题使用
        """
        # assert 0 <= code < 1000
        # http的状态码大于600会报错，超过600响应为内部错误
        status_code = code if code < 600 else 500
        if message is None:
            message = messages.get(code)
        super().__init__(status_code=status_code,
                         content={"code": code + SYSTEM_CODE_BASE, 'message': message, 'data': {"detail": detail}})


def init_exception(app: FastAPI):
    """初始化异常处理"""

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc: Exception):
        """请求参数校验不通过"""
        logger.error(f'{request.client.host}:{request.client.port} - '
                     f'"{request.method.upper()} {request.url.path}"  {status.HTTP_500_INTERNAL_SERVER_ERROR} ')
        logger.error(f'请求参数校验不通过')
        return ErrorResponse(status.HTTP_400_BAD_REQUEST, message='请求参数校验不通过', detail=str(exc))

    @app.exception_handler(ValidationError)
    async def resp_validation_exception_handler(request, exc: Exception):
        """响应值参数校验不通过"""
        logger.error(f'{request.client.host}:{request.client.port} - '
                     f'"{request.method.upper()} {request.url.path}"  {status.HTTP_500_INTERNAL_SERVER_ERROR} ')
        logger.error(f'请求参数校验不通过')
        return ErrorResponse(status.HTTP_500_INTERNAL_SERVER_ERROR, message='响应参数校验不通过', detail=str(exc))

    @app.exception_handler(InternalException)
    async def base_exception_handler(request, exc: InternalException):
        """捕获自定义异常"""
        logger.error(f'{request.client.host}:{request.client.port} - '
                     f'"{request.method.upper()} {request.url.path}"  {status.HTTP_500_INTERNAL_SERVER_ERROR} ')
        logger.error(format_exc())
        return ErrorResponse(exc.code, message=exc.message, detail=exc.detail)

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc: HTTPException):
        """捕获FastAPI异常"""
        logger.error(f'{request.client.host}:{request.client.port} - '
                     f'"{request.method.upper()} {request.url.path}"  {status.HTTP_500_INTERNAL_SERVER_ERROR} ')
        logger.error(format_exc())
        return ErrorResponse(exc.status_code, message=str(exc.detail), detail=exc.detail)

    @app.exception_handler(Exception)
    async def allexception_handler(request: Request, exc: Exception):
        """捕获所有其他的异常"""
        logger.error(f'{request.client.host}:{request.client.port} - '
                     f'"{request.method.upper()} {request.url.path}"  {status.HTTP_500_INTERNAL_SERVER_ERROR} ')
        logger.error(format_exc())
        return ErrorResponse(status.HTTP_500_INTERNAL_SERVER_ERROR,
                             message=messages.get(status.HTTP_500_INTERNAL_SERVER_ERROR),
                             detail=str(exc))


if __name__ == "__main__":
    import traceback

    DEBUG = True
    try:
        try:
            1 / 0
        except Exception as e:
            detail = traceback.format_exc()
            raise InternalException(status.HTTP_500_INTERNAL_SERVER_ERROR, message='错误', detail=detail)
    except Exception as e:
        print(str(e))
    pass
    # resp = ErrorResponse(status.HTTP_403_FORBIDDEN, message='接口请求参数错误')
    # print(resp.body)

    # try:
    #     raise InternalException(status.xx, message=messages[status.xx])
    # except InternalException as e:
    #     print(e.code, e.message, e.detail)
    # resp = ErrorResponse(e.code)
    # print(resp.body)
