#Arham Mehdi
#100889136
#Assignment 1

import timeit

# Class to represent a product
class Product:
    def __init__(self, product_id, name, price, category):
        self.id = product_id
        self.name = name
        self.price = price
        self.category = category

# Class to manage product data
class ProductManager:
    def __init__(self):
        self.products = []

    def load_data(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                product = Product(int(data[0]), data[1], float(data[2]), data[3])
                self.products.append(product)

    def insert_product(self, product):
        start_time = timeit.default_timer()
        self.products.append(product)
        end_time = timeit.default_timer()
        print(f"Time taken to insert: {end_time - start_time} seconds")

    def update_product(self, product_id, new_price):
        start_time = timeit.default_timer()
        for product in self.products:
            if product.id == product_id:
                product.price = new_price
                break
        end_time = timeit.default_timer()
        print(f"Time taken to update: {end_time - start_time} seconds")

    def delete_product(self, product_id):
        start_time = timeit.default_timer()
        self.products = [product for product in self.products if product.id != product_id]
        end_time = timeit.default_timer()
        print(f"Time taken to delete: {end_time - start_time} seconds")

    def search_product_by_id(self, product_id):
        start_time = timeit.default_timer()
        for product in self.products:
            if product.id == product_id:
                end_time = timeit.default_timer()
                print(f"Time taken to search: {end_time - start_time} seconds")
                return product
        end_time = timeit.default_timer()
        print(f"Time taken to search: {end_time - start_time} seconds")
        return None

    def search_product_by_name(self, product_name):
        start_time = timeit.default_timer()
        for product in self.products:
            if product.name == product_name:
                end_time = timeit.default_timer()
                print(f"Time taken to search: {end_time - start_time} seconds")
                return product
        end_time = timeit.default_timer()
        print(f"Time taken to search: {end_time - start_time} seconds")
        return None

    def sort_products_by_price(self, algorithm='bubble'):
        if algorithm == 'bubble':
            self.bubble_sort()
        elif algorithm == 'insertion':
            self.insertion_sort()
        elif algorithm == 'quick':
            self.quick_sort()

    def bubble_sort(self):
        start_time = timeit.default_timer()
        n = len(self.products)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.products[j].price > self.products[j+1].price:
                    self.products[j], self.products[j+1] = self.products[j+1], self.products[j]
        end_time = timeit.default_timer()
        print(f"Time taken to sort: {end_time - start_time} seconds")

# Sample usage
if __name__ == "__main__":
    # Task 1: Data Management
    product_manager = ProductManager()
    product_manager.load_data(r"C:\Users\17803\Downloads\product_data (1).txt")

    while True:
        print("\nOptions:")
        print("1. Insert")
        print("2. Update")
        print("3. Delete")
        print("4. Search")
        print("5. Sorting Algorithm Implementation")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Insert a new product
            product_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            category = input("Enter product category: ")
            new_product = Product(product_id, name, price, category)
            product_manager.insert_product(new_product)

        elif choice == 2:
            # Update an existing product
            product_id = int(input("Enter product ID: "))
            new_price = float(input("Enter new product price: "))
            product_manager.update_product(product_id, new_price)

        elif choice == 3:
            # Delete a product
            product_id = int(input("Enter product ID: "))
            product_manager.delete_product(product_id)

        elif choice == 4:
            # Search for a product
            search_option = int(input("1. Search by ID, 2. Search by Name: "))
            if search_option == 1:
                product_id = int(input("Enter product ID: "))
                searched_product = product_manager.search_product_by_id(product_id)
            elif search_option == 2:
                product_name = input("Enter product name: ")
                searched_product = product_manager.search_product_by_name(product_name)

            if searched_product:
                print(f"Product Found: {searched_product.name}, Price: {searched_product.price}")
            else:
                print("Product not found.")

        elif choice == 5:
            # Sorting Algorithm Implementation
            print("\nSorting by Price (Bubble Sort):")
            product_manager.sort_products_by_price('bubble')

        elif choice == 6:
            # Exit
            break

        else:
            print("Invalid choice. Please try again.")
