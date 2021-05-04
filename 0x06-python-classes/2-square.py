#!/usr/bin/python3
"""Module with Square class definition"""


class Square:
    """A class with instance attribute size
    defined only when valid int is passed as arg
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise TypeError('size must be >= 0')
        else:
            raise ValueError('size must be an integer')
