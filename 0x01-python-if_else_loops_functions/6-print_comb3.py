#!/usr/bin/python3
for n in range(0, 8):
    for m in range(n + 1, 10):
        print("{0}{1}".format(n, m), end=', ')
print("{0}{1}".format(n + 1, m))
