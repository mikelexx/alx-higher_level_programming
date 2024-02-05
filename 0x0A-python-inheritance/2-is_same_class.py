#!/usr/bin/python3
"""
this module contains function that compares object with a class.
"""


def is_same_class(obj, a_class):
    """
    compares an object with a specified class.
    Args:
        obj: an object
        a_class: class
    Returns: True if the object is exactly an \
            instance of the specified class ; otherwise False.
    """
    return type(obj) is a_class
