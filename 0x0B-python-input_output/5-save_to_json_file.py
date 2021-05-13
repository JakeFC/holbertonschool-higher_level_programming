#!/usr/bin/python3
"""Module for save_to_json_file function"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON representation"""
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        obj = json.dumps(my_obj)
        f.write(obj)
