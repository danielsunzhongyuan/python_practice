#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/06 19:46
# @Author   : Zhongyuan Sun


def hourglassSum(arr):
    length = len(arr)
    result = []
    for i in range(1, length - 1):
        for j in range(1, length - 1):
            result.append(
                arr[i][j] + arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] + arr[i + 1][j - 1] + arr[i + 1][j] +
                arr[i + 1][j + 1])
    return max(result)


def main():
    print hourglassSum([[1, 1, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0],
                        [1, 1, 1, 0, 0, 0],
                        [0, 0, 2, 4, 4, 0],
                        [0, 0, 0, 2, 0, 0],
                        [0, 0, 1, 2, 4, 0]])


if __name__ == "__main__":
    main()
