#!/usr/bin/python3
"""Defines a function to add two integers"""

def add_integer(a, b=98):
    """Return the integer addition of a and b.
    a and are first casted to integers if they are float.
    
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
     return int(a) + int(b)
