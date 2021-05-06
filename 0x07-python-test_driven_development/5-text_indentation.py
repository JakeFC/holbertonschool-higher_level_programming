#!/usr/bin/python3
"""Module for text_indentation function
"""


def text_indentation(text):
    """Prints text with 2 newlines after characters: (. ? :)"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    f = 0
    for i in range(len(text)):
        if f is 1:
            if text[i] is ' ':
                continue
            else:
                f = 0
        if text[i] is '.' or text[i] is '?' or text[i] is ':':
            f = 1
            print(text[i], sep="", end='\n\n')
        else:
            print(text[i], sep="", end="")
