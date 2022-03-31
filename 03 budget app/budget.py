class Category:
    def __init__(self, nameCategory):
        self.category = nameCategory
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount): 
            return False
        else: 
            self.ledger.append({"amount": amount * (-1), "description": description})
            return True
    
    def get_balance(self):
        currentBalance = 0
        for event in self.ledger:
            currentBalance += event["amount"]
        return currentBalance

    def transfer(self, amount, budgetCategory):
        if not self.withdraw(amount, f"Transfer to {budgetCategory.category}"):
            return False
        else:
            budgetCategory.deposit(amount, f"Transfer from {self.category}")
            return True

    def check_funds(self, amount): 
        if self.get_balance() < amount:
            return False
        else:
            return True


    def __repr__(self):
        # print(self.ledger)
        # [
        #   {'amount': 1000, 'description': 'initial deposit'}, 
        #   {'amount': -10.15, 'description': 'groceries'}, 
        #   {'amount': -15.89, 'description': 'restaurant and more food for dessert'}, 
        #   {'amount': -50, 'description': 'Transfer to Clothing'}
        # ]


        num_star = (30 - len(self.category)) // 2
        line_result = ""
        line_header = ""
        
        line_result = line_header.ljust(num_star, "*") + self.category + line_header.rjust(num_star, "*") + "\n"

        for item in self.ledger:
            amount = "{:.2f}".format(item["amount"])
            num_space = 30 - (len(item["description"][0:23]))

            line_result += item["description"][0:23] + str(amount).rjust(num_space, " ") + "\n"
        
        totBalance = "{:.2f}".format(self.get_balance())
        line_result += f"Total: {totBalance}"

        return(line_result)


def create_spend_chart(categories):
    pass
