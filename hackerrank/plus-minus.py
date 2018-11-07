#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/07 18:53
# @Author   : Zhongyuan Sun


# Complete the plusMinus function below.
def plusMinus(arr):
    positive, negative, zero = 0, 0, 0
    for n in arr:
        if n > 0:
            positive += 1
        elif n < 0:
            negative += 1
        else:
            zero += 1
    total = positive + negative + zero
    print "%.6f" % (1.0*positive/total)
    print "%.6f" % (1.0*negative/total)
    print "%.6f" % (1.0*zero/total)


def main():
    plusMinus([1, 1, 0, -1, -1])
    plusMinus([-4, 3, -9, 0, 4, 1])


if __name__ == "__main__":
    main()
