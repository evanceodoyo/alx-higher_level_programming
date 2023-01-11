#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """Return a JSON representation of obj
    """
    return json.dumps(my_obj)
