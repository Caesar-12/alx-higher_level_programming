#!/usr/bin/python3

"""
Module: 4-print_square
Prints a square with '#'
"""


def print_square(size):

    """
    Function: print_square
    prints square
    """

    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0 and type(size) is not float:
        raise ValueError("size must be >= 0")
    elif size < 0 and type(size) is float:
        raise TypeError("size must be an integer")

    if size == 0:
        print()
        return
    for length in range(size):
        for width in range(size):
            print("#", end="")
        print()
