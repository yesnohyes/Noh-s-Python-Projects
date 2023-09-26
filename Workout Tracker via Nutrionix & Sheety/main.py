import requests
from datetime import datetime

APP_ID = "a0f5c40a"
APP_KEY = "bdbe6d7299e363287138514bb7729901"

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}

exercise_input = input("Tell me which exercises you did?: ")

user_params = {
    "query": exercise_input
}

response = requests.post(url=nutrition_endpoint, json=user_params, headers=headers)
exercise_list = response.json()["exercises"]

today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%H:%M:%S")


for exercise in exercise_list:
    exercise_name = exercise["name"].title()
    exercise_duration = exercise["duration_min"]
    exercise_calories = exercise["nf_calories"]

    sheety_parameters = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories
        }
    }

    sheety_auth = (
        "yesnohyes",
        "qwerty123"
    )

    sheety_endpoint = "https://api.sheety.co/c6725b97dcd4e9e9c4de390105100666/myWorkoutTracker (python)/workouts"

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_parameters, auth=sheety_auth)
    print(sheety_response.text)