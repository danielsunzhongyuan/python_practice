#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/06 19:32
# @Author   : Zhongyuan Sun


def repeatedString(s, n):
    length = len(s)
    a_count = s.count("a")
    times = n / length
    remains = n % length
    return a_count * times + s[:remains].count("a")


def main():
    print repeatedString("aba", 10)


if __name__ == "__main__":
    main()
