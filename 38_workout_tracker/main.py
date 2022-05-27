import requests
import datetime as dt

APP_ID = "34ff5e85"
API_KEY = "b40466b3f7eaee2081c7b2861be3d135"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


query = input("Tell me what exercises you did: ")

body = {
 "query": query,
 "gender":"male",
 "weight_kg":78,
 "height_cm":180.34,
 "age":31
}

exercise_resp = requests.post(url=exercise_endpoint, json=body, headers=HEADERS)

exercises_data = exercise_resp.json()["exercises"]

today = dt.datetime.now().strftime("%d/%m/%Y")
current_time = dt.datetime.now().strftime("%X")

sheet_endpoint = "https://api.sheety.co/1f4c9ffa2aa5ad343c8c27d52f0aeec7/workouts/sheet1"


for exercise in exercises_data:
    sheet_body = {
        "sheet1": {
            "date": today,
            "time": current_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_resp = requests.post(url=sheet_endpoint, json=sheet_body, verify=False)
    print(sheet_resp.text)