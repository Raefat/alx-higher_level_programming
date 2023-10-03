#!/usr/bin/python3

def uppercase(str):
    upper = ''
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            upper += char(ord(letter) - 32)
        else:
            upper += letter
    print(upper)
