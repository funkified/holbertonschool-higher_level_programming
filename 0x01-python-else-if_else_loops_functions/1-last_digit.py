#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
last_digit = number % 10
if number > 5:
    print("{} {} is {} and is greater than 5".format(str, number, last_digit))
if number == 0:
    print("{} {} is {} and is zero".format(str, number, last_digit))
if number < 6 and number is not 0:
    print("{} {} is {} and is less than 6 and not 0".format(str, number, last_digit))
