#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
    last = 0 - ((0 - number) % 10)
print("Last digit of", number, "is", last, end="")
if last > 5 and number > 0:
    print(" and is greater than 5")
elif last == 0 and number >= 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
