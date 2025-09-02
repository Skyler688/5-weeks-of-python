import requests
import json
import datetime as dt
# Using .env instead of enviroment variabes
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

arg = input("Enter exersize:")

nutritionix = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

body = {
    "query": arg
}

responce = requests.post(url=nutritionix, headers=header, data=json.dumps(body))
responce.raise_for_status()

print(json.dumps(responce.json(), indent=4))
now = dt.datetime.now()
data = responce.json()

sheety = "https://api.sheety.co/6918d56be4db6f51302f60c82281eb78/workoutTracker/sheet1"

header = {
    "Content-Type": "application/json",
    "Authorization": os.getenv("SHEETY_AUTH")
}

for exercise in data["exercises"]:

    body = {
        "sheet1": {
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M:%S"),
            "duration": exercise["duration_min"],
            "exercise": exercise["name"],
            "calories": exercise["nf_calories"]
        }
    }

    responce = requests.post(url=sheety, headers=header, data=json.dumps(body))
    responce.raise_for_status()

    print(responce)