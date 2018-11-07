#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/06 19:37
# @Author   : Zhongyuan Sun


def compareTriplets(a, b):
    result = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            result[0] += 1
        elif a[i] < b[i]:
            result[1] += 1
    return result


def main():
    print compareTriplets([5, 6, 7], [3, 6, 10])


if __name__ == "__main__":
    main()
