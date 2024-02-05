#!/usr/bin/python3
"""
this modules has a function that returns the list of available attributes and methods of an object.
"""
def lookup(obj):
    """
    returns the list of available attributes and methods of an object.
    """
    retun dir(obj)
