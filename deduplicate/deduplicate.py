#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/09/29 16:00
# @Author   : Zhongyuan Sun
import datetime

class M(object):
    def __init__(self, timestamp, wifi, mac):
        self.timestamp = timestamp
        self.wifi = wifi
        self.mac = mac

    def __str__(self):
        return self.mac + " " + self.timestamp + " " + self.wifi + " "

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.wifi == other.wifi and self.mac == other.mac


class NewModel(M):
    def __init__(self, start, end, wifi, mac):
        self.end = end
        M.__init__(self, start, wifi, mac)

    def __str__(self):
        return self.mac + " " + self.timestamp + " " + self.end + " " + self.wifi + " "

    def __repr__(self):
        return self.__str__()


def cmp1(m1, m2):
    if m1.mac > m2.mac:
        return 1
    if m1.mac < m2.mac:
        return -1

    if m1.timestamp > m2.timestamp:
        return 1
    if m1.timestamp < m2.timestamp:
        return -1

    if m1.wifi > m2.wifi:
        return 1
    if m1.wifi < m2.wifi:
        return -1
    return 0


def main():
    print datetime.datetime.now()
    with open("./sample2.txt", "rb") as fh:
        lines = fh.readlines()

    records = []
    for line in lines:
        record = line.split("\t")
        if record:
            records.append(M(record[0], record[1], record[3]))

    records.sort(cmp1)
    new_records = []
    new_record = None
    for record in records:
        if new_record:
            if new_record == record:
                new_record.end = record.timestamp
                continue
            else:
                new_records.append(new_record)
        new_record = NewModel(record.timestamp, record.timestamp, record.wifi, record.mac)

    new_records.append(new_record)
    print datetime.datetime.now()


if __name__ == "__main__":
    main()
