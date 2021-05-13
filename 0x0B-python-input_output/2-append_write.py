#!/usr/bin/python3
"""Module for append_write function"""


def append_write(filename="", text=""):
    """Appends string text to a text file and returns number of characters
    written
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
