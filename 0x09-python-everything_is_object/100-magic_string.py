#!/usr/bin/python3
def magic_string(c=[0]):
    c[0] += 1
    return (", ".join(['Holberton' for i in range(c[0])]))
