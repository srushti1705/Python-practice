class Cart:
    flat_discount = 0 
    min_bill = 100 
    def __init__(self):
        self.items = {} 
    
    @classmethod
    def update_flat_discount(cls, new_flat_discount):
        cls.flat_discount = new_flat_discount 

    @classmethod
    def increase_flat_discount(cls, amount):
        cls.flat_discount += amount 
        cls.update_flat_discount(cls.flat_discount) 

    @staticmethod 
    def greet():
        print("Have a great shopping experience!") 

print(Cart.flat_discount)
Cart.increase_flat_discount(50) 
print(Cart.flat_discount)
Cart.greet()