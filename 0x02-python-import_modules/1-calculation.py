#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 5
b = 10

print("{:n} + {:n} = {:n}".format(a, b, add(a, b)))
print("{:n} - {:n} = {:n}".format(a, b, sub(a, b)))
print("{:n} / {:n} = {:n}".format(a, b, div(a, b)))
print("{:n} * {:n} = {:n}".format(a, b, mul(a, b)))

if __name__ == "__main__":
    add(a, b)
    sub(a, b)
    div(a, b)
    mul(a, b)
