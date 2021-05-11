#!/usr/bin/python3
"""Module for class BaseGeometry"""


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
