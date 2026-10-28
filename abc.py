from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__ (self, name):
        self.name=name
    def make_sound(self):
        pass
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        print(f"{self.name} says Woof!")
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        print(f"{self.name} says Meow!")
Thomas=Cat("Thomas")
Spike=Dog("Spike")
Spike.make_sound()
Thomas.make_sound()
        
