#!/usr/bin/python3

"""
module 2-square
Set private att, set condition and return square
"""


class Square:

    """
    Class Square
    Set private att, set condition and return square
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if len(value) != 2 and type(value[0]) is not int and type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def area(self):
        s_area = self.__size * self.__size
        return s_area

    def my_print(self):
        sqr = self.__size
        if sqr == 0:
            print()
        else:
            for i in range(sqr):
                for j in range(sqr):
                    print("#", end="")
                print()
