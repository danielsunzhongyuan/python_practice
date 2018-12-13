#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/12/14 00:36
# @Author   : Zhongyuan Sun


def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance


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
