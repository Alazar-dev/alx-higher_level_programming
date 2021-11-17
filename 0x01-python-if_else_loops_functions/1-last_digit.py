#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
str = "Last digit of"
if number < 0:
    last_digit = ((-number) % 10) * -1
else:
    last_digit = number % 10
if last_digit > 5:
    print(str, number, "is", last_digit, 'and is greater than 5')
elif last_digit == 0:
    print("str", number, "is", last_digit, 'and is 0')
else:
    print("str", number, "is", last_digit, "and is less than 6 and not 0")
