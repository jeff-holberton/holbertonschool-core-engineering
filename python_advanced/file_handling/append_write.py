#!/usr/bin/env python3
"""append_write"""


def append_write(filename="", text=""):
    """append_write function"""
    with open(filename, 'a') as f:
        char_added = f.write(text)
    return char_added
