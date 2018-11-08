#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/08 23:27
# @Author   : Zhongyuan Sun


def getMinimumUniqueSum(arr):
    # Write your code here
    arr.sort()
    length = len(arr)
    for i in xrange(1, length):
        if arr[i] <= arr[i - 1]:
            arr[i] = arr[i - 1] + 1
    return sum(arr)


def main():
    print getMinimumUniqueSum([1, 2, 2])
    print getMinimumUniqueSum([2, 2, 4, 5])
    print getMinimumUniqueSum([1, 2, 2])


if __name__ == "__main__":
    main()
