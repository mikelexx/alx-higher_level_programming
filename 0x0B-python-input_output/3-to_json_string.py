#!/usr/bin/python3
"""
contains  a function that returns the JSON representation\
        of an object (string):
"""


import json


def to_json_string(my_obj):
    """
    returns JSON representation of an object (my_obj)
    Args:
    my_obj: object.
    Returns: string - json representation
    """
    jstring = json.dumps(my_obj)
    return jstring
