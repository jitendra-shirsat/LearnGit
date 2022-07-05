# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint:disable=missing-docstring

from abc import abstractmethod



class Animal:
    @abstractmethod
    def eat(self):
        pass



class Bird(Animal):
    def fly(self):
        print("Fly")
    def eat(self):
        print("Overriden Eat")
