
from customer import Customer
from strategy import getActualPriceNormal
from strategy import getActualPriceHappyHour

# NORMAL BILLING

customer1=Customer(getActualPriceNormal)
customer1.addDrink(1, 7)

# START HAPPY HOUR (50% discount)

customer1.getPriceStrategy=getActualPriceHappyHour
customer2=Customer(getActualPriceHappyHour)

customer2.addDrink(1, 7)

customer1.addDrink(2, 5)
customer2.addDrink(2, 5)

# FINAL BILL

customer1.printBill() # 12
customer2.printBill() # 8.5




