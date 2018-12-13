#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/12/14 00:31
# @Author   : Zhongyuan Sun

try:
    from synchronize import make_synchronized
except ImportError:
    def make_synchronized(func):
        import threading
        func.__lock__ = threading.Lock()

        def synced_func(*args, **kwargs):
            with func.__lock__:
                return func(*args, **kwargs)

        return synced_func


class Singleton(object):
    instance = None

    @make_synchronized
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance


def main():
    one = Singleton()
    two = Singleton()
    assert one == two
    assert one is two
    print id(one), id(two)
    one.a = 2
    print two.a


if __name__ == "__main__":
    main()
