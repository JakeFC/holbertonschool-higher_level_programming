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

    def __str__(self):
        return ('[Rectangle] (' + str(self.id) + ') ' + str(self.__x) + '/' +
                str(self.__y) + ' - ' + str(self.__width) + '/' +
                str(self.__height))

    def area(self):
        """returns the area of the object(width * height)"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle with character '#' to stdout"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute of Rectangle instance"""
        if args and args[0]:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except:
                pass
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def t_error(name):
        """raises a type error for non-int variable name"""
        raise TypeError(name + ' must be an integer')

    def v_error1(name):
        """raises a value error for invalid height or width(name)"""
        raise ValueError(name + ' must be > 0')

    def v_error2(name):
        """raises a value error for invalid x or y(name)"""
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
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            Rectangle.t_error('height')
        if value <= 0:
            Rectangle.v_error1('height')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            Rectangle.t_error('x')
        if value < 0:
            Rectangle.v_error2('x')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            Rectangle.t_error('y')
        if value < 0:
            Rectangle.v_error2('y')
        self.__y = value
