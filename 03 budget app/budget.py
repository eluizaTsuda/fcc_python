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
    if self.check_funds(amount) == False:
      return False
    else:
      self.withdraw(amount, f"Transfer to {budgetCategory.category}")
      budgetCategory.deposit(amount, f"Transfer from {self.category}")
      return True

  def __repr__(self):

    num_star = (30 - len(self.category)) // 2
    line_result = ""
    line_header = ""

    line_result = line_header.ljust(num_star, "*") + self.category + line_header.rjust(num_star, "*") + "\n"  

    for item in self.ledger:
      amount = "{:.2f}".format(item["amount"])  # two digits after the decimal point
      num_space = 30 - (len(item["description"][0:23]))

      line_result += item["description"][0:23] + str(amount).rjust(num_space, " ") + "\n"
  
    totBalance = "{:.2f}".format(self.get_balance())
    
    line_result += f"Total: {totBalance}"
    
    return(line_result)

def create_spend_chart(categories):
    #------------------------------------------------------
    #print(categories[0].ledger)
    #[{'amount': 1000, 'description': 'initial deposit'}, 
    # {'amount': -10.15, 'description': 'groceries'}, 
    # {'amount': -20, 'description': 'groceries'}, 
    # {'amount': -15.89, 'description': 'restaurant and more food for dessert'}, 
    # {'amount': -50, 'description': 'Transfer to Clothing'}]
    # total_withdraw_categ = 96.04
    #print(categories[1].ledger)
    #[{'amount': 50, 'description': 'Transfer from Food'}, 
    # {'amount': -10, 'description': 'shoes'}]
    # total_withdraw_categ = 10.00
    #print(categories[2].ledger)
    #[{'amount': 1000, 'description': 'initial deposit'}, 
    # {'amount': -15.5, 'description': 'gas'}]
    # total_withdraw_categ = 15.5
    #
    # total_withdraw = 96.04 + 10.00 + 15.5 = 121.54
    # categ_perc = {'Food': 79, 'Clothing': 8, 'Auto': 13}
    #------------------------------------------------------

    # total of withdrawl and percentage
    categ_perc = {} # key=category | value=total withdraw
    total_withdraw = 0

    for categ in categories:
        total_withdraw_categ = 0
        for item in categ.ledger:
            if item["amount"] < 0:
                total_withdraw += item["amount"]
                total_withdraw_categ += item["amount"]
        categ_perc[categ.category] = abs(total_withdraw_categ)
    total_withdraw = abs(total_withdraw)

    for key, value in categ_perc.items():
        categ_perc[key] = round((value / total_withdraw) * 100)
    
    list_categ = list(categ_perc.keys())
    list_percent = list(categ_perc.values())

    # chart with the percentage spent in each category
    chart = "Percentage spent by category\n"
    percent = 100

    while percent >= 0:
        chart += str(percent).rjust(3) + "| "
        for i in range(0,len(list_percent)):
            if list_percent[i] >= percent:
                chart +=  "o".ljust(3)
            else:
                chart +=  " ".ljust(3)
         
        chart += "\n"            
        
        percent = percent - 10
     
    # horizontal line below the bars
    chart += "    " + "-".rjust(1 + (3 * len(list_categ)), "-") + "\n"

    # identify maximo length of categories
    word_size = []
    for i in range(0, len(list_categ)):
        word_size.append(len(list_categ[i]))

    max_size = max(word_size)

    # adjust each category to maximum length
    for i in range(0, len(list_categ)):
        list_categ[i] = (list_categ[i].replace("*", "")).ljust(max_size, " ")

    # display categories vertically 
    for i in range(0, max_size):
      chart += "     "
      for category in range(0, len(list_categ)):
        chart += (list_categ[category][i]) + "  "
      chart += "\n"
    
    chart = chart[:-1]

    return chart