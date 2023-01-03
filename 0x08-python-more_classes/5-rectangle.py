#!/usr/bin/python3

"""
Module: 0-rectangle.py
Defines a class -> Rectangle
"""


class Rectangle:
    """
    Class: Rectangle
    Declares 2 class attributes and 8 methods
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        shapeList = []
        for i in range(self.__height):
            shapeList.append("#" * self.__width)
        rec = "\n".join(shapeList)
        return rec

    def __repr__(self):
        return "Rectangle("+str(self.__width)+", "+str(self.__height)+")"

    def __del__(self):
        print("Bye rectangle...")
