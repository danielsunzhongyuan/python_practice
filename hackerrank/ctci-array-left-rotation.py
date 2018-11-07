#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/06 19:54
# @Author   : Zhongyuan Sun


def rotLeft(a, d):
    length = len(a)
    reverse(a, 0, d - 1)
    reverse(a, d, length - 1)
    reverse(a, 0, length - 1)
    return a


def reverse(a, i, j):
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


def main():
    print rotLeft([1, 2, 3, 4, 5], 4)


if __name__ == "__main__":
    main()
