#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/09/20 20:32
# @Author   : Zhongyuan Sun


def singleton(cls):
    instances = {}

    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class MyClass:
    def __init__(self, name):
        self.name = name

    def pp(self):
        print self.name


def main():
    a = MyClass("zz")
    a.pp()

    b = MyClass("ii")  # b.name will still be zz
    b.pp()


if __name__ == "__main__":
    main()
