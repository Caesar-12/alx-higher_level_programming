#!/usr/bin/python3
"""
module: 10-square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class: Square
    defines a square child class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
