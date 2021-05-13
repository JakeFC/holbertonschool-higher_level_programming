#!/usr/bin/python3
"""Module for class Student"""


class Student:
    """class with instance attributes: first_name, last_name, and age,
    and public method to_json"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of Student object with only listed
        attributes, or all if missing input"""
        if type(attrs) is not list:
            return self.__dict__
        d = {}
        for a in attrs:
            if a in self.__dict__:
                d[a] = self.__dict__[a]
        return d
