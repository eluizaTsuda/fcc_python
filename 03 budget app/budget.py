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
    if self.check_funds(amount) == False:
      return False
    else:
      self.withdraw(amount, f"Transfer to {budgetCategory.category}")
      budgetCategory.deposit(amount, f"Transfer from {self.category}")
      return True

  def get_withdraw_amount (self):
    amount = 0 
    
    for i in self.ledger:
      if i["amount"] > 0:
        amount += i["amount"]
    return amount

  def __repr__(self):

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

    #print(categories)
    

    word_size = []
    percent = 100
    total_withdraw = 0
    chart = "Percentage spent by category\n"

    # Percentage calculation






    percent_category = [ 70, 10, 50]  #### for now
  
    # draw the % spent by category
    while percent >= 0:
        chart += str(percent).rjust(3) + "| "
        for i in range(0,len(percent_category)):
            if percent_category[i] >= percent:
                chart +=  "o".ljust(3)
            else:
                chart +=  " ".ljust(3)
        chart = (chart.rstrip()) + "\n"            
        percent = percent - 10

     
    # Identify categories 
    match = re.findall("[*+]\w+[*+]", str(categories))

    # horizontal line below the bars
    chart += "    " + "-".rjust(1 + (3 * len(match)), "-") + "\n"

    # identify maximo length of categories
    for i in range(0, len(match)):
        word_size.append(len(match[i])-2)

    max_size = max(word_size)

    # adjust each category to maximum length
    for i in range(0, len(match)):
        match[i] = (match[i].replace("*", "")).ljust(max_size, " ")

    # display categories vertically 
    for i in range(0, max_size):
      chart += "     "
      for category in range(0, len(match)):
        chart += (match[category][i]) + "  "
      chart += "\n"

    return chart