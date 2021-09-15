#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    first = sentence[0]
    if sentence == 0:
        first = None
    return [size, first]
