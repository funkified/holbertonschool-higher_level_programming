#!/usr/bin/python3
"""
Task 3
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the ojbect is an instance of a class that inherited from
    specified class, otherwise, False
    """
    return isinstance(obj, a_class)
