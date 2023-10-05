#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    summ = 0
    arg_len = len(sys.argv) - 1
    for arg in range(1, arg_len + 1):
        summ += int(sys.argv[arg])

    print("{}".format(summ))
