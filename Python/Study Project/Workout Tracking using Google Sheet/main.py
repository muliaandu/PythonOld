import requests
import datetime
import os

NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_APP_KEYS = os.environ["NUTRITIONIX_APP_KEYS"]
SHEETY_GET = os.environ["SHEETY_GET"]
SHEETY_POST = os.environ["SHEETY_POST"]
SHEETY_PUT = os.environ["SHEETY_PUT"]
SHEETY_DELETE = os.environ["SHEETY_DELETE"]
excersise_input = input(f"\nTell me which exercise you did: ")
today = datetime.datetime.now()

Nutritionix_Endpoint = os.environ["Nutritionix_Endpoint"]
Header = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEYS
}
body = {
    "query": excersise_input
}

response = requests.post(url=Nutritionix_Endpoint, headers=Header, json=body)
response.raise_for_status()
data = response.json()

date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")
exercise = data["exercises"][0]["name"].title()
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]
print(exercise)

header_sheety = {
    "Authorization": os.environ["sheety_Authorization"]
}

body_sheety = {
    "workout": {
    "date": date,
    "time": time,
    "exercise": exercise,
    "duration": duration,
    "calories": calories
    }
}

sheety_response = requests.post(url=SHEETY_POST, headers=header_sheety, json=body_sheety)
sheety_response.raise_for_status()
print(sheety_response.text)