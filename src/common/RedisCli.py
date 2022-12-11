# -*- coding: utf-8 -*-
# @Author: Yang jiaxian
# @Date  : 2022/12/12
# @Desc  :
# @Email : 499706512@qq.com
import sys
from redis import Redis, AuthenticationError
from src.common.logger import logger
from src.utils.utils import flyweight


@flyweight
class RedisCli(object):

    def __init__(self, config):
        try:
            self._redis_client = Redis(
                host=config["host"],
                port=config["port"],
                password=config["password"],
                db=config["db"],
                socket_timeout=config["socket_timeout"],
                decode_responses=True  # 解码
            )
            if not self._redis_client.ping():
                logger.info("连接redis超时")
                sys.exit()
            logger.info("连接上了")
        except (AuthenticationError, Exception) as e:
            logger.info(f"连接redis异常 {e}")
            sys.exit()

    # 使实例化后的对象 赋予redis对象的的方法和属性
    def __getattr__(self, name):
        return getattr(self._redis_client, name)

    def __getitem__(self, name):
        return self._redis_client[name]

    def __setitem__(self, name, value):
        self._redis_client[name] = value

    def __delitem__(self, name):
        del self._redis_client[name]


if __name__ == '__main__':
    import time

    MYCONFIG2 = {
        "host": "127.0.0.1",
        "port": 6379,
        "password": "",
        "db": 2,
        "socket_timeout": 5
    }

    MYCONFIG3 = {
        "host": "127.0.0.1",
        "port": 6379,
        "password": "",
        "db": 3,
        "socket_timeout": 5
    }
    _time = time.time()
    for _ in range(10000):
        redis2: Redis = RedisCli(MYCONFIG2)
        # redis3: Redis = RedisCli(MYCONFIG3)
        redis2.set("test", "asdfasdf", 151)
        # redis3.set("test", "asdfasdf", 151)
    print(time.time() - _time)