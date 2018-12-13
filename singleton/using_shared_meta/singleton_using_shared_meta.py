#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/12/14 00:40
# @Author   : Zhongyuan Sun


# 这种方式勉强算单例，属性是共享的，但是id不同
class Singleton(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        ob = super(Singleton, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob


class MyClass(Singleton):
    a = 1


def main():
    one = MyClass()
    two = MyClass()
    # assert one == two
    # assert one is two
    print id(one), id(two)
    one.a = 2
    print two.a


if __name__ == "__main__":
    main()
