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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes a JSON string representation of list_objs to a file"""
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            if list_objs:
                for i in range(len(list_objs)):
                    list_objs[i] = list_objs[i].to_dictionary()
            f.write(Base.to_json_string(list_objs))
