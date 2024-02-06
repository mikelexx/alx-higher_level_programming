#!/usr/bin/python3
"""
this module contains  a function that returns\
        an object (Python data structure)\
        represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """
    returns an object (Python data structure)\
            represented by a JSON string.
    Args:
        my_str: object represented as string.
    Returns: actual object.
    """
    obj = json.loads(my_str)
    return obj
