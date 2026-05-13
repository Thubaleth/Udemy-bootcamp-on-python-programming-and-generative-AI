import requests
import json
try:
    url = "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m"
    response = requests.get(url,timeout = 5)# request will wait for 5 seconds before timing out. this is useful for avoiding long waits if the server is slow and unresponsive
    data = response.raise_for_status()# cheecks the https status
    print(json.dumps(response.json(), indent =4))#make it more readable
except requests.exceptions.RequestException as e:#where are checking a broad range of possible errors
       
     print(f"an error has occured: {e}")#e is the neme of the error
