#!/usr/bin/python3


class Square:
    """The class that defines a square"""
    def __init__(self, size=0):
        """Constructor of the Square class"""
        self.size = size

    def size(self):
        """The __size getter"""
        return (self.__size)**2

    @property
    def size(self):
        """The __size setter"""
        return size.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
