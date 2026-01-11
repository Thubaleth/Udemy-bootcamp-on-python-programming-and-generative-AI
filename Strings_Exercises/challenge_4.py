"""Write a Python script to convert feet (ft) to centimeters (cm).

Conversion: 1 ft = 30.48 cm

Prompt the user to enter a value in feet.

Display the result in centimeters with two decimal places, formatted using an f-string."""

feet_value = float(input("Enter the value in feet: "))

converted = feet_value * 30.48

print(f'the converted feet value is {round(converted,2)}')
