#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_len = len(sys.argv) - 1
    if arg_len == 0:
        print("0 arguments.")
    elif arg_len == 1:
        print("1 argument:")
        print("{}: {}".format(arg_len, sys.argv[arg_len]))
    else:
        print("{} arguments:".format(arg_len))
        for arg in range(1, arg_len + 1):
            print("{}: {}".format(arg, sys.argv[arg]))
