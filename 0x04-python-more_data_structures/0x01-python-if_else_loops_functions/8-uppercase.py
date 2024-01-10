#!/usr/bin/python3
def uppercase(str):
    letter = 2
    for ch in str:
        if 97 <= ord(ch) <= 122:
            letter = ord(ch) - 32
        else:
            letter = ord(ch)
        print("{:c}".format(letter), end="")
    print("")
