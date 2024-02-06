#!/usr/bin/python3
"""
contains  a function that writes a string\
        to a text file (UTF8) and returns\
        the number of characters written:
"""


def write_file(filename="", text=""):
    """
    this function writes a string to a text file (UTF8)
    Args:
        filename: name of file.
        text: text to be writen to the file.
    Returns: count of bytes written.
    """
    with open(filename, 'w', encoding="UTF8") as f:
        count = f.write(text)
        return count
