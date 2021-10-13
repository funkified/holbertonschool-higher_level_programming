#!/usr/bin/python3
"""
Module that writes a string to at text file
"""


def write_file(filename="", text=""):
    """ write a file """
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
