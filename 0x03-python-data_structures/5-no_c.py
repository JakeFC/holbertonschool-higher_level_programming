#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    new = my_string.translate({ord('c'): None})
    new = new.translate({ord('C'): None})
    return new
