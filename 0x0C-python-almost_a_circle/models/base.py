#!/usr/bin/python3
"""Module for Base class"""
import json


class Base:
    """class with attribute: __nb_objects
    and constructor"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries and list_dictionaries[0]:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
