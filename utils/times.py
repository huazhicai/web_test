# -*- coding:utf-8 -*-
import time
import datetime
from functools import wraps


def timestamp():
    """时间戳"""
    return time.time()


def dt_strftime(fmt="%Y%m%d"):
    """
    datetime格式化时间
    :param fmt "%Y%m%d %H%M%S
    """
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    """
    睡眠时间
    """
    time.sleep(seconds)


def timethis(func):
    """函数运行时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__module__}.{func.__name__} : {end - start}')
        return result

    return wrapper
