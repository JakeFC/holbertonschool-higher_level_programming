#!/usr/bin/python3
"""Module for append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text (new_string) to filename after each line
    containing search_string"""
    with open(filename, 'r', encoding='utf-8') as f:
        s = ""
        while 1:
            line = f.readline()
            if not line:
                break
            s += line
            if line.find(search_string) != -1:
                s += new_string
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(s)
