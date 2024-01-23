#!/usr/bin/python3
""" 2-square.py
Contains a class that defines square based on module
1-square.py.

"""


class Square:
    """
    This class defines a square in which size must be an integer,
    otherwise raise a TypeError exception with the message
    size must be an integer.

    if size is less than 0, raise a ValueError exception with the message
    size must be >= 0.

    Args:
        size: size of square to be made.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
