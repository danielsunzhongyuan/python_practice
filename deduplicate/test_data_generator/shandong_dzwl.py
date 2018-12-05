#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/12 19:34
# @Author   : Zhongyuan Sun


"""
1525040614,27,,,,,460023482114794,,,,0530,60203,115.975136,35.737778,,,,,,,,,,1
"""

import random


# def get_normal_distribution(mu=0, sigma=1, size=1):
#     u = np.random.uniform(size=size)
#     v = np.random.uniform(size=size)
#     z = np.sqrt(-2*np.log(u)) * np.cos(2*np.pi*v)
#     return mu + z * sigma


def main():
    """
    timestamp: 1525040614 ~ 1525127014 一天
    27
    ,,,,
    460023482114794 ~ 460023482124794 1w
    
    :return: 
    """
    record = [""] * 24
    record[1] = "27"
    record[10] = "633"
    record[11] = "40269"

    imsi_list = ["46002348211" + str(i) for i in xrange(10000)]
    imei_list = ["235492304" + str(i) for i in xrange(1000000)]
    with open("./test.csv", "a+") as fh:
        for i in xrange(5):
            count = 5
            while count > 0:
                # x = get_normal_distribution()[0]
                record[0] = str(int(float(str(random.random() * 86400 + 1525040614))))
                record[6] = random.choice(imsi_list)
                record[7] = random.choice(imei_list)
                record[12] = str(random.random() + 119)
                record[13] = str(random.random() + 35)
                if random.random() > 0.997:
                    fh.write(",".join(record) + "\n")
                else:
                    fh.write(",".join(record[:18]) + "\n")
                count -= 1
            fh.flush()


if __name__ == "__main__":
    main()
