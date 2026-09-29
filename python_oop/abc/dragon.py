#!/usr/bin/env python3
"""dragon"""

from abc import ABC


class SwimMixin():
    """SwimMixin"""

    def swim(self):
        """swim"""
        print("The creature swims!")


class FlyMixin():
    """FlyMixin"""

    def fly(self):
        """fly"""
        print("The creature flies!")


class Dragon(FlyMixin, SwimMixin):
    """Dragon"""

    def roar(self):
        """roar"""
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()
    dragon.roar()
    dragon.fly()
    dragon.swim()
