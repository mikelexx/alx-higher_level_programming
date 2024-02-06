#!/usr/bin/python
"""
contains  a function that reads a \
        text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    reads data from a file.
    Args:
        filename: name of file to be read.
    """
    with open(filename, 'r', encoding="UTF8") as f:
        data = f.read()
        print(data)
