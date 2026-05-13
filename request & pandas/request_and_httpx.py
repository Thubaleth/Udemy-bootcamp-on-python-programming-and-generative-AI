import requests 
import httpx

url = "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m"

response = requests.get(url)
print(response.status_code)
print(response.headers)
print(response.text)
data = response.json()
print(data) #converts the JSON text into a Python dictionary
print(data["hourly"]["temperature_2m"])

r = httpx.get(url)
print(r.status_code)
print(r.json())