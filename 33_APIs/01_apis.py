'''
An Application programming interface is a set of 
commands, functions, protocols, and objects that 
programmers can use to crete software or interact 
with an external system

API endpoint is a location where the apid data is stored.
usually just a url like api.coinbase.com

an API request can be a GET, POST, etc

reposnse codes:

1XX: Hold on
2XX: here ya go
3XX: go away
4XX: you screwed up
5XX: I screwed up
'''
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json",)
#200 - succeeds
print(response.status_code)

#checks for unsuccessful
response.raise_for_status()


longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
iss_postion = (longitude, latitude)
print(iss_postion)
