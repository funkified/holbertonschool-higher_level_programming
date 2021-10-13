#!/usr/bin/python3
"""
Task1
"""


def write_file(filename="", text=""):
    """ write a file """
    with open("my_first_file.txt", mode="w", encoding="utf8") as f:
        return f.write(text)
