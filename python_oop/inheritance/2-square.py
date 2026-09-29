#!/usr/bin/env python3
"""Rectangle class"""


BaseGeometry = __import__('base_geometry').BaseGeometry


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """init method"""
        super().__init__(size, size)

    def area(self):
        """method that returns the area of the square"""
        return super().area()

    def __str__(self):
        """string representation method"""
        return f"[Square] {self.__width}/{self.__height}"
