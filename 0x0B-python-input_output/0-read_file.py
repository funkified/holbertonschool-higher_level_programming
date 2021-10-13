#!/usr/bin/python3
"""
task1
"""


def read_file(filename=""):
    """read a file"""
    with open(filename, 'r', encoding="utf8") as f:
        print(f.read(), end="")
