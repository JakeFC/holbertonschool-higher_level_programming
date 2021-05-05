#!/usr/bin/python3
"""Module with Square class definition"""


class Square:
    """A class with:
    __size: optional private instance attribute created on init
    __position: optional private instance attribute create on init
    area(self): method to perform function
    size(self): property used to return __size as self.size
    size(self, value): method to set a new __size attribute
    position(self): property used to return __position as self.position
    position(self, value): method used to set new __position attribute
    my_print(self): method to print the square of '#' characters
    """
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise TypeError('size must be >= 0')
        else:
            raise ValueError('size must be an integer')
        if isinstance(position, tuple) and len(position) is 2 and \
           isinstance(position[0], int) and isinstance(position[1], int) \
           and position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size is 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for row in range(self.__size):
            for x in range(self.__position[0]):
                print(' ', end="")
            for i in range(self.__size):
                print('#', end="")
            print("")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__init__(value)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__init__(self.__size, value)
