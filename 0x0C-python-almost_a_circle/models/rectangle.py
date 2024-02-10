#!/usr/bin/python3
"""
This module Rectangle class that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    This class creates a rectangle shape.
    Args:
        width: width of rectangle
        height: height of rectangle
        x: x cordinate position of rectangle
        y: y cordinate position of rectangle
        id: identification number of rectangle
    Raises:
        TypeError: if any of the attribure is not integer.
        ValueError: if width or height is less than or equal\
                    to zero or if either x or y is less than 0.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        this function assigns an argument to each attribute of object.
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute.
        Args: list of attributes to be added.
        """
        if args and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
            return
        for key, val in kwargs.items():
            setattr(self, key, val)

    def display(self):
        """
        displays the object dimensions and position by use of symbol #.
        """
        for h in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def area(self):
        """
        returns area of rectangle instance.
        """
        return self.__width * self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def to_dictionary(self):
        """
        returns the dictionary representation of object.
        """
        rep = {}
        for key, val in self.__dict__.items():
            if key == "_Rectangle__height":
                rep["height"] = val
            elif key == "_Rectangle__width":
                rep["width"] = val;
            elif key =="_Rectangle__x":
                rep["x"] = val
            elif key == "_Rectangle__y":
                rep["y"] = val
            else:
                rep["id"] = val
        return rep
    
