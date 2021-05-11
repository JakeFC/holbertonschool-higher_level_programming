#!/usr/bin/python3
"""Module for BaseGeometry and Rectangle classes"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass of BaseGeometry with private instance attributes width and
    height, magic str() representation, and public area() method which
    returns area
    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
