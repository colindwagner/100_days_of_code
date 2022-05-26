
import requests
import datetime as dt


USERNAME = "colindwagner"
TOKEN = "fF&pL5SQpR&dwC"
ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
graph_header = {
    "X-USER-TOKEN": TOKEN
}

today = dt.datetime.today().strftime('%Y%m%d')
add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today}"
pixel_resp = requests.delete(url=add_pixel_endpoint, headers=graph_header)
print(pixel_resp.text)