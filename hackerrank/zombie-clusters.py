#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: zsun

# @Time     : 2018/11/08 23:48
# @Author   : Zhongyuan Sun


# Complete the 'zombieCluster' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY zombies as parameter.
# 僵尸之间能联系起来的分成一组，要找总共有几组？

# 样例：
# 1000
# 0110
# 0110
# 0001
# 这里总共有3组，分别是(0),(1,2),(3)

def zombieCluster(zombies):
    # Write your code here
    length = len(zombies)
    if length <= 1:
        return length

    clusters = 0
    zombie_cluster_mapping = {}
    for zombie, connection in enumerate(zombies):
        connected_zombies = get_connected_zombies(connection)
        intersections = get_intersect_of_two_arrays(connected_zombies, zombie_cluster_mapping.keys())
        if not intersections:
            clusters += 1
            for z in connected_zombies:
                zombie_cluster_mapping[z] = clusters
        else:
            intersection_clusters = get_cluster(zombie_cluster_mapping, intersections)
            min_cluster = min(intersection_clusters)
            for z in connected_zombies:
                zombie_cluster_mapping[z] = min_cluster
            for c in intersection_clusters:
                set_cluster_from_to(zombie_cluster_mapping, c, min_cluster)

    return len(set(zombie_cluster_mapping.values()))


def set_cluster_from_to(mapping, from_value, to_value):
    for k in mapping.keys():
        if mapping[k] == from_value:
            mapping[k] = to_value


def get_cluster(mapping, intersections):
    ret = []
    for i in intersections:
        ret.append(mapping[i])
    return list(set(ret))


def get_connected_zombies(connection):
    """
    Get all connected zombies including itself
    """
    connected_zombies = []
    for ind, connection in enumerate(connection):
        if connection == "1":
            connected_zombies.append(ind)
    return connected_zombies


def get_intersect_of_two_arrays(arr1, arr2):
    return [i for i in arr1 if i in arr2]


def main():
    print zombieCluster(["1000", "0100", "0010", "0001"])
    print zombieCluster(["1100", "1110", "0110", "0001"])
    print zombieCluster(["100001", "010010", "101100", "001100", "010010", "100001"])
    print zombieCluster(["10000", "01110", "01100", "01011", "00011"])
    print zombieCluster(["10000", "01110", "01100", "01010", "00001"])
    print zombieCluster(["110010", "110000", "001101", "001100", "000011", "000011"])


if __name__ == "__main__":
    main()
