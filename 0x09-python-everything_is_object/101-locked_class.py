#!/usr/bin/python3

"""
Module: 101-locked_class
class that restricts dynamic allocation of attributes
"""


class LockedClass():

    """
    Class: LockedClass
    restricts dynamic atfributes creation
    """

    __slots__ = ['first_name']

    def __init__(self, name):
        self.firstname = name
