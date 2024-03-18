"""
Question: Write a program that reads a CSV file containing information about
products and stores it in a dictionary. Provide functions to search for products
based on various criteria.

"""
import csv
import os

def read_products_from_csv(filename):
    products = {}
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            product_id = row['ProductID']
            products[product_id] = row
    return products

def search_product_by_id(products, product_id):
    return products.get(product_id)

def search_products_by_category(products, category):
    return [product for product in products.values() if product['Category'] == category]

def search_products_by_price_range(products, min_price, max_price):
    return [product for product in products.values() if min_price <= float(product['Price']) <= max_price]

# Get the absolute path of the CSV file
current_directory = os.path.dirname(__file__)
csv_file_path = os.path.join(current_directory, 'products.csv')

# Example usage:
products = read_products_from_csv(csv_file_path)
print("Product with ID 102:", search_product_by_id(products, '102'))
print("All products in the 'Accessory' category:", search_products_by_category(products, 'Accessory'))
print("Products between $200 and $500:", search_products_by_price_range(products, 200, 500))
