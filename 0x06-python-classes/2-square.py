#!/usr/bin/python3
"""Define a class named square"""


class Square:
    """Here is a place to class attributes"""

    def __init__(self, size=0):
        """Initialize the data with errorhandling"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
