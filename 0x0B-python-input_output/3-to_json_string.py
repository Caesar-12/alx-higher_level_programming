#!/usr/bin/python3
"""
Module: 3-to_json_string
returns the JSON representation of objects
"""

import json


def to_json_string(my_obj):
    """returns json objects"""

    json_obj = json.dumps(my_obj)

    return json_obj
