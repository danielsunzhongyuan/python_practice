#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/07 12:58
# @Author   : Zhongyuan Sun


def minimumSwaps(arr):
    length = len(arr)
    if length <= 1:
        return 0
    i = 0
    count = 0
    while i < length:
        if arr[i] == i + 1:
            i += 1
        else:
            tmp = arr[i]
            arr[i], arr[tmp-1] = arr[tmp-1], arr[i]
            count += 1
    return count


def main():
    print minimumSwaps([4, 3, 1, 2])  # 3
    print minimumSwaps([2, 3, 4, 1, 5])  # 3


if __name__ == "__main__":
    main()
