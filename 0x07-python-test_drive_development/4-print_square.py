#!/usr/bin/python3
"""Module for print_square function
"""


def print_square(size):
    """Prints a square of '#' chars with side length size"""
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        return
    for row in range(size):
        for i in range(size):
            print('#', end="")
        print("")
