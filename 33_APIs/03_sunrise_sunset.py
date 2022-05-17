from time import time
import requests
import datetime as dt

my_lat = 40.608181
my_long = -75.584347
api_endpoint = 'https://api.sunrise-sunset.org/json'

parameters = {
    "lat": my_lat,
    "lng": my_long,
    "formatted": 0
}
response = requests.get(url=api_endpoint,params=parameters)
sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]


time_now  = dt.datetime.now()
print(time_now.hour)
