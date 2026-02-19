class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings
        self.you_save = price - deal_price

    def display_product_details(self):
        print("Product: {}".format(self.name)) 
        print("Price: ₹ {}".format(self.price))
        print("Deal Price: ₹ {}".format(self.deal_price))
        print("You Save: ₹ {}".format(self.you_save))
        print("Ratings: {}".format(self.ratings))

class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, ratings, warranty_in_months):
        super().__init__(name, price, deal_price, ratings) 
        self.warranty_in_months = warranty_in_months

    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months 

    def get_warranty(self):
        return self.warranty_in_months 
    
    def display_product_details(self):
        super().display_product_details() 
        print("Warranty: {} months".format(self.warranty_in_months)) 
 
class GroceryItem(Product):
    def __init__(self, name, price, deal_price, ratings, expiry_date):
        super().__init__(name, price, deal_price, ratings)
        self.expiry_date = expiry_date

    def display_product_details(self):
        super().display_product_details() 
        print("Expiry Date: {}".format(self.expiry_date))

class Order:
    delivery_charges = {
        "prime_membership": 0,
        "standard_delivery": 50,
    }
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address 

    def add_item_to_cart(self, product, quantity):
        self.items_in_cart.append((product, quantity)) 

    def display_order_details(self):
        print("------Product Details------")
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
            print("---------------------------")
        print("Delivery Speed: {}".format(self.delivery_speed))
        print("Delivery Address: {}".format(self.delivery_address))
        print("Delivery Charges: ₹ {}".format(self.get_delivery_charges(self.delivery_speed)))
        print("Total Bill: ₹ {}".format(self.display_total_bill())) 

    def display_total_bill(self):
        total_bill = 0 
        for product, quantity in self.items_in_cart:
            total_bill += product.deal_price * quantity + self.get_delivery_charges(self.delivery_speed)
        return total_bill

    @classmethod 
    def get_delivery_charges(cls, delivery_speed):
        return cls.delivery_charges.get(delivery_speed, 0)

tv = ElectronicItem("TV", 50000, 45000, 4.8, 24)
e = ElectronicItem("Smartphone", 20000, 15000, 4.5, 24)

milk = GroceryItem("Milk", 50, 40, 4.0, "15-08-2024")
g = GroceryItem("Rice", 1000, 800, 4.2, "31-12-2025")

order = Order("Prime Delivery", "123, Main Street") 
order.add_item_to_cart(milk, 2)
order.add_item_to_cart(tv, 1)
order.display_order_details()