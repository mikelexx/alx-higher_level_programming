#!/usr/bin/python3
"""
This module contains a function that multiplies \
2 matrices.
"""


def matrix_mul(m_a, m_b):
    """
    this function multiplies one matrix by another.
    Args:
        m_a (int/ float): first matrix
        m_b (int/ float): second matrix
    Raises:
        ValueError: if ma_a can't be multiplied by m_b
        TypeError: if one element of either list is neither \
                a float nor an integer.
    Returns: ma_a x ma_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise TypeError("m_b can't be empty")
    if len(m_a) == 0:
        raise TypeError("m_a can't be empty")
    if not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list of lists")
    if not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list of lists")
    if len(m_a) == 1 and len(m_a[0]) == 0:
        raise TypeError("m_a can't be empty")
    if len(m_b) == 1 and len(m_b[0]) == 0:
        raise TypeError("m_b can't be empty")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_b) != len(m_a[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    res = []
    for k in range(len(m_a)):
        row = []
        for i in range(len(m_b[0])):
            tmp = 0
            for j in range(len(m_b)):
                if len(m_b[k]) != len(m_b[0]):
                    raise TypeError("each row of m_b must be of the same size")
                if not isinstance(m_b[j][i], int)\
                        and not isinstance(m_b[j][i], float):
                    raise TypeError("m_b should \
                            contain only integers or floats")
                if not isinstance(m_a[k][j], int) \
                        and not isinstance(m_a[k][j], float):
                    raise TypeError("m_a should \
                            contain only integers or floats")
                tmp += m_a[k][j] * m_b[j][i]
            row.append(tmp)
        res.append(row)
    return res
