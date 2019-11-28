class Warrior():
    knight_id=0  
    archer_id=0
    initEnergy=50
    
    # NB: cCONCRETE STRATEGIES can be methods or  
    # can be simple functions, even belonging to another module
    
    def gain_archer(self, x):
        self.energy += 3*x + 1                   

    def loss_archer(self, x):
        self.energy -= x + 1
        
    def gain_knight(self, x):
        self.energy += 4*x + 3
        
    def loss_knight(self, x):
        self.energy -= 0.5*x + 1

    def __init__(self,category):

        self.energy=type(self).initEnergy #OK!        
        self.category=category #archer or knight
        
        
        if self.category=='knight':
            self.id=Warrior.knight_id
            Warrior.knight_id+=1
            
            self.gain=self.gain_knight
            self.loss=self.loss_knight
            
            
        if self.category=='archer':
            self.id=Warrior.archer_id
            Warrior.archer_id+=1
    
            self.gain=self.gain_archer
            self.loss=self.loss_archer


