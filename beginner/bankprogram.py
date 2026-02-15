class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def show_balance(self):
        print("Current balance:", self.balance)

# Creating object
acc1 = BankAccount("Srushti", 1000)

acc1.deposit(500)
acc1.show_balance()
