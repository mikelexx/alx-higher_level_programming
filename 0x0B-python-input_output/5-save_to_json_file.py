#!/usr/bin/python3
"""
this module contains  a function that writes an\
        Object to a text file, using a JSON representation:
"""

import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation:
    Args:
        my_obj: object to be json stringified.
        filame: file to save the JSON representation of object.
    """
    with open(filename, 'a', encoding="UTF8") as f:
        jstring = json.dumps(my_obj)
        f.write(jstring)
