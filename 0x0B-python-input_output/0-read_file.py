#!/usr/bin/python3
"""
task1
"""

def read_file(filename=""):
    """read a file"""
    with open("my_file_0.txt", mode="r", encoding="utf8") as f:
        print(f.read(), end="")
