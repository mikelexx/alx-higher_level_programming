#!/usr/bin/python3
"""
This module contains a function that divides every number in a matrix by 2.
"""


def matrix_divided(matrix, div):
    """
    This function devides each element of a matrix by a number given(div).
    Args:
        matrix: a list of lists(matrix) of integers/floats.
        div: dividend
    Raises:
        TypeError: if the matrix is not a list of lists or if any element
        is not of integer / float type or if the size of lists(rows) in the
        matrix are not of same size.
        ZeroDivisionError: if div is 0 since we don't want\
                to divide any element
        with zero.
    """
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of\
                integers/floats")
    else:
        row_len = len(matrix[0])
    result = []

    for row in matrix:
        temporary_row = []
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) \
                    of integers/floats")
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have \
                    the same size")
        for n in row:
            if type(n) not in [int, float]:
                raise TypeError("Each row of the matrix must have\
                        the same size")
            temporary_row.append(round((n / div), 2))
        result.append(temporary_row)
    return result
