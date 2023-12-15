from Product import Product
from ProductManager import ProductManager

class Application:          # Application class 

    def __init__(self, product_manager):    #Olumide Olatoye 991710777
        self.product_manager = product_manager


    def show_main_menu(self):   #Show Main Menu
        while True:
            print("\nMain Menu:")
            print("1. Display all products")
            print("2. Display product by type (Phone/Computer)")
            print("3. Display total revenue")
            print("4. Add new Product")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_all_products()
            elif choice == '2':
                self.display_products_by_type()
            elif choice == '3':
                self.display_total_revenue()
            elif choice == '4':
                self.add_new_product()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def display_all_products(self):             #display all products
        for product in manager.products:
            print(product)

    def display_products_by_type(self):         #Display products by type
        category = input("Enter product type (Phone/Computer): ")
        filtered_products = [product for product in manager.products if product.category.lower() == category.lower()]
        for product in filtered_products:
            print(product)

    def display_total_revenue(self):     #Display total revenue 
        revenue = manager.total_revenue()
        print(f"Total Revenue: {revenue}")

    def add_new_product(self):            #Add a new product
        code = input("Enter product code: ")
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        quantity = input("Enter product quantity: ")
        cost_price = input("Enter product cost price: ")

        new_product = Product(int(code), name, category, int(quantity), float(cost_price))
        manager.add_product(new_product)
        print("Product added successfully.")

# Main part of the program
if __name__ == "__main__":
    manager = ProductManager()
    app = Application(manager)
    app.run()
