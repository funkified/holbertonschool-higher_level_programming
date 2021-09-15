#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    first = sentence[0]
    if sentence:
        return [size, first]
    else:
        return None
