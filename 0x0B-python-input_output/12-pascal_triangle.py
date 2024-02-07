#!/usr/bin/python3
"""
Technical interview preparation:
You are not allowed to google anything
Whiteboard first
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the\
            Pascal’s triangle of n:
    Args:
        n: number of rows of pascal trinagle.
    Returns: an empty list if n >= 0 else list lists.
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    res = [[1]]
    curr = [1]
    for i in range(1, n):
        tmp = []
        for j in range(len(curr)):
            if j == 0:
                tmp.append(1)
            else:
                tmp.append(curr[j] + curr[j - 1])
            if j == len(curr) - 1:
                tmp.append(1)
        res.append(tmp)
        curr = tmp
    return res
