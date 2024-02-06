#!/usr/bin/python3
"""
Write a function that appends a string at the end \
        of a text file (UTF8) and returns the number\
        of characters added:
"""


def append_write(filename="", text=""):
    """
     appends a string at the end of a text file (UTF8)
    Args:
        filename: name of file.
        text: text to be appended
    Returns: number of characters written.
    """

    with open(filename, 'a', encoding="UTF8") as f:
        return (f.write(text))
