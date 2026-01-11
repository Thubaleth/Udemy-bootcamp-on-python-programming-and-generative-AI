
"""Write a Python script that prompts the user for a circle's radius and calculates its area.

Formula: Area = π * r² (π = 3.1415)

Display the area with four decimal places using an f-string."""

radius = float(input("Enter the circles raduis : "))

area = 3.14 * (radius)**2 

print(f"The area is : {round(area,4)} ")
