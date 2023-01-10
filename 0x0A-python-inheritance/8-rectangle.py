#!/usr/bin/python3
"""
module: 8-rectangle
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
