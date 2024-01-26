#!/usr/bin/python3
""" 0-add_integer.py
This module contains function that adds two integers.
The function raises error incase a non integer data argument is passed.
The floats arguments are fist casted to integer as to  produce integer result.
"""


def add_integer(a, b=98):
    """
    This functions returns the addition of two integers.
    Args:
        a - first integer.
        b - second integer.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if isinstance(b, float):
        b = int(b)
    if isinstance(a, float):
        a = int(a)
    res = a + b
    return res
