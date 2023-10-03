#!/usr/bin/python3

def uppercase(str):
    upper = ''
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = char(ord(letter) - 32)
        print("{:s}".format(letter), end='')
    print()
