#!/usr/bin/python3
"""
Module: 5-save_to_json_file
save json representation of an object to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """writes object to file using json depresentation"""

    json_obj = json.dumps(my_obj)

    with open(filename, "w") as fd:
        fd.write(json_obj)
