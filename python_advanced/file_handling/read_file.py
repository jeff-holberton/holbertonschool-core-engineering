#!/usr/bin/env python3
"""read_file"""

def read_file(filename=""):
    """read_file function"""
    with open(filename) as f:
        print(f.read())
