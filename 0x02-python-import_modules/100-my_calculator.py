#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    arg_len = len(sys.argv) - 1
    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
        sys.exit(0)
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
        sys.exit(0)
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
        sys.exit(0)
    elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
        sys.exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
