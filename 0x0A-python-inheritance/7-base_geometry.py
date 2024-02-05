#!/usr/bin/python3
"""
constains a class based on module 6-base_geometry.
"""


class BaseGeometry():
    """
    This module contains unimplemented fuction and integer validator\
            function.
        """
    def area(self):
        """
        this function  does nothing
        Raises:
            Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        this function validates integer.
        Args:
            name (str): is assumed to be always a string
            value (int): will be checked agains type int
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
