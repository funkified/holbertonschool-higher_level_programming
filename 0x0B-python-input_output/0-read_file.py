#!/usr/bin/python3
"""
Mwethod that reads the content of a text file
"""


def read_file(filename=""):
    """read a file"""
    with open(filename, 'r', encoding='UTF-8') as f:
        print(f.read(), end="")
