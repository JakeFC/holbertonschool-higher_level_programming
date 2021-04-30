#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0
    n, p = 0, 0
    for x in roman_string:
        if p is 'I' and (x is 'V' or x is 'X'):
            n -= 2
        if p is 'X' and (x is 'L' or x is 'C'):
            n -= 20
        if p is 'C' and (x is 'D' or x is 'M'):
            n -= 200
        if x is 'I':
            n += 1
        elif x is 'V':
            n += 5
        elif x is 'X':
            n += 10
        elif x is 'L':
            n += 50
        elif x is 'C':
            n += 100
        elif x is 'D':
            n += 500
        else:
            n += 1000
        p = x
    return n
