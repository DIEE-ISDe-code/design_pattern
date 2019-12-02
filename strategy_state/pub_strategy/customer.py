
class Customer(object):
    def __init__(self, strategy):
        self.cost=0
        self._strategy=strategy
        #self._strategy=self.set_strategy(strategy)
    def printBill(self):
        print (self.cost)

    def addDrink(self,n,unitCost):
        self.cost+= self._strategy.getActualPrice(n*unitCost)
        
    def set_strategy(self,strategy):
        self._strategy=strategy
        
