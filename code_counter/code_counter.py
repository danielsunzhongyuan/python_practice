#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/09/13 12:12
# @Author   : Zhongyuan Sun

from optparse import OptionParser
import os


def walk_dir(files, path, excludes, suffix):
    for x in os.listdir(path):
        if os.path.isfile(os.path.join(path, x)):
            if x.endswith(suffix):
                files.append(os.path.join(path, x))
        elif os.path.isdir(os.path.join(path, x)):
            if x not in excludes:
                walk_dir(files, os.path.join(path, x), excludes, suffix)


def calculate_lines(path):
    count = 0
    with open(path) as fh:
        a = fh.readlines()
        for i in a:
            if i.strip("\n").strip(" ") != "":
                count += 1
    return count


def main():
    parser = OptionParser()
    parser.add_option("-p", "--path", dest="path", help="code repository path")
    parser.add_option("-e", "--exclude", dest="exclude_folders", help="exclude folder, like vender, static")
    parser.add_option("-s", "--suffix", dest="suffix", help="suffix of code, like go|java|py etc.")
    options, args = parser.parse_args()
    files = []
    path = options.path if options.path else "/Users/zsun/go/src/gangas-view-new"

    if options.exclude_folders:
        exclude_folders = options.exclude_folders.split(",")
        for i in range(len(exclude_folders)):
            exclude_folders[i] = exclude_folders[i].strip()
    else:
        exclude_folders = ["vendor", "views", "sql"]

    suffix = options.suffix if options.suffix else "go"
    walk_dir(files, path, exclude_folders, suffix)
    total_count = 0
    for f in files:
        total_count += calculate_lines(f)
    print total_count


if __name__ == "__main__":
    main()
