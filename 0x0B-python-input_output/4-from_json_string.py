#!/usr/bin/python3
"""
Module: 3-to_json_string
returns objects represented by json strings
"""

import json
from io import StringIO

def from_json_string(my_obj):
    """returns objects represented by json strings"""

    io = StringIO(my_obj)
    json_obj = json.load(io)

    return json_obj
