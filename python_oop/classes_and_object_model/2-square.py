#!/usr/bin/env python3
"""Square class definition program"""


class Square:
    """Square class definition"""
    def __init__(self, size):
        """Definition of init method"""
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
