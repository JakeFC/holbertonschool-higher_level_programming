#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        new = str
    else:
        new = str[:n] + str[n + 1:]
    return new