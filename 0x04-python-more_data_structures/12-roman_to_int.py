#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        return 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    prev = roman_string[0]
    count = 0
    for n in roman_string:
        if n not in romans:
            return 0
        if romans[n] > romans[prev]:
            count -= romans[prev]
            count -= romans[prev]
        count += romans[n]
        prev = n
    return count
