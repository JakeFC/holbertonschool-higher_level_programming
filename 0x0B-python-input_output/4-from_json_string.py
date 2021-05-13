#!/usr/bin/python3
"""Module for from_json_string function"""


def from_json_string(my_str):
    """Returns a Python object representation of my_str"""
    import json
    return json.loads(my_str)
