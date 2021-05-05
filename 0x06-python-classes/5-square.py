#!/usr/bin/python3
"""Module with Square class definition"""


class Square:
    """A class with:
    __size: optional private instance attribute created on init
    area(self): method to perform function
    size(self): property used to return __size as self.size
    size(self, value): method to set a new __size
    my_print(self): method to print the square of '#' characters
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

    def my_print(self):
        if self.__size is 0:
            print("")
        for row in range(self.__size):
            for i in range(self.__size):
                print('#', end="")
            print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__init__(value)
