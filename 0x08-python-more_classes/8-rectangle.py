#!/usr/bin/python3
"""
This module has Rectangle class that defines a rectangle \
        based on module 7-rectangle.
"""


class Rectangle:
    """
    This class defines a rectangle based on module 0-rectangle.py.
    It is enabling recreation of a instance by using eval method.
    Args:
        width (int): widht dimenstion of rectangle.
        height (int): height dimenstion of rectangle.
    Raises:
        ValueError: for width or height < 0.
        TypeErrror: for width or height argument that is not integer.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        substr = ""
        for i in range(self.__height):
            for j in range(self.__width):
                substr += str(self.print_symbol)
            if i != self.__height - 1:
                substr += '\n'
        return substr

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.height)

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This function checks which rectangle object is bigger.
        Args:
            rect_1 (Rectangle): first assumed Rectangle object
            rect_2 (Rectangle): Second assumed rectangle object
        Raises:
            TypeError: if any argument is not a Rectangle instance.
        Returns: rect with bigger area or rect_1 if they have equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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

    def area(self):
        """
        Returns the Rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """"
        Calculates the perimeter for rectangle.
        Returns: Perimeter of rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
