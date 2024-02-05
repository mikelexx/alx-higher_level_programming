#!/usr/bin/python3
"""
this module contains Square that inherits\
        from Rectangle (9-rectangle.py).(task\
        based on 10-square.py).
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    creates a square object.
    Args:
        size (str): dimensions for square.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        returns area of square
        """
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
