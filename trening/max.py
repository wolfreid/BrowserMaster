class BankAccount():
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    print(self.name, round(self.balance, 2))
  def show_balance(self):
    print ("nice",round(self.balance, 2))
  def deposit(self, amount):
    if amount < 1:
      print ("Deposit can't be less than 1")
      return
    else:
      print (round(amount, 2))
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
      if amount > self.balance:
        print("Not enough money, asshole!")
        return
      else:
        print(round(amount, 2))
        self.balance -= amount
        self.show_balance()



my_account  = BankAccount("Vitya")
my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)