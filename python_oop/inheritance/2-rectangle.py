#!/usr/bin/env python3
"""Rectangle class"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """init method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method that returns the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """string representation method"""
        return f"[Rectangle] {self.__width}/{self.__height}"
