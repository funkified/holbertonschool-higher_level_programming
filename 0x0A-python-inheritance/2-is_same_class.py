#!/usr/bin/python3
"""
Task 2
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of specfied class
    otherwise False
    """
    return type(obj) is a_class
