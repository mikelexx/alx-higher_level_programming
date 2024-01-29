#!/usr/bin/python3

"""
This module contains a function for indenting a string.
The string is splint into separate lines with no leading or lagging spaces.
The delimiters used for splitting are (, ?, : )
"""


def text_indentation(text):
    """
    This function splits a given string into multiple strings
    each beggining on a new line and then prints them.
    Args:
        text(str): string that is to be splitted.
    Raises:
        TypeError: if the text given is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in
                    text.split(delim)])
    print(text, end="")
