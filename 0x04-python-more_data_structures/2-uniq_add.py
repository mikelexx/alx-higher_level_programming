#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    for n in set(my_list):
        count += n
    return count
