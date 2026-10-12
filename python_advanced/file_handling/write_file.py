#!/usr/bin/env python3
"""write_file"""


def write_file(filename="", text=""):
    """write_file function"""
    with open(filename, 'w') as f:
        char_read = f.write(text)
    return char_read
