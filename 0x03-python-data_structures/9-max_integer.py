#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return
    tmp = my_list.copy()
    tmp.sort()
    return tmp.pop()
