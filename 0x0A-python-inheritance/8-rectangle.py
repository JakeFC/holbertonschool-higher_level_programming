#!/usr/bin/python3
"""Module for BaseGeometry and Rectangle classes"""


class BaseGeometry:
    """Class with public method area() that raises an exception
    and public method integer_validator which validates a value
    """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


class Rectangle(BaseGeometry):
    """Class with private instance attributes width and height"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        self.__height = height
