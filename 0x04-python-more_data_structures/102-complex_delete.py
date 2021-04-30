#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return a_dictionary
    while True:
        for x in a_dictionary:
            if a_dictionary.get(x) is value:
                del a_dictionary[x]
                break
        else:
            break
    return a_dictionary
