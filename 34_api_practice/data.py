import requests

parameters = {
    "amount": 40,
    "type": "boolean"
}
response = requests.get(url='https://opentdb.com/api.php', params=parameters, verify=False)
question_data = response.json()["results"]