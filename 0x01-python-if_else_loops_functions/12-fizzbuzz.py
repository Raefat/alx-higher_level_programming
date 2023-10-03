#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 and num % 5:
            print("FizzBuzz")
        elif num % 3:
            print("Fizz")
        else:
            print("Buzz")
