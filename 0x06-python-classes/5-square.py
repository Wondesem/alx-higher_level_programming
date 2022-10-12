#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """The class that defines a square"""

    def __init__(self, size=0):
        """Constructor of the Square class"""
        self.size = size

    @property
    def size(self):
        """The __size getter"""
        return self.__size

    @size.setter
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

    def my_print(self):
        """Porints in stdout the square with the character #"""
        if self.size is 0:
            print()
        else:
            for i in range(0, self.size):
                print("#" * self.size)
