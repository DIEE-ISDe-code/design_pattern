
from customer import Customer
import strategy



# Prepare strategies

normalStrategy=strategy.NormalStrategy()
happyHourStrategy=strategy.HappyHourStrategy()

# NORMAL BILLING

customer1=Customer(normalStrategy)
customer1.addDrink(1, 7)

# START HAPPY HOUR (50% discount)

#customer1.strategy=happyHourStrategy
customer1.set_strategy(happyHourStrategy)
customer2=Customer(happyHourStrategy)

customer2.addDrink(1, 7)

customer1.addDrink(2, 5)
customer2.addDrink(2, 5)

# FINAL BILL

customer1.printBill() # 12
customer2.printBill() # 8.5




