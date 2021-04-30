#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return
    max, name = 0, None
    for x in a_dictionary:
        n = a_dictionary[x]
        if n > max:
            max, name = n, x
    return name
