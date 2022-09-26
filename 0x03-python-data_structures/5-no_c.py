#!/usr/bin/python3
def no_c(my_string):
    newStr = ""
    for character in my_string:
        if character != "c" and != "C":
            newStr += character
        return newStr
