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
    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months 

    def get_warranty(self):
        return self.warranty_in_months 
    
    def display_electronice_product_details(self):
        self.display_product_details() 
        print("Warranty: {} months".format(self.warranty_in_months)) 
 
class GroceryItem(Product):
    def set_expiry_date(self, expiry_date):
        self.expiry_date = expiry_date

    def get_expiry_date(self):
        return self.expiry_date 
    
    def grocery_product_details(self):
        self.display_product_details() 
        print("Expiry Date: {}".format(self.expiry_date))

# p = Product("Laptop", 30000, 25000, 4)  
# p.display_product_details()

# e = ElectronicItem("Smartphone", 20000, 15000, 4.5)
# e.set_warranty(12) 
# e.display_electronice_product_details()

# g = GroceryItem("Rice", 1000, 800, 4.2)
# g.set_expiry_date("19-02-2026")
# g.grocery_product_details()

class Order:
    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address 

    def add_item_to_cart(self, product, quantity):
        self.items_in_cart.append((product, quantity)) 

    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))

    def display_total_bill(self):
        total_bill = 0 
        for product, quantity in self.items_in_cart:
            total_bill += product.deal_price * quantity 
        print("Total Bill: ₹ {}".format(total_bill)) 

milk = GroceryItem("Milk", 50, 40, 4.0)
tv = ElectronicItem("TV", 50000, 45000, 4.8)
order = Order("Prime Delivery", "123, Main Street") 
order.add_item_to_cart(milk, 2)
order.add_item_to_cart(tv, 1)
order.display_order_details()
order.display_total_bill()