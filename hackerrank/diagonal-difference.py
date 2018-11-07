#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/06 21:10
# @Author   : Zhongyuan Sun

import math


def diagonalDifference(arr):
    length = len(arr)
    left_to_right, right_to_left = 0, 0
    for i in range(length):
        left_to_right += arr[i][i]
        right_to_left += arr[length - 1 - i][i]
    return int(math.fabs(left_to_right - right_to_left))


def main():
    print diagonalDifference([[11, 2, 4],
                              [4, 5, 6],
                              [10, 8, -12]])


if __name__ == "__main__":
    main()
