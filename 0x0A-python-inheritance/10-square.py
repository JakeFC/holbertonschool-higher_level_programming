#!/usr/bin/python3
"""Module for class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass of Rectangle with private instance attribute size"""
    def __init__(self, size):
        self.integer_validator('size', size)
        Rectangle.__init__(self, size, size)
        self.__size = size
