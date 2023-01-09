#!/usr/bin/python3
"""
Module: 2-is_same_class
Checks if its and exact instance
"""


def is_same_class(obj, a_class):
    """returns true if exact instance"""

    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
