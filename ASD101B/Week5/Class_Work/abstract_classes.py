# Abstract classes
# An abstract class does not allow you to instantiate it in the form /
# of an object. It can only be inherited.

from abc import ABC, abstractmethod

# This is the parent class.
class Animal(ABC):

    def move(self):
        pass

# This is the inherited or child class.
class Human(Animal):

    def move(self):
        print('I can walk and run')

me = Human()
me.move()