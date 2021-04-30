#!/usr/bin/python3
def number_keys(a_dictionary):
    if a_dictionary is None:
        return
    count = 0
    for x in a_dictionary:
        count += 1
    return count
