#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys.append(key)
    for k in keys:
        a_dictionary.pop(k, None)
    return a_dictionary
