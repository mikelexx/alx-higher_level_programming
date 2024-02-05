#!/usr/bin/python3
"""
contains function checks if  if the object is an instance of, or if the object is an instance of a class that inherited from.
"""

def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object
        a_class: class
    returns: True if the object is an instance of,\
            or if the object is an instance of a\
            class that inherited from, the specified\
            class ; otherwise False
    """
    return isinstance(obj, a_class)
