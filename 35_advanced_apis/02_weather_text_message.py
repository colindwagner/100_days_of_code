#apis can be secured through an api key
import requests
import os
from twilio.rest import Client 

weather_api_key = os.environ.get("OWM_API_KEY")
weather_api_end_point = f"https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": "40.712776",
    "lon": "-74.005974",
    "appid": weather_api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=weather_api_end_point, verify=False, params=parameters)
response.raise_for_status()
hourly_forecast = response.json()["hourly"]

text_string = ""

for hour in hourly_forecast[:12]:
    temp_f = round((hour["temp"] - 273.15) * 9/5 + 32)
    description = hour["weather"][0]["description"]
    text_string = text_string + f"At hour {hourly_forecast.index(hour) + 1}, the temp is going to be {temp_f},\nThe weather will be {description}\n"

print(text_string)


twilio_id = "SKd45b7bddbc9935a8139235a8ccdbefbb"
twilio_secret = os.environ.get("TWILIO_SECRET")


auth_token = os.environ.get("TWILIO_AUTH")
account_sid = 'ACc9604759e58a2cc4a1570d9fdd82724c' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGe3af3861ed8ef52782bfef44322f65f3', 
                              body=text_string,      
                              to='+18329935448' 
                          ) 
print(message.sid)