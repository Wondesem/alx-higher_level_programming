#!/usr/bin/python3
"""
Defines function to check kind of class
"""


def is_kind_of_class(obj, a_class):
    """The function returns True if the object is an instance of
    or if the object is an instance of a class that inherited from,
    the specified class;
    otherwise False.
    """
    return isinstance(obj, a_class)
