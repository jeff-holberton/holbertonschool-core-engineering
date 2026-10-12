#!/usr/bin/env python3
"""read_file"""


def read_file(filename=""):
    """read_file function"""
    with open(filename) as f:
        char_read = print(f.read(), end="")
    return char_read
