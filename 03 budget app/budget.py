import re

class Category:
    def __init__(self, nameCategory):
        self.category = nameCategory
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == False:
            return False
        else: 
            self.ledger.append({"amount": amount * (-1), "description": description})
            return True
    
    def get_balance(self):
        currentBalance = 0
        for event in self.ledger:
            currentBalance += event["amount"]
        return currentBalance

    def check_funds(self, amount): 
        if amount > self.get_balance():
            return False
        else:
            return True

    def transfer(self, amount, budgetCategory):
        #if not self.withdraw(amount, f"Transfer to {budgetCategory.category}"):
        #    return False
        #else:
        #    budgetCategory.deposit(amount, f"Transfer from {self.category}")
        #    return True
        if self.check_funds(amount) == False:
            return False
        else:
            self.withdraw(amount, f"Transfer to {budgetCategory.category}")
            budgetCategory.deposit(amount, f"Transfer from {self.category}")
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
    print( "  ")
    print( "  ")
    print( "  ")
    print( "  ")

    word_size = []
    percent = 100
    chart = "Percentage spent by category\n"

    while percent >= 0:
        chart += str(percent).rjust(3) + "|\n"
        percent = percent - 10
    
    match = re.findall("[*+]\w+[*+]", str(categories))
    chart += "    " + "-".rjust(1 + (3 * len(match)), "-") + "\n"

    for i in range(0, len(match)):
        word_size.append(len(match[i])-2)
 
    max_size = max(word_size)

    for i in range(0, len(match)):
        match[i] = (match[i].replace("*", "")).ljust(max_size, " ")
 
    for i in range(0, max_size):
        chart += "     " + (match[0][i] + "  " + match[1][i] + "  " + match[2][i] + "\n")

    return chart

    

