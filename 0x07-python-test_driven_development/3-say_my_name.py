#!/usr/bin/python3
""""
This module contains function that prints names of a person.
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints the first and lastname of a person.
    Args:
        first_name (str): first name of a person.
        last_name (str): last name of a person.
    Raises:
        TypeError: if any of arguments given is not a string.
    """
    if not isinstance(first_name, str) or first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str) or last_name is None:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
