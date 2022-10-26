#!/usr/bin/python3
# 7-add_item.py
"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", "a")

try:
    lst = load_from_json_file("add_item.json")
except ValueError:
    lst = []
save_to_json_file(lst + sys.argv[1:], "add_item.json")
