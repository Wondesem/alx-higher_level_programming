#!/usr/bin/python3
def no_c(my_string):
    char_to_remove = ["c", "C"]
    newStr = ""
    for character in my_string:
        if character != char_to_remove:
            newStr += character
            return newStr
