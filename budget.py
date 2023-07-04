import math
class Category:
  # Category name ex: food, clothing and entertainment
  name = ''         
  # List of deposit and withdraws
  ledger = []   

  # Default Constructors intializing name 
  def __init__(self, name):
    self.name = name
    self.ledger = []

  # return current balance of the budget based on the 
  # deposits and withdrawals occurred
  def get_balance(self):
    balance = 0
    for transaction in self.ledger:
        balance += transaction['amount']
    return balance

  # check if the given amount can be withdrawen from
  # the current balance
  def check_funds(self, amount):
    if amount > self.get_balance():
        return False
    return True

  # Add amount of fund and description to ledger 
  def deposit(self, amount, description= ""):
    self.ledger.append({"amount": amount, "description": description})
    
  # add withdraw and description to the ledger 
  # if the balance is more than or equal the withdrawal amount
  def withdraw(self, amount, des = ""):
    if self.check_funds(amount):
      self.deposit(-amount, des)
      return True

    return False

  # Transfer fund if found from current catergory
  # to a given one 
  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {category.name}")
      category.deposit(amount, f"Transfer from {self.name}")
      return True
    return False

  # This function is called when the obj of class is 
  # printed and returns the string needed
  def __str__(self):
    s = '*' * math.ceil((30 - len(self.name))/2) + self.name + '*' * math.floor((30- len(self.name))/2) + '\n'
    
    for i in self.ledger:
      s += i['description'][:23]

      if len(i['description']) < 23:
        s += ' ' * (23 - len(i['description']))

      if len(f"{i['amount']:.2f}") < 7:
        s += ' ' * (7 - len(f"{i['amount']:.2f}"))

      s += f"{i['amount']:.2f}" + '\n'

    s += f"Total: {self.get_balance():.2f}"
    return s


def create_spend_chart(categories):
    s = "Percentage spent by category\n"

    # Calculate list of percentages of each category
    spents = []
    percentages = []
    maxLength = 0
    tot_spent = 0

    for cat in categories:
        spent = 0
        if len(cat.name) > maxLength:
          maxLength = len(cat.name)

        for i in cat.ledger:
          if i["amount"] < 0:
            spent += -i["amount"]
                   
        tot_spent += spent
        spents.append(spent)
      
    # Calculate the percentages
    for spent in spents:
      percentage = spent / tot_spent * 100
      percentages.append(percentage)
      
    for x in range(100, -1, -10):
        
      s += "{:3d}| ".format(x)

      for percent in percentages:
          if percent >= x:
              s += "o  "
          else:
              s += "   "

      s += "\n"

    s += " " * 4 + "-" * (len(percentages) * 3 + 1)

    for x in range(0, maxLength):
        s += "\n   "
        for cat in categories:
            if len(cat.name) > x:
                s += "  " + cat.name[x]
            else:
                s += "   "
        s += "  "
    return s



# #def create_spend_chart(categories):
#     s = "Percentage spent by category\n"

#     # Calculate list of percentages of each category
#     percentages = []
#     maxLength = 0

#     for cat in categories:
#         spent = 0
#         fund = 0

#         if len(cat.name) > maxLength:
#             maxLength = len(cat.name)

#         for i in cat.ledger:
#             if i["amount"] < 0:
#                 spent += -1 * i["amount"]
#             else:
#                 fund += i["amount"]

#         if spent + fund != 0:  # Avoid division by zero
#             percentages.append(round(spent / (spent + fund) * 100))
#         else:
#             percentages.append(0)

#     for x in range(100, -1, -10):
#         if len(str(x)) < 3:
#             s += " " * (3 - len(str(x)))
#         s += str(x) + "| "

#         for percent in percentages:
#             if percent >= x:
#                 s += "o  "
#             else:
#                 s += "   "

#         s += " \n"

#     s += " " * 4 + "-" * (len(percentages) * 3 + 1)

#     for x in range(0, maxLength):
#         s += "  \n   "
#         for cat in categories:
#             if len(cat.name) > x:
#                 s += "  " + cat.name[x]
#             else:
#                 s += "   "

#     return s
