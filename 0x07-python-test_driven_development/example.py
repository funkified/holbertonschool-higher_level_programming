#!/usr/bin/python3
def uniq(list):
    """ Returns unique values of a list"""
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
        return u_list

my_list = uniq(list)
print(my_list)
