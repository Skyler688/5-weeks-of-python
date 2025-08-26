import requests
from datetime import datetime, timezone
from time import sleep
import smtplib

MY_LAT = 40.534271 # Your latitude
MY_LONG = -112.298447 # Your longitude

BOT_EMAIL = "my bot email"
APP_PASS = "gmail app pass"

MY_EMAIL = "my target email"

def send_email():
    print("Sending email...")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=BOT_EMAIL, password=APP_PASS)
        connection.sendmail(
            from_addr=BOT_EMAIL,
            to_addrs= MY_EMAIL,
            msg="Subject:ISS Status\n\nThe iss is overhead, go look outside."
        )


while True:

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = 40
    iss_longitude = -112
    print(f"My Latitude: {MY_LAT} - ISS: {iss_latitude}")
    print(f"My Longitude: {MY_LONG} - ISS: {iss_longitude}")

    #If the ISS is close to my current position
    #Your position is within +5 or -5 degrees of the ISS position.
    if (iss_latitude <= MY_LAT + 5 and iss_latitude >= MY_LAT - 5) and (iss_longitude <= MY_LONG + 5 and iss_longitude >= MY_LONG - 5):
        print("ISS in position")

        parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()

        sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunrise_min = int(data["results"]["sunrise"].split("T")[1].split(":")[1])
        sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        sunset_min = int(data["results"]["sunset"].split("T")[1].split(":")[1])

        print(f'Sunrise-> {sunrise_hour}:{sunrise_min}, Sunset-> {sunset_hour}:{sunset_min}')

        # Creating a night time array
        # NOTE -> using an array to hold the night time hours becaus i am using UTC time and normal hours do not corilate.
        night = []
        for index in range(24):
            if sunset_hour + index > 23:
                night_hour = sunset_hour + index - 24
            else:
                night_hour = sunset_hour + index

            if night_hour == sunrise_hour:
                night.append(night_hour) # append one last time to add the finall hour to the list
                break
            else:
                night.append(night_hour)

        print(f"Night time hours -> {night}")    
        # grab the utc time to match the api
        time_now = datetime.now(timezone.utc)
        current_hour = time_now.hour
        current_min = time_now.minute
        
        print(f"Current time -> {current_hour}:{current_min}")

        # If it is currently dark
        # Then send me an email to tell me to look up.
        if current_hour in night:
            if current_hour == night[0]: 
                if current_min > sunset_min:
                    send_email()
                else:
                    print("Currently day (before sunset)")    
            elif current_hour == night[-1]: 
                if current_min < sunrise_min:
                    send_email() 
                else:
                    print("Currently day (after sunrise)")   
            else:
                send_email()  
        else:
            print("Currently day")

    else:
        print("ISS not in position")    

    # BONUS: run the code every 60 seconds.
    sleep(60)
