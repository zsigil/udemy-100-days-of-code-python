import requests
from datetime import datetime

from secret import apikey


my_api_key = apikey.API_KEY

# Gödöllő geoposition
lat = '47.597530'
long = '19.348030'

# current_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={my_api_key}"
# forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&appid={my_api_key}"

url = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": lat,
    "lon": long,
    "appid": my_api_key,
    "cnt": 6
}

res = requests.get(url, params)
res.raise_for_status()

weather_data = res.json()
print(weather_data)

# send sms via Twilio API


def send_sms():
    # https://www.twilio.com/en-us/ahoy
    pass


#  if weather condition code is less than 700, bring an umbrella
weather_id_list = []

for item in weather_data["list"]:
    print(datetime.fromtimestamp(item["dt"]))
    for item2 in item["weather"]:
        weather_id_list.append(item2["id"])

if min(weather_id_list) < 700:
    print(weather_id_list)
    print("Umbrella needed for today")
    send_sms()
