#!/usr/bin/env python3
"""Shapes"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Shape abstract class"""

    @abstractmethod
    def area(self):
        """area abstract method"""
        pass

    @abstractmethod
    def perimeter(self):
        """perimeter abstract method"""
        pass


class Circle(Shape):
    """Circle concrete class"""

    def __init__(self, radius):
        """init"""
        self.__radius = radius

    def area(self):
        """area"""
        return self.__radius * self.__radius * 3.141592653589793

    def perimeter(self):
        """perimeter"""
        return 2 * self.__radius * 3.141592653589793


class Rectangle(Shape):
    """Circle concrete class"""

    def __init__(self, width, height):
        """init"""
        self.__width = width
        self.__height = height

    def area(self):
        """area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter"""
        return self.__width * 2 + self.__height * 2


def shape_info(shape):
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
