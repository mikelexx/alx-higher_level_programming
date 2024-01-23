#!/usr/bin/python3
""" 1-square.py

Contains class that defines a square shape.

"""


class Square:
    """
    Class Square that defines a square by a private
    instance attribute: size.
    Args:
        size: to be used as dimensoin of square.

    """
    def __init__(self, size):
        self.__size = size
