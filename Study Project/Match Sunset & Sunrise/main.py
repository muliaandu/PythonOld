import requests
import datetime

LATITUDE = -6.338780
LONGITUDE = 106.860950
FORMAT = 0

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": FORMAT
}

response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.datetime.now()
print(time_now)