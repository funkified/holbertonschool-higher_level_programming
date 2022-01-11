#!/usr/bin/python3
"""
Function that finds a peak in a
list of a unsorted integers
"""


def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    """ lenght = len(list_of_integers)
        hi = lenght - 1
        lo = 0
        mid = lenght // 2
        if mid == hi:
            return list_of_integers[mid]
        if mid - 1 > mid:
            hi = mid - 1
            return list_of_integers[hi]
        else:
            lo = mid + 1
            return list_of_integers[lo]
    """
    list_of_integers.sort()
    return list_of_integers[-1]
