#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for n in list[:-1]:
            print("{}".format(n), end=" ")
        if list:
            print("{}".format(list[-1]))
        else:
            print()
