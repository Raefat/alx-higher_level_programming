#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0] if tuple_a[0] else 0
    a2 = tuple_a[1] if tuple_a[1] else 0
    b1 = tuple_b[0] if tuple_b[0] else 0
    b2 = tuple_b[1] if tuple_b[1] else 0
    tuple_c = (a1 + a2, b1 + b2)
    return (tuple_c)
