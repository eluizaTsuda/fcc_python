# This entrypoint file to be used in development. Start by reading README.md

import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(20, "snacks")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(250.55, "jacket")
clothing.withdraw(10, "shoes")
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15.500, "gas")

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))

# Run unit tests automatically
#main(module='test_module', exit=False)import budget