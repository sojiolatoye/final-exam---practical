

class Product:    #Product class
    def __init__(self, code, name, category, quantity, cost_price):
        self.code = code
        self.name = name
        self.category = category
        self.quantity = quantity
        self.cost_price = cost_price

    def get_code(self):
        return self.code

    def set_category(self, new_category):
        if not new_category.isalpha() or not new_category.strip():
            raise ValueError("Category must contain only alphabets and cannot be blank.")
        self.category = new_category

    def net_price(self):
        taxable_amount = self.quantity * self.cost_price
        tax = taxable_amount * 0.135  # 13.5% tax
        return taxable_amount + tax

    def __str__(self):
        return f"Code: {self.code}, Name: {self.name}, Category: {self.category}, Net Price: {self.net_price()}"




