#!/usr/bin/pthon3
"""
Task 1: my_list
"""


class MyList(list):
    """MyList class"""
    def __init__(self):
        """Initialize Class"""
        super().__init__()

    def print_sorted(self):
        """ Function that prints a sorted list"""
        print(sorted(self))
