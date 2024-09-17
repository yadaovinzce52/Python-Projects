import requests
import datetime as dt
import os

GENDER = 'Male'
WEIGHT_KG = 88.4505
HEIGHT_CM = 167.64
AGE = 26

APP_ID = os.environ['WT_APP_ID']
API_KEY = os.environ['WT_API_KEY']

parse_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = os.environ['WT_SHEETY']

nutritionix_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

params = {
    'query': input('Tell me which exercises you did: '),
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(parse_endpoint, json=params, headers=nutritionix_headers)
result = response.json()

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

sheety_headers = {
    'Authorization': os.environ['WT_AUTHORIZATION']
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_headers)

    print(sheet_response.text)
