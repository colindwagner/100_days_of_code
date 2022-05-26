from cmd import IDENTCHARS
import json
import requests
import datetime as dt


USERNAME = "colindwagner"
TOKEN = "fF&pL5SQpR&dwC"
ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# pixela_resp = requests.post(url=pixela_endpoint, json=user_params)
# print(pixela_resp.text)

pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": ID,
    "name": "my coding graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji"
}
graph_header = {
    "X-USER-TOKEN": TOKEN
}
# graph_resp = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=graph_header)
# print(graph_resp.text)


today = dt.datetime.today().strftime('%Y%m%d')
print(today)

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
pixel_params = {
    "date": today,
    "quantity": "9"
}

pixel_resp = requests.post(url=add_pixel_endpoint, json=pixel_params, headers=graph_header)
print(pixel_resp.text)