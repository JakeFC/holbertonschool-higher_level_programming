#!/usr/bin/python3
"""Module for is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Returns True of False for whether obj is a member of a_class
    or one inherited from it
    """
    return isinstance(obj, a_class)
