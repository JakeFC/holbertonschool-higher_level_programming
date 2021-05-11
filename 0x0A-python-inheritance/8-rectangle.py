#!/usr/bin/python3
"""Module for BaseGeometry and Rectangle classes"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass of BaseGeometry with private instance attributes width and
    height
    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
