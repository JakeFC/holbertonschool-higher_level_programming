#!/usr/bin/python3
"""Module with Square class definition"""


class Square:
    """A class with:
    __size: optional private instance attribute
    area(self): method to perform function
    size(self): property used to return __size
    size(self, value): method to set a new __size
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise TypeError('size must be >= 0')
        else:
            raise ValueError('size must be an integer')

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise TypeError('size must be >= 0')
        else:
            raise ValueError('size must be an integer')
