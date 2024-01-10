#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if el == search else el for el in my_list]
