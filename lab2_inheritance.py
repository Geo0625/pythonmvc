class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
        
    def display_details(self):
        print(f"=== Product Details ===\nProduct ID: {self.product_id}\nName: {self.name}\nPrice: {self.price}")
        
class Electronics(Product):
    def __init__(self, product_id, name, price, warranty_months):
        super().__init__(product_id, name, price)
        self.warranty_months = warranty_months
        
    def display_details(self):
        super().display_details()
        print(f"Warranty Month: {self.warranty_months}")
        print()
        
class SmartClothing(Product):
    def __init__(self, product_id, name, price, fabric_type):
        super().__init__(product_id, name, price)
        self.fabric_type = fabric_type
    
    def display_details(self):
        super().display_details()
        print(f"Fabric Type: {self.fabric_type}")
        print()
        
p1 = Electronics("001", "Phone", 10000, "3 months")
p1.display_details()

p2 = SmartClothing("002", "Uniqlo", 1500, "Cotton")
p2.display_details()
