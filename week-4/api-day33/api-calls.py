import requests
from datetime import datetime

LAT = 40.534271
LNG = -112.298447

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# test = (longitude, latitude)
# print(test)

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# creates a list using the split() method
sunrise = data["results"]["sunrise"].split("T")
# Can also refine the results, for example this grabs the hour
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print("Sunrise", sunrise)
print("Sunset", sunset)

time_now = datetime.now()