#!/usr/bin/python3
"""Module for function pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of lists of ints representing the Pascal's
    triangle of n"""
    t = []
    if n <= 0:
        return t
    for row in range(n):
        l = []
        for column in range(row + 1):
            if column == row:
                l.append(1)
                t.append(l)
            elif column == 0:
                l.append(1)
            else:
                l.append(t[row - 1][column - 1] + t[row - 1][column])
    return t
