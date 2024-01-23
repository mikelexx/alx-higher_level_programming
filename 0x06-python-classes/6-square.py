#!/usr/bin/python3
""" 5-square.py
This module defines a square based on module 4-square.py.
"""


class Square:
    """
    This class defines a square of size given by user and
    method for finding its area and printing it graphically
    using # symbol.

    Args:
        size: lengths of square to be made.
        position: tuple containing two integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if ((not isinstance(value, tuple)
                or len(value) != 2)
                or not isinstance(value[0], int)
                and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        """ retrieves the size property of square.
        The size setter checks that size must be positive int
        before assigning it  as private instance attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
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

    def my_print(self):
        """
        This function prints in stdout the square with the character
        #  but instead prints empty line if size is equal to zero.
        """
        if self.__size == 0:
            print()
        else:
            for m in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
