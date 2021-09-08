#!/usr/bin/python3

for i in range(0, 100):
    if i < 10:
        print("{:d}{:d},".format(0, i), end=" ")
    else:
        print("{:d},".format(i), end=" ")
    if i == 99:
        print(i)
