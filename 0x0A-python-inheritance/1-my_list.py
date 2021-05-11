#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """Class that inherets from list, with public instance method
    print_sorted
    """
    def print_sorted(self):
        print(sorted(self))
