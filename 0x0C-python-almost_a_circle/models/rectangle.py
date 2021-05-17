#!/usr/bin/python3
"""Module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """subclass of Base with attributes: __width, __height, __x, & __y
    constructor, and getters and setters for each attribute"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        inputs = {'width': width, 'height': height, 'x': x, 'y': y}
        for name, v in inputs.items():
            if type(v) is not int:
                Rectangle.t_error(name)
            if v <= 0 and (name is 'width' or name is 'height'):
                Rectangle.v_error1(name)
            if v < 0 and (name is 'x' or name is 'y'):
                Rectangle.v_error2(name)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def t_error(name):
        raise TypeError(name + ' must be an integer')

    def v_error1(name):
        raise ValueError(name + ' must be > 0')

    def v_error2(name):
        raise ValueError(name + ' must be >= 0')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            Rectangle.t_error('width')
        if value <= 0:
            Rectangle.v_error1('width')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            Rectangle.t_error('height')
        if value <= 0:
            Rectangle.v_error1('height')
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            Rectangle.t_error('x')
        if value < 0:
            Rectangle.v_error1('x')
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            Rectangle.t_error('y')
        if value < 0:
            Rectangle.v_error1('y')
        self.__y = y
