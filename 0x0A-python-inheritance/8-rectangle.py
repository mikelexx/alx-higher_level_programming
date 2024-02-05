#!/usr/bin/python3
"""
this module defines a class Rectangle that\
        inherits from BaseGeometry (7-base_geometry.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    this class defines rectangle shape.
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
    Raises:
        e : for any error caught in in subsequent calls.
    """
    def __init__(self, width, height):
        try:
            self.integer_validator("width", width)
            self.integer_validator("height", height)
        except ValueError as e:
            raise e
        except TypeError as e:
            raise e
        else:
            self.__width = width
            self.__height = height
