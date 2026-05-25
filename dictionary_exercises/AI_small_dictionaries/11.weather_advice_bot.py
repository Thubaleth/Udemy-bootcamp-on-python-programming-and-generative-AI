"""
Give weather advice.

weather = {
    "rain": "Take an umbrella",
    "sunny": "Wear sunglasses",
    "cold": "Wear a jacket"
}

Requirements:
- Ask user for weather condition
- Display matching advice
- Show default message if unknown
"""
weather = {
    "rain": "Take an umbrella",
    "sunny": "Wear sunglasses",
    "cold": "Wear a jacket",
    'cloudy':"Take an umbrella"
}

def weather_advice():
    weather_condition = input("Enter the weather condition: ")
    
    
    if weather_condition in weather:
            return weather[weather_condition]
    else:
           return "No advice available"

           
        
    
print(weather_advice())