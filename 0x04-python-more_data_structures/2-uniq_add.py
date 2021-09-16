#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_uniq = []
    uniq_nums = set(my_list)
    res = 0
    for n in uniq_nums:
        list_uniq.append(n)
        res += n
    return res
