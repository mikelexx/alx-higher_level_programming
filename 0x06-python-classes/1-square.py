#!/usr/bin/python2
""" 1-square.py.
This module contains a clas Square that defines a square.
"""


class Square:
    """
    This class defines  a square based by:
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    Args:
        size: Can be of any type.
    Attributes:
        __size:privete to control computations involving Square.

    """
    def __init__(self, size):
        self.__size = size
