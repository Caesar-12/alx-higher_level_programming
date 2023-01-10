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
        # super().__init__()
        rec = Rectangle(1, 1)
        self.__size = size
        rec.integer_validator("size", self.__size)

    def area(self):
        return (self.__size * self.__size)
