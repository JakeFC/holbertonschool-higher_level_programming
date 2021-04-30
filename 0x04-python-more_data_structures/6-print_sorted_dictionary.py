#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    new = sorted(a_dictionary)
    for x in new:
        print(x, ': ', a_dictionary.get(x), sep="")
