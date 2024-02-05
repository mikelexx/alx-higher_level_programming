#!/usr/bin/python3
"""
this module contains a class that inherits from int.
"""


class MyInt(int):
    """
    inverts the == and == functions of integers.
    """
    def __eq__(self, c2):
        return False

    def __ne__(self, c2):
        return True
