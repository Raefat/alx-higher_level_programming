#!/usr/bin/python3
for num in range(0, 99):
    if num < 10:
        print(f"{num:02d}", end=',')
print(f"{num + 1:02d}")
