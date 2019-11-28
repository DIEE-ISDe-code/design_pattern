
from abc import ABC, abstractmethod

class Warrior(ABC):
    id=0
    initEnergy=50

    def __init__(self):
        self.id=type(self).id
        type(self).id+=1
        # self.id=Knight.id # class name embedded in the code!
        # Knight.id+=1 # class name embedded in the code!

        self.energy=type(self).initEnergy #OK!
        #self.energy=Knight.initEnergy # class name embedded in the code!
        #self.energy=self.initEnergy #initEnergy SEEMS TO BE an instance attribute!
        #self.energy=self.__class__.initEnergy #OK!

    @abstractmethod
    def gain(self, x):
        pass

    @abstractmethod
    def loss(self, x):
        pass

class Knight(Warrior):
    def gain(self, x):
            self.energy += 4*x + 3

    def loss(self, x):
            self.energy -= 0.5*x + 1

class Archer(Warrior):
    def gain(self, x):
            self.energy += 3*x + 1

    def loss(self, x):
            self.energy -= x + 1
