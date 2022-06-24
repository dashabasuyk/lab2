from abc import ABC
from abc import abstractclassmethod
class Animals(ABC):
    @abstractclassmethod
    def voice(self):
        pass
class Cat(Animals):
    def voice(self):
        return "Meow"
class Dog(Animals):
    def voice(self):
        return "Gaw"
class Frog(Animals):
    def voice(self):
        return "Kwa"
class Wolf(Animals):
    def voice(self):
        return "Auu"
