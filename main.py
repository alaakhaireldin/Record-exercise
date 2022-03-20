import requests
from datetime import datetime

gender = "female"
weight = 65
height = 163
age = 25
rows_endpoint = "https://api.sheety.co/eaae49380427409c92b0562611ad0565/copyOfMyWorkouts/workouts"
date_now = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

website_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
application_id = "4268e46e"
api_key = "2531a7ab9ac19e9751e3ed28f5c8379c"

exercise_text = input("what did you do today? ")

headers = {
    "x-app-id": application_id,
    "x-app-key": api_key,
}

parameters = {
    "query": exercise_text,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}

request_workout = requests.post(website_endpoint, headers=headers, json=parameters)
result = request_workout.json()
# print(result)
#
for exercise in result['exercises']:
    row_parameters = {
        "workout": {
            "date": str(date_now),
            "time": (str(time_now)),
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    # print(row_parameters)
    request = requests.post(rows_endpoint, json=row_parameters)
    print(request.text)
