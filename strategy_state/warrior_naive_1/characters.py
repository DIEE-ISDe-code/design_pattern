class Warrior():
    knight_id=0  
    archer_id=0
    initEnergy=50

    def __init__(self,category):

        self.energy=type(self).initEnergy #OK!
        #self.energy=Knight.initEnergy # class name embedded in the code!
        #self.energy=self.initEnergy #initEnergy SEEMS TO BE an instance attribute!
        #self.energy=self.__class__.initEnergy #OK!
        
        self.category=category #archer or knight
        
        if self.category=='knight':
            self.id=Warrior.knight_id
            Warrior.knight_id+=1
        if self.category=='archer':
            self.id=Warrior.archer_id
            Warrior.archer_id+=1


    def gain(self, x):
        if self.category=='knight':
            self.energy += 4*x + 3
        if self.category=='archer':
            self.energy += 3*x + 1                   

    def loss(self, x):
        if self.category=='knight':
            self.energy -= 0.5*x + 1
        if self.category=='archer':
            self.energy -= x + 1
            
