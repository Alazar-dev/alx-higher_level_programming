#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
str = "Last digit of"
if number < 0:
    last_digit = ((-number) % 10) * -1
else:
    last_digit = number % 10
if (last_digit > 5):
    print("{} {:d} is {:d} and is greater than 5"
          .format(str, number, last_digit))
elif (last_digit == 0):
    print("{} {:d} is {:d} and is 0".format(str, number, last_digit))
else:
    print("{} {:d} is {:d} and is less than 6 and not 0"
          .format(str, number, last_digit))