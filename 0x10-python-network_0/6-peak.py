#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Write a function that finds a peak in a list of unsorted integers.
    Args:
        list_of_integers: list to be searched.
    """

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    middle = int(len(list_of_integers) / 2)

    if middle != len(list_of_integers) - 1:
        if list_of_integers[middle - 1] < list_of_integers[middle] and\
           list_of_integers[middle + 1] < list_of_integers[middle]:
            return list_of_integers[middle]
    else:
        if list_of_integers[middle - 1] < list_of_integers[middle]:
            return list_of_integers[middle]
        else:
            return list_of_integers[middle - 1]

    if list_of_integers[middle - 1] > list_of_integers[middle]:
        new_list = list_of_integers[0:middle]
    else:
        new_list = list_of_integers[middle + 1:]
    return find_peak(new_list)
