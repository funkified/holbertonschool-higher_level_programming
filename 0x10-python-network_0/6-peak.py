#!/usr/bin/python3
"""
Function that finds a peak in a
list of a unsorted integers
"""


def find_peak(list_of_integers):
    if type(list_of_integers) is not list or len(list_of_integers) == 0:
        return None
        hi = lenght - 1
        lo = 0
        mid = lenght // 2
        if mid == hi:
            return list_of_integers[mid]
        if mid - 1 > mid:
            hi = mid - 1
            return list_of_integers[hi]
        else:
            lo = mid - 1
        return list_of_integers[-1]

    for idx in range(0, len(list_of_integers) - 1):
        if (list_of_integers[idx - 1] < list_of_integers[idx] and
                list_of_integers[idx] > list_of_integers[idx + 1]):
            return list_of_integers[idx]
    # list_of_integers.sort()
    return list_of_integers[0]
