#!/usr/bin/python3
"""Module for Base class"""
import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves a list of objs of class cls to a csv file"""
        with open(cls.__name__ + '.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            if list_objs is None:
                return
            for i in list_objs:
                tmpi = []
                if cls.__name__ == 'Rectangle':
                    try:
                        tmpi.append(i.id)
                        tmpi.append(i.width)
                        tmpi.append(i.height)
                        tmpi.append(i.x)
                        tmpi.append(i.y)
                    except:
                        pass
                if cls.__name__ == 'Square':
                    try:
                        tmpi.append(i.id)
                        tmpi.append(i.size)
                        tmpi.append(i.x)
                        tmpi.append(i.y)
                    except:
                        pass
                writer.writerow(tmpi)

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of objects created from arg lists in csv file"""
        try:
            with open(cls.__name__ + '.csv', encoding='utf-8') as f:
                reader = csv.reader(f)
                tmp = []
                for line in reader:
                    d = {}
                    if cls.__name__ is 'Rectangle':
                        try:
                            d['id'] = int(line[0])
                            d['width'] = int(line[1])
                            d['height'] = int(line[2])
                            d['x'] = int(line[3])
                            d['y'] = int(line[4])
                        except:
                            pass
                    if cls.__name__ is 'Square':
                        try:
                            d['id'] = int(line[0])
                            d['size'] = int(line[1])
                            d['x'] = int(line[2])
                            d['y'] = int(line[3])
                        except:
                            pass
                    tmp.append(cls.create(**d))
                return tmp
        except:
            return []
