#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/12/13 21:32
# @Author   : Zhongyuan Sun


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
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
