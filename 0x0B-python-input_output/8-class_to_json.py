#!/usr/bin/python3
"""
this module contains a function that returns the\
dictionary description with simple \
data structure (list, dictionary, string, integer and boolean) \
for JSON serialization of an object:
"""
import json


def class_to_json(obj):
    """
    serializes the attributes and methods of an object.
    Args:
        obj: an object of any type
    returns: the dictionary description with \
simple data structure (list, dictionary, string, \
integer and boolean) for JSON serialization of an object:
    """
    return json.dumps(obj.__dict__)
