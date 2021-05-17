#!/usr/bin/python3
"""Module for class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """subclass of Rectangle with custom __str__"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ('[Square] (' + str(self.id) + ') ' + str(self.x) + '/' +
                str(self.y) + ' - ' + str(self.size))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            Rectangle.t_error('width')
        if value <= 0:
            Rectangle.v_error1('width')
        self.width = value
        self.height = value
