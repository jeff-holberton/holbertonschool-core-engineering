#!/usr/bin/env python3
"""Square class definition program"""


class Square:
    """Square class definition"""
    def __init__(self, size=0):
        """Definition of init method"""
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        """area method that returns the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter method"""
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
