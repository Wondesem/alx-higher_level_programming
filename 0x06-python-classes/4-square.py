#!/usr/bin/python3


class Square:
    """The class that defines a square"""
    def __init__(self, size=0):
        """Constructor of the Square class"""
        self.size = size
        @property
    def size(self):
        """The __size getter"""
        return self.__size

    @size.sette
    def size(self, value):
        """The __size setter"""
        if value:
            if isinstance(value, int) is not True:
                raise TypeError("size must be an integer")
            return
            if value < 0:
                raise ValueError("size must be >= 0")
            return
        self.__size = value

        def area(self):
            """Returns the size of the square"""
            return self.__size ** 2
