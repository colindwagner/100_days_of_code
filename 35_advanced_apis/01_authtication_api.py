#apis can be secured through an api key
import requests

api_key = "cb29450add7c81d47caea6cd998f724e"
api_end_point = f"https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": "40.712776",
    "lon": "-74.005974",
    "appid": api_key,
    "exclude": "current,minutely,hourly,alerts"
}

response = requests.get(url=api_end_point, verify=False, params=parameters)
print(response.json())