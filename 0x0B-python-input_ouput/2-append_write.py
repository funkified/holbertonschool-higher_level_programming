#!/usr/bin/python3
"""
Module that appends a string a th the end of a text file
"""


def append_write(filename="", text=""):
    """ return number of chars appended"""
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
