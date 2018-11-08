#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/08 23:27
# @Author   : Zhongyuan Sun

"""
有一个数组，里面有重复的数，现在要加大重复的数，是得没有重复的数，求最小要加多少？
返回的是新数组的总和。也就是原数组的和，加上上面的"最小要加多少"
"""
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
