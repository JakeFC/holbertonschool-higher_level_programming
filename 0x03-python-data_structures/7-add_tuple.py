#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or len(tuple_a) is 0:
        a = 0, 0
    elif len(tuple_a) is 1:
        a = tuple_a[0], 0
    else:
        a = tuple_a[0], tuple_a[1]
    if tuple_b is None or len(tuple_b) is 0:
        b = 0, 0
    elif len(tuple_b) is 1:
        b = tuple_b[0], 0
    else:
        b = tuple_b[0], tuple_b[1]
    new = (a[0] + b[0]), (a[1] + b[1])
    return new
