#!/usr/bin/python3
"""Module containing add_integer function
"""


def add_integer(a, b=98):
    """Returns the sum of two inputs, or raises an error"""
    t = []
    try:
        t.append(round(a))
    except Exception:
        raise TypeError('a must be an integer')
    try:
        t.append(round(b))
    except Exception:
        raise TypeError('b must be an integer')
    return t[0] + t[1]
