#!/usr/bin/python3

"""
Contains a function that prints a square with the character #.
"""


def print_square(size):
    """
    This function prints a square using #.
    Args:
        size(int): size of the square to be printed.
    Raises:
        TypeError: if the size given isn't of integer type.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
