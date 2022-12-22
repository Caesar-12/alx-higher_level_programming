#!/usr/bin/python3

"""
module 2-square
Set private att and set condition
"""


class Square:

    """
    Class Square
    Set private att
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
