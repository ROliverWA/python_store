
class Products:
    def __init__(self, name, price, category, unique_id):
        self.name = name
        self.price = price
        self.category = category
        self.unique_id = unique_id
    def update_price(self, percent_change, is_increased):
        change_amount = (percent_change)/100 
        if(is_increased):            
            price += change_amount
        elif not (is_increased):
            price -= change_amount
    def print_into(self):
        print(self.name, self.category, self.price)