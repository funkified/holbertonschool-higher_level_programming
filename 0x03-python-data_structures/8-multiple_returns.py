#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    first = sentence[0]
    if size > 0:
        return (size, first)
    else:
        None
