#!/usr/bin/env python3
"""flyingfish"""

from abc import ABC


class Fish(ABC):
    """abstract fish class"""

    def swim(self):
        """swim"""
        print("The fish is swimming")

    def habitat(self):
        """habitat"""
        print("The fish lives in water")


class Bird(ABC):
    """abstract bird class"""

    def fly(self):
        """fly"""
        print("The bird is flying")

    def habitat(self):
        """habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """flyingfish"""

    def fly(self):
        """fly"""
        print("The flying fish is soaring!")

    def swim(self):
        """swim"""
        print("The flying fish is swimming!")

    def habitat(self):
        """habitat"""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    print(FlyingFish.mro())
