#!/usr/bin/python3
"""
module: 9-rectangle
BaseGeometry subclass
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class: Rectangle
    childclass ofBaseGeometry
    """

    def __init__(self, width, height):
        super().__init__()
        bge = BaseGeometry()
        self.__width = width
        self.__height = height
        bge.integer_validator("width", self.__width)
        bge.integer_validator("height", self.__height)

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
