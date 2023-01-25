class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  """ Displays users name and account balance"""
  def __repr__(self):
    return "%s's account balance: $%.2f" % (self.name, self.balance)
  """ Shows Users Balance"""
  def show_balance(self):
    return "$%.2f" % (self.balance)
  """ Function for deposit """
  def deposit(self, amount):
    if amount <= 0:
      print "Error"
      return
    else: 
      print "Deposit Amount: $%.2f" % (amount)
      self.balance += amount
      self.show_balance()
  
  """ Allows user to withdraw """
  def withdraw(self, amount):
    if amount > self.balance:
      print "ERROR. Withdraw greater than amount available"
      return
    else:
      print "Withdraw Amount: $%.2f" % (amount)
      self.balance -= amount
      self.show_balance()
    
my_account = BankAccount("Kaylen")
print my_account.__repr__()
my_account.balance
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account.__repr__()
