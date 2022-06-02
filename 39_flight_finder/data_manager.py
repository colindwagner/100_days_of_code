from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/1f4c9ffa2aa5ad343c8c27d52f0aeec7/flightTracker/sheet1"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, verify=False)
        data = response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data, verify=False
            )
            print(response.text)
