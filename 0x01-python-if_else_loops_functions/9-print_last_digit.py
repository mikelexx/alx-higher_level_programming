#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        return 0 - (0 - number) % 10
    else:
        return (number % 10)
