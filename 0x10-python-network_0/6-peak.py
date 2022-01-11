#!/usr/bin/python3
"""
Function that finds a peak in a
list of a unsorted integers
"""


def find_peak(list_of_integers):
    """ Find peak in a list """
    if type(list_of_integers) is not list or len(list_of_integers) == 0:
        return None
        lenght = len(list_of_integers)
        hi = lenght
        lo = 0
        mid = lenght // 2
        if lenght == 1:
            return list_of_integers[1]
        if mid == hi:
            return list_of_integers[mid]
        if mid - 1 > mid:
            hi = mid - 1
            return list_of_integers[hi]
        if list_of_integers[lo] > list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] > list_of_integers[-2]:
            return list_of_integers[-1]

    for idx in range(0, len(list_of_integers)):
        if (list_of_integers[idx - 1] < list_of_integers[idx] and
                list_of_integers[idx] > list_of_integers[idx + 1]):
            return list_of_integers[idx]
    return list_of_integers[0]
