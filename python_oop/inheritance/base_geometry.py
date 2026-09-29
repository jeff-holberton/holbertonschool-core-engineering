#!/usr/bin/env python3
"""Base geometry"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """area exception method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator method"""
        if isinstance(value, int) is False:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
