#!/usr/bin/python3
"""Module for class BaseGeometry"""


class BaseGeometry:
    """Class with public method area() that raises an exception"""
    def area(self):
        raise Exception('area() is not implemented')
