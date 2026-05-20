"""Create a shopping cart system:

cart = {}

Requirements:
- Function to add items to cart
- Function to remove items
- Function to update item quantity
- Function to calculate total items in cart
- Use a loop-based menu for user interaction
"""

#- Function to add items to cart
cart = {}
def add_item():
    item = input("Enter the item: ")
    num_of_items = int(input("Enter the number of items: "))
   
    if item in cart:
        cart[item] += num_of_items
    else:
        cart[item] = num_of_items
    print("item added successfully")




# Function to remove items
def remove_item():
    item = input("Enter item to b deleted")
    if item in cart:
     del cart[item]
     print(f'{item} deleted successfully')
    else:
       print(f'{item} not found')

#Function to update item quantity
def update_item():
   item = input("Enter item to update : ")

   if item in cart:
      num_of_items = input("update the item qautity")
      cart[item] = num_of_items
      print(f'{item} updated')
   else:
      print("item not found")

    
#Function to calculate total items in cart

def total_items():
   total = sum(cart.values())
   print(f"total item in cart {total}")

def view_cart():
    if not cart:
        print("Cart is empty!")
    else:
        print("\nCart Items:")
        for item, qty in cart.items():
            print(f"{item}: {qty}")
   
#  Menu system
def menu():
    while True:
        choice = int(input(
            "\n1. Add item\n"
            "2. Remove item\n"
            "3. Update item\n"
            "4. View cart\n"
            "5. Total items\n"
            "6. Exit\n"
            "Enter choice: "
        ))

        if choice == 1:
            add_item()

        elif choice == 2:
            remove_item()

        elif choice == 3:
            update_item()

        elif choice == 4:
            view_cart()

        elif choice == 5:
            total_items()

        elif choice == 6:
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")


menu()