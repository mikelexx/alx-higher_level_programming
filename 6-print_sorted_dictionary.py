#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    tmp = [key for key in a_dictionary]
    tmp = sorted(tmp)
    for key in tmp:
        print(key, ":", a_dictionary[key])
