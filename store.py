import products

class Store:
    def __init__(self, name='Our Store'):
        self.name = name    
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
    def sell_product(self, category, unique_id):
        for x in range(len(self.products)):
            if (unique_id == self.products[x].unique_id):
                sold_product = self.products.pop(category)                
                print(sold_product);
            else:
                print("No Items Found Matching ID")
    def inflation(self, percent_increase):
        for x in range(len(self.products)):
            self.products[x] = Products.update_price(percent_increase, True)
    def set_clearance(self, category, percent_discount):
        for x in range(len(self.products)):
            if(Products.category == category):
                Products.update_price(percent_discount, False)
    def list_products(self):
        for x in range(len(self.products)):
            print(self.products[x].name)
            
        
        






