#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/12/13 21:35
# @Author   : Zhongyuan Sun

from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class MyClass(object):
    a = 1


def main():
    one = MyClass()
    two = MyClass()
    assert one == two
    assert one is two
    print id(one), id(two)
    one.a = 2
    print two.a


if __name__ == "__main__":
    main()
