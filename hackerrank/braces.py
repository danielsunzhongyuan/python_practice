#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/08 23:23
# @Author   : Zhongyuan Sun


def braces(values):
    result = []
    for value in values:
        result.append(check_brace(value))
    return result


def check_brace(value):
    stack = []
    for brace in value:
        if brace in ["{", "[", "("]:
            stack.append(brace)
        elif brace == "}" and stack and stack[-1] == "{":
            stack.pop()
        elif brace == "]" and stack and stack[-1] == "[":
            stack.pop()
        elif brace == ")" and stack and stack[-1] == "(":
            stack.pop()
        else:
            return "NO"
    return "YES" if not stack else "NO"


def main():
    print braces(["{}[]()", "{[}]}"])
    a = [2, 1, 3]
    a.sort()
    print a


if __name__ == "__main__":
    main()
