#!/usr/bin/python3
if __name__ = "__main__":
    from sys import argv
    add = 0
    for x in argv[1:]:
        add += int(x)
        print("{:d}".format(add))
