#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = 0
    for arg in sys.argv[1:]:
        count += int(arg)
    print(count)
