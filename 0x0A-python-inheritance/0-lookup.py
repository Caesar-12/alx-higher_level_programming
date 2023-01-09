#!/usr/bin/python3
"""
Module: 0-lookup
contains function lookup: returns all attributes and methods
"""


def lookup(obj):
    """Retuens a list of all attributes and methods"""
    #keyList = list(obj.__dict__.keys())
    #print(sorted(keyList))
    #return (sorted(keyList))

    if obj and type(obj) is type:
        return dir(obj)
    else:
        raise TypeError("obj must be a class or subclass")
