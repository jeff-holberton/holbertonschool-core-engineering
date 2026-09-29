#!/usr/bin/env python3
"""animals"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal Abstract Class"""

    @abstractmethod
    def sound(self):
        """sound abstract method"""
        pass


class Dog(Animal):
    """Dog Concrete Class"""

    def sound(self):
        """sound concrete method"""
        return "Bark"


class Cat(Animal):
    """Cat Concrete Class"""

    def sound(self):
        """sound concrete method"""
        return "Meow"


if __name__ == "__main__":
    bobby = Dog()
    garfield = Cat()

    print(bobby.sound())
    print(garfield.sound())

    animal = Animal()
    print(animal.sound())
