#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ != "__main__":
    exit()
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
op = ['+', '-', '*', '/']
if sys.argv[2] not in op:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
a = int(sys.argv[1])
b = int(sys.argv[3])
op = sys.argv[2]
if op == '+':
    print("{} {} {} = {}".format(a, op, b, add(a, b)))
if op == '-':
    print("{} {} {} = {}".format(a, op, b, sub(a, b)))
if op == '*':
    print("{} {} {} = {}".format(a, op, b, mul(a, b)))
if op == '/':
    print("{} {} {} = {}".format(a, op, b, div(a, b)))
