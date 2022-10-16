#!/usr/bin/python3
"""A module to add two numbers

This module performs the addition of two numbers
of type integer or float

"""


def add_integer(a, b=98):
    """Returns the addition of a and b as integer

    a and b must be cast into integer before
    addition if either of them is float
    
    Raises:
        TypeError a and b must be integers or floats
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
