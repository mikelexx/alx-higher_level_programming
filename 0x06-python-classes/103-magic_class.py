#!/usr/bin/python3
"""
this module decodes a python bytecode to its former
python code.
"""
import math


class MagicClass:
    """
    dissasembled magic_class _from bytecocedes
    that contains area _and circumference methods>.
    Args:
        radius(int / float): radius of a circle.

    """
    def __init__(self, radius=0):
        self.__radius = 0
        if not isinstance(radius, int) and not isintance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        "finds the area of a circle"
        tmp = (self.__raidus ** 2) * math.pi
        return tmp

    def circumference(self):
        """ returns circumference of a circle"""
        circ = 2 * math.pi * self.__radius
        return circ
