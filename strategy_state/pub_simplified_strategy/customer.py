
class Customer():
    def __init__(self, strategy):
        self.cost=0
        self.getPriceStrategy=strategy

    def printBill(self):
        print (self.cost)

    def addDrink(self,n,unitCost):
        self.cost+= self.getPriceStrategy(n*unitCost)
