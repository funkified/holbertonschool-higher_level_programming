#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    key = 0
    value = 0
    for score, weight in my_list:
        key += score * weight
        value += weight
    return key / value
