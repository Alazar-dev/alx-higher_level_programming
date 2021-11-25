#!/usr/bin/python3
import sys


def number_of_arguments():
    length = len(sys.argv)

    if length == 1:
        print("0 argument")
    elif length == 2:
        print("{} argument: ".format(length - 1))
        print("{}, {}".format(1, sys.argv[1]))
    else:
        print("{} arguments: ".format(length - 1))
        for i in range(1, length):
            print("{}, {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    number_of_arguments()