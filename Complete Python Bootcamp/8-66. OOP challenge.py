class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} accepted.")

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f"Withdrawal of ${amount} accepted.")
        else:
            print("Funds unavailable!")


jose = Account("Jose", 100)
print(jose)
jose.deposit(50)
jose.withdraw(75)
jose.withdraw(500)
print(jose)
