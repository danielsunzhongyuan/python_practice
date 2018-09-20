#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/09/20 20:28
# @Author   : Zhongyuan Sun


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class MyClass(object):
    __metaclass__ = Singleton

    def __init__(self, name):
        self.name = name

    def pp(self):
        print self.name


def main():
    a = MyClass("xx")
    a.pp()
    b = MyClass("yy")  # b.name will still be xx
    b.pp()


if __name__ == "__main__":
    main()
