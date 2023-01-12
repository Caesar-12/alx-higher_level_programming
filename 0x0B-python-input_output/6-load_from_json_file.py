#!/usr/bin/python3
"""
Module: 6-load_from_json_file
creates an object from json strings in a file
"""


import json
from io import StringIO


def load_from_json_file(filename):
    """creates an object from json strings in a file"""

    with open(filename, "r") as fd:
        json_obj = fd.readline()
        io = StringIO(json_obj)
        obj = json.load(io)
        return obj
