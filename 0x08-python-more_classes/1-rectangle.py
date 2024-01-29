#!/usr/bin/python3
"""
This module has Rectangle class that defines a rectangle.
"""


class Rectangle:
    """
    This class defines a rectangle based on module 0-rectangle.py.
    Args:
        width (int): widht dimenstion of rectangle.
        height (int): height dimenstion of rectangle.
    Raises:
        ValueError: for width or height < 0.
        TypeErrror: for width or height argument that is not integer.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
