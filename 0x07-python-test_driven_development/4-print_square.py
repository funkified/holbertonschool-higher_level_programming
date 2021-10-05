#!/usr/bin/python3
"""
Print Square
"""


def print_square(size):
    """ Function to print a square and handling errors"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
            print("#" * size)
