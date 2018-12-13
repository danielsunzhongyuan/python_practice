#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/12/13 21:29
# @Author   : Zhongyuan Sun


class MySingleton(object):
    def foo(self):
        print "singleton using module"


my_singleton = MySingleton()


def main():
    pass


if __name__ == "__main__":
    main()
