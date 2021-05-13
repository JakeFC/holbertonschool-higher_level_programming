#!/usr/bin/python3
"""Module for function class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure for
    JSON serialization of object [obj]"""
    return (obj.__dict__)
