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

p = Product("Laptop", 30000, 25000, 4)  
p.display_product_details()

e = ElectronicItem("Smartphone", 20000, 15000, 4.5)
e.set_warranty(12) 
e.display_electronice_product_details()

g = GroceryItem("Rice", 1000, 800, 4.2)
g.set_expiry_date("19-02-2026")
g.grocery_product_details()