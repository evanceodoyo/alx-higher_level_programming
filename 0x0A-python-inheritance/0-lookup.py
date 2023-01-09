#!/usr/bin/python3
"""Returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """function: lookup()
    Returns a list object
    """
    return dir(obj)
