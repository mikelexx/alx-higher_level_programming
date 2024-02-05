#!/usr/bin/python3
"""
this module contains  a function that adds a\
        new attribute to an object if it’s possible.
"""


def add_attribute(obj, attr, value):
    """
    adds attribute to specified obj if possible.
    Args:
        obj : object
        attr: attribute to be added to that object.
        value: value of the attribute to be added.
    Raises:
        TypeError: if obj can't have new attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
