#!/usr/bin/python3

"""
Module: 0-add_integer
receives and adds two integers
"""


def add_integer(a, b=98):

    """
    Function: add_integer
    receives two integers and return their sum
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
