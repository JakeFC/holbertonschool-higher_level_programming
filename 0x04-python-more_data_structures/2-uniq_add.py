#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    x = 0
    for i in set(my_list):
        x += i
    return x
