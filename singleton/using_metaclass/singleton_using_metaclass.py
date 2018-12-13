#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/12/13 23:07
# @Author   : Zhongyuan Sun


# 注意这里的 Singleton 继承自 type，而不是 object
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(object):
    __metaclass__ = Singleton
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
