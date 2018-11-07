#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/07 19:03
# @Author   : Zhongyuan Sun


def birthdayCakeCandles(ar):
    m = max(ar)
    return ar.count(m)


def main():
    print birthdayCakeCandles([3, 1, 2, 3])


if __name__ == "__main__":
    main()
