class BankAccount:
    def __init__(self, acc_number):
        self.acc_number = acc_number
        self.balance = 0

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")
        
    def deposit(self, amount):
        self.balance += amount

def transfer_amount(acc_1, acc_2, amount):
    try:
        acc_1.withdraw(amount)
        acc_2.deposit(amount)
        return True 
    except ValueError:
        return False
    
user_1 = BankAccount("001") 
user_2 = BankAccount("002")
user_1.deposit(250)
user_2.deposit(100) 

print("User 1 balance: {}".format(user_1.balance))
print("User 2 balance: {}".format(user_2.balance))

print(transfer_amount(user_1, user_2, 50))

print("Transferring 50 from User 1 to User 2..." )
print("User 1 balance: {}".format(user_1.balance))
print("User 2 balance: {}".format(user_2.balance)) 