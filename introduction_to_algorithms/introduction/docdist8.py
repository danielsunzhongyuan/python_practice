#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/09/16 22:15
# @Author   : Zhongyuan Sun

import math
import string
import sys


def read_file(filename):
    try:
        with open(filename, "r") as fh:
            return fh.read()
    except IOError:
        print "Error opening or reading input file: ", filename
        sys.exit()


def get_words_from_line_list(text):
    text = text.translate(translation_table)
    word_list = text.split()
    return word_list


# global variables needed for fast parsing
# translation table maps upper case to lower case and punctuation to spaces
translation_table = string.maketrans(string.punctuation+string.uppercase,
                                     " "*len(string.punctuation)+string.lowercase)


def get_words_from_string(line):
    line = line.translate(translation_table)
    word_list = line.split()
    return word_list


def count_frequency(word_list):
    l = {}
    for new_word in word_list:
        l[new_word] = l.get(new_word, 0) + 1
    # return l.items()
    return l


def insertion_sort(arr):
    for j in range(len(arr)):
        key = arr[j]
        i = j - 1
        while i > -1 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


def merge_sort(arr):
    length = len(arr)
    if length == 1:
        return arr
    mid = length / 2
    l = merge_sort(arr[:mid])
    r = merge_sort(arr[mid:])
    return merge(l, r)


def merge(l, r):
    i, j = 0, 0
    len_l, len_r = len(l), len(r)
    ret = []
    while i < len_l and j < len_r:
        if l[i] < r[j]:
            ret.append(l[i])
            i += 1
        else:
            ret.append(r[j])
            j += 1
    if i < len_l:
        ret.extend(l[i:])
    if j < len_r:
        ret.extend(r[j:])
    return ret


def quick_sort(arr, left, right):
    if left < right:
        k = partition(arr, left, right)
        quick_sort(arr, left, k-1)
        quick_sort(arr, k+1, right)


def partition(arr, left, right):
    key = arr[left]
    while left < right:
        while left < right and arr[right] >= key:
            right -= 1
        while left < right and arr[right] < key:
            arr[left] = arr[right]
            left += 1
            arr[right] = arr[left]
    arr[left] = key
    return left


def word_frequency_for_file(filename):
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    # freq_mapping = merge_sort(freq_mapping)
    # quick_sort(freq_mapping, 0, len(freq_mapping)-1)

    print "File", filename, ":",
    print len(line_list), "lines,",
    print len(word_list), "words,",
    print len(freq_mapping), "distinct words"

    return freq_mapping


def inner_product(l1, l2):
    total = 0.0
    for key in l1:
        if key in l2:
            total += l1[key] * l2[key]
    return total


def vector_angle(l1, l2):
    numerator = inner_product(l1, l2)
    denominator = math.sqrt(inner_product(l1, l1) * inner_product(l2, l2))
    return math.acos(numerator / denominator)


def main():
    if len(sys.argv) != 3:
        print "Usage: docdist1.py filename_1 filename_2"
    else:
        filename_1 = sys.argv[1]
        filename_2 = sys.argv[2]
        sorted_word_list_1 = word_frequency_for_file(filename_1)
        sorted_word_list_2 = word_frequency_for_file(filename_2)
        distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
        print "The distance between the document is %0.6f (radians)" % distance


if __name__ == "__main__":
    import profile
    profile.run("main()")
    main()
