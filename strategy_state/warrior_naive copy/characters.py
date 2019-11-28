class Warrior():
    id=0
    initEnergy=50

    def __init__(self):
        self.id=Warrior.id
        Warrior.id+=1
        #self.energy=Warrior.initEnergy # class name embedded in the code!
        #self.energy=self.initEnergy #initEnergy SEEMS TO BE an instance attribute!
        #self.energy=self.__class__.initEnergy #OK!
        self.energy=type(self).initEnergy #OK!
        

    def gain(self, x):
        if self.energy<60:
            self.energy += 3*x + 1
        elif self.energy>=60:
            self.energy += 4*x + 3

    def loss(self, x):
        if self.energy<60:
            self.energy -= x + 1
        elif self.energy>=60:
            self.energy -= 0.5*x + 1

