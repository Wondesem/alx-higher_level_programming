#!/usr/bin/python3
"""It is MyList class document"""


class MyList(list):
    """It's a method of MyList class"""
    def __init__(self):
        """The objet is initialized using super function"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
