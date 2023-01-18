#!/usr/bin/python3
"""
Module: base
defines a class Base
"""


class Base():
    """
    Class: Base
    manages id attribute for other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
