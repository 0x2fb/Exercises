# Define Bank Account Below:
class BankAccount(object):

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
