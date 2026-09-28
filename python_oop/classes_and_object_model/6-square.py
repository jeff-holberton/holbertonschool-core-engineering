#!/usr/bin/env python3
"""Square class definition program"""


class Square:
    """Square class definition"""
    def __init__(self, size=0, position=(0, 0)):
        """Definition of init method"""
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

        if (
            isinstance(position, tuple)
            and len(position) == 2
            and all(isinstance(n, int) and n >= 0 for n in position)
        ):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    def my_print(self):
        """print a square method"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print('\n' * self.__position[1], end="")
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    @property
    def position(self):
        """position getter method"""
        return self.__position

    @position.setter
    def position(self, position):
        """position setter method"""
        if (
            isinstance(position, tuple)
            and len(position) == 2
            and all(isinstance(n, int) and n >= 0 for n in position)
        ):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def __str__(self):
        """str"""
        str = ""
        if self.__size == 0:
            return str
        for i in range(self.__size):
            str += '\n' * self.__position[1]
            str += " " * self.__position[0]
            str += "#" * self.__size
            str += '\n'
        return str
