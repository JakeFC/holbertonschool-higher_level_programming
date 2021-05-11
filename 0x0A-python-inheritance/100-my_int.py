#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """Subclass of int which inverts __eq__ and __ne__ magic methods"""
    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
