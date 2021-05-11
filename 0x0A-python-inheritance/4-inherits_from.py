#!/usr/bin/python3
"""Module for inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True of False for whether obj is inherited from a_class"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
