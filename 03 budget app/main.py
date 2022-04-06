# This entrypoint file to be used in development. Start by reading README.md
import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(750.15, "groceries")
food.withdraw(150.89, "restaurant and more food for dessert")
print("{:.2f}".format(food.get_balance()))
     
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55, "jacket")
clothing.withdraw(100, "dress")
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15, "gas")
entertainment = budget.Category("Entertainment")
auto.transfer(500, entertainment)
entertainment.withdraw(85, "games")
entertainment.withdraw(180, "travel")

print(food)
print(clothing)
print(auto)
print(entertainment)

print(create_spend_chart([food, clothing, auto, entertainment]))

# Run unit tests automatically
#main(module='test_module', exit=False)