#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    romans = {"I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
    prev = roman_string[0]
    count =  0
    for n in roman_string:
        if n not in romans:
            return None
        if romans[n] > romans[prev]:
            count -= romans[prev]
            count -= romans[prev]
        count += romans[n]
        prev = n
    return count
