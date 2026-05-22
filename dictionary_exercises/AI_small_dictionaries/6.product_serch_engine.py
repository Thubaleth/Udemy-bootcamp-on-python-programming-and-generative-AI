"""Create a product search system.

products = {
    "Laptop": {"category": "Electronics", "price": 1200},
    "Phone": {"category": "Electronics", "price": 800},
    "Chair": {"category": "Furniture", "price": 150}
}

Requirements:
- Search by category
- Search by price range
- Display matching products
"""
products = {
    "Laptop": {"category": "Electronics", "price": 1200},
    "Phone": {"category": "Electronics", "price": 800},
    "Chair": {"category": "Furniture", "price": 150}
}


def search_by_category():
    category = input("Enter your category: ")

    found = False

    for product, details in products.items():
        if details["category"] == category:
            print(product, details)
            found = True

    if not found:
        print("Category not found")




def search_by_price_range():
    price = input("Enter your price:")

    found = False
    for product,details in products.items():
        if details["price"] == int(price):
         print(product,details)
         found = True
    
    if not found:
        print("category not found")

def display_matching_products():

    matching_products = {}

    category = input("Enter the category: ").lower()

    for product, details in products.items():

        if details["category"].lower() == category:
            matching_products[product] = details

    return matching_products

print(display_matching_products())


   
