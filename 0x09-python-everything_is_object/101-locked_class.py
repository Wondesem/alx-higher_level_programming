#!/usr/bin/python3
# 101-locked_class.py
""" File name : 101-locked_class.py
Low memory cost: Defines a locked class
Importing any module is not allowed
        """


class LockedClass:
    """Prevent the user from instantiating new LockedClass attributes.
    prevents the user from dynamically creating new instance attributes
    except if the new instance attribute is called first_name
    """
    __lots__ = ["first_name"]
