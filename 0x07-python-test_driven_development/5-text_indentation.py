#!/usr/bin/python3
"""
Task 5
"""


def text_indentation(text):
    """
    Method to print a string
    Text: string to print
        if is not a string raise exception
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip()
    for i in text:
        if i not in ['.', '?', ':']:
            print(i, end="")
        else:
            print(i)
            print('\n')
