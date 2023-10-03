#!/usr/bin/python3

def print_last_digit(number):
    last = 10 - (number % 10) if number < 0 else number % 10
    print("{}".format(last), end='')
    return last
