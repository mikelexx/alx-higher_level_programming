#!/usr/bin/python3
""" 3-square.py
This module defines a square based on module 2-square.py.
"""


class Square:
    """
    This class defines a square of size given by user and
    method for finding its area.

    Args:
        size: lengths of square to be made.
    """

    def __init__(self, size=0):
        self.size = size

    def __eq__(self, other):
        return self.__size == other.size

    def __ne__(self, other):
        return self.__size != other.size

    def __lt__(self, other):
        return self.__size < other.size

    def _le__(self, other):
        return self.__size <= other.size

    def __gt__(self, other):
        return self.__size > other.size

    def __ge__(self, other):
        return self.__size >= other.size

    @property
    def size(self):
        """ retrieves the size property of square.
        The size setter checks that size must be positive int
        before assigning it  as private instance attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise ValueError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This function computes and returns area of a square of
        dimensions defined bt `size` attribute.

        Returns:
            The area of a square always.
        """
        area = self.__size * self.__size
        return area
