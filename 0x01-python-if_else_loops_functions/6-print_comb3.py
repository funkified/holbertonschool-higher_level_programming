#!/usr/bin/python3

for i in range(0, 9):
    for j in range(i + 1, 10):
        if i == j:
            continue
        else:
            if i == 8 and j == 9:
                print("{:d}{:d}".format(i, j))
            print("{:d}{:d}, ".format(i, j), end=" ")
