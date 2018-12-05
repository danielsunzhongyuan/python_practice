#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/09/29 16:00
# @Author   : Zhongyuan Sun


import csv
import math
import os
from optparse import OptionParser

import yaml


class M(object):
    def __init__(self, timestamp, base, change, original, timeout):
        self.base = base
        self.change = change
        self.timestamp = timestamp
        self.original = original
        self.timeout = timeout

    def __str__(self):
        return self.original

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.base == other.base and self.change == other.change and math.fabs(
            int(self.timestamp) - int(other.timestamp)) <= self.timeout

    def get_key(self):
        return self.base


class NewModel(M):
    def __init__(self, timestamp, base, change, original, end_time, timeout):
        self.end_time = end_time
        M.__init__(self, timestamp, base, change, original, timeout)

    def __str__(self):
        return self.original

    def get_value(self):
        self.original.extend([self.end_time, self.timeout])
        return self.original

    def __repr__(self):
        return self.__str__()


def cmp1(m1, m2):
    if m1.base > m2.base:
        return 1
    if m1.base < m2.base:
        return -1

    if m1.timestamp > m2.timestamp:
        return 1
    if m1.timestamp < m2.timestamp:
        return -1

    if m1.change > m2.change:
        return 1
    if m1.change < m2.change:
        return -1
    return 0


def main():
    # parse arguments
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="config_path", help="config path")
    parser.add_option("-i", "--input", dest="input_path", help="input path (a file or a folder)")
    parser.add_option("-o", "--output", dest="output_path", help="output path (a file)")
    options, args = parser.parse_args()

    if not options.config_path:
        print "Please specify config file path"
        os.exit(1)
        return

    with open(options.config_path, "r+") as fh:
        config = yaml.safe_load(fh)

    if not config:
        print "Please check config file. (Should be YAML)"
        os.exit(1)
        return

    if not options.input_path:
        print "Please specify input file path"
        os.exit(2)
        return

    ts_index = int(config["time_key_index"])
    base_indices = [int(i) for i in str(config["base_key_index"]).split(",")]
    change_indices = [int(i) for i in str(config["change_key_index"]).split(",")]
    timeout = int(config["timeout"])

    records = []
    with open(options.input_path, "rb") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=config["csv_separator"])
        for row in spamreader:
            records.append(
                M(
                    row[ts_index],
                    config["csv_separator"].join([row[i] for i in base_indices]),
                    config["csv_separator"].join([row[i] for i in change_indices]),
                    row,
                    timeout
                )
            )

    mapping = {}
    for record in records:
        tmp = mapping.get(record.get_key(), [])
        tmp.append(record)
        mapping[record.get_key()] = tmp

    with open(options.output_path, "wb") as fh:
        for key, value in mapping.items():
            value.sort(cmp1)
            new_records_list = []
            new_record = None
            for record in value:
                if new_record:
                    if new_record == record:
                        new_record.end_time = record.timestamp
                        continue
                    else:
                        new_records_list.append(new_record)
                new_record = NewModel(record.timestamp, record.base, record.change, record.original, record.timestamp,
                                      timeout)
            new_records_list.append(new_record)
            for new_record in new_records_list:
                fh.write(config["csv_separator"].join([str(i) for i in new_record.get_value()]) + "\n")


if __name__ == "__main__":
    main()
