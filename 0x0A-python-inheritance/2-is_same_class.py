#!/usr/bin/python3
"""Module for is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True of False for whether obj is a member of a_class"""
    if type(obj) is a_class:
        return True
    return False
