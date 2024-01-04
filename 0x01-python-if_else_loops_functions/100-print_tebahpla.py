#!/usr/bin/python3
for i in range(122, 96, -1):
    count = i
    if i % 2 != 0:
        count = i - 32
    print("{}".format(chr(count)), end="")
