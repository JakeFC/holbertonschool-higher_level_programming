#!/usr/bin/python3
"""Script which adds all argv arguments to a Python list, then saves them to
file 'add_item.json'"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
l = []
for i in argv[1:]:
    l.append(i)
try:
    orig = load_from_json_file('add_item.json')
    l = orig + l
except:
    pass
save_to_json_file(l, 'add_item.json')
