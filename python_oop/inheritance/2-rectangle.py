#!/usr/bin/env python3
"""Rectangle class"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """area exception method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator method"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
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
