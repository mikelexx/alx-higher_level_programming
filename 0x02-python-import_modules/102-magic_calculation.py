#!/usr/bin/python3
def magic_calculation(n, m):
    from magic_calculation_102 import add, sub

    if (n < m):
        d = add(n, m)
        for i in range(4, 6):
            d = add(n, m)
        return d
    else:
        return sub(n, m)
