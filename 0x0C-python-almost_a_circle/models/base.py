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
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the object representation of json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes a JSON string representation of list_objs to a file"""
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            if list_objs:
                dicts = []
                for i in range(len(list_objs)):
                    dicts.append(list_objs[i].to_dictionary())
            f.write(Base.to_json_string(dicts))

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open(cls.__name__ + '.json', encoding='utf-8') as f:
                objs = Base.from_json_string(f.read())
            for i in range(len(objs)):
                objs[i] = cls.create(**objs[i])
            return objs
        except:
            return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance of cls with all attributes from dictionary"""
        if cls.__name__ is 'Square':
            new = cls(1)
        elif cls.__name__ is 'Rectangle':
            new = cls(1, 1)
        else:
            new = cls()
        new.update(**dictionary)
        return new
