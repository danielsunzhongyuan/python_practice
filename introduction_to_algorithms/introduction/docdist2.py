#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/09/16 20:07
# @Author   : Zhongyuan Sun

import math
import sys


def read_file(filename):
    try:
        with open(filename, "r") as fh:
            return fh.readlines()
    except IOError:
        print "Error opening or reading input file: ", filename
        sys.exit()


def get_words_from_line_list(lines):
    word_list = []
    for line in lines:
        word_list = word_list + get_words_from_string(line)
    return word_list


def get_words_from_string(line):
    word_list = []
    character_list = []
    for c in line:
        if c.isalnum():
            character_list.append(c)
        elif len(character_list) > 0:
            word = "".join(character_list)
            word = word.lower()
            word_list.append(word)
            character_list = []
    if len(character_list) > 0:
        word = "".join(character_list)
        word = word.lower()
        word_list.append(word)
    return word_list


def count_frequency(word_list):
    l = []
    for new_word in word_list:
        for entry in l:
            if new_word == entry[0]:
                entry[1] = entry[1] + 1
                break
        else:
            l.append([new_word, 1])
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


def word_frequency_for_file(filename):
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    insertion_sort(freq_mapping)

    print "File", filename, ":",
    print len(line_list), "lines,",
    print len(word_list), "words,",
    print len(freq_mapping), "distinct words"

    return freq_mapping


def inner_product(l1, l2):
    total = 0.0
    i, j = 0, 0
    len1, len2 = len(l1),  len(l2)
    while i < len1 and j < len2:
        if l1[i][0] == l2[j][0]:
            total += l1[i][1] * l2[j][1]
            i += 1
            j += 1
        elif l1[i][0] < l2[j][0]:
            i += 1
        else:
            j += 1
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
