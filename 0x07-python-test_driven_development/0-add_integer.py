#!/usr/bin/python3
"""
Task: 0-add_integer
Test: Cases for unittest
Args: a+b
"""


def add_integer(a, b=98):
    """
    Add integers:    a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
