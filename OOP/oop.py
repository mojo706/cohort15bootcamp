class BankAccount: #Class Definition
    def __init__(self): 
        self.balance = 0

#Some Class Methods
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

# Inheritance at it's best
class PremiumAccount(BankAccount):
    def __init__(self, least_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self,amount): #Polymorphism => withdraw only withdraws amounts > minimum_balance
        if self.balance - amount < self.minimum_balance:
            print "You cannot withdraw more than your minimum balance, do you want an overdraft?"
        else:
            BankAccount.withdraw(self, amount)
