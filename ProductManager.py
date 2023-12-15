class ProductManager:
    def __init__(self):
        self.products = []
        self.load_data()

    def load_data(self):
        data = DataStorage.get_data()
        for row in data:
            code, name, category, quantity, cost_price = row
            product = Product(int(code), name, category, int(quantity), float(cost_price))
            self.products.append(product)

    def total_revenue(self):
        total = sum(product.net_price() for product in self.products)
        return total

    def add_product(self, product):
        self.products.append(product)