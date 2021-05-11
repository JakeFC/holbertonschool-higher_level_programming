#!/usr/bin/python3
"""Module for add_attribute function"""


def add_attribute(obj, attribute, value):
    if obj.__class__.__module__ == 'builtins':
        raise TypeError('can\'t add new attribute')
    if hasattr(obj, '__slots__'):
        if attribute in obj.__slots__:
            setattr(obj, attribute, value)
            return
        else:
            raise TypeError('can\'t add new attribute')
    setattr(obj, attribute, value)
