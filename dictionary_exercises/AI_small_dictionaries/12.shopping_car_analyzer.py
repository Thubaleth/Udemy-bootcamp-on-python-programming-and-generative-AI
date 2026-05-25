"""
Analyze shopping cart prices.

cart = {
    "Laptop": 1200,
    "Phone": 800,
    "Mouse": 50
}

Requirements:
- Calculate total price
- Find most expensive item
- Apply discount if total > 1000
"""

cart = {
    "Laptop": 1200,
    "Phone": 800,
    "Mouse": 50
}
total = 0
max = 0
discount = 0
expensive_device = ""
for device,price in cart.items():

   total += price
   if price > max:
      max = price
      expensive_data = device
      
    
   if price > 1000:
      discount = price - (price * 0.15)
      print(f"here is the price for {device} with discpunt: {discount}")
      
print(f"{expensive_data} is the most device")

      
