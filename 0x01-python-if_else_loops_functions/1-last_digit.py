#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
isNegative = False
if number < 0:
    number = -number
    isNegative = True

num = -number if isNegative else number
if num < 6:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
elif num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
else:
    print(f"Last digit of {number} is {num}")