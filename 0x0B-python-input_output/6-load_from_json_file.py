#!/usr/bin/python3
"""Module for load_from_json_file function"""


def load_from_json_file(filename):
    """Creates an object from JSON file [filename]"""
    import json
    with open(filename, encoding='utf-8') as f:
        return json.loads(f.read())
