import requests
from datetime import datetime
import smtplib as smtp
import time

MY_LAT = 30.438255  # Your latitude
MY_LONG = -84.280731  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.

def within_iss(lat, long):
    return True if iss_latitude <= lat <= iss_latitude + 5 and iss_longitude - 5 <= long <= iss_longitude else False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour


# If the ISS is close to my current position
while True:
    time.sleep(60)
    if within_iss(MY_LAT, MY_LONG) and sunrise > hour > sunset:
        my_email = ''
        password = ''
        with smtp.SMTP('smtp.gmail.com') as gmail:
            gmail.starttls()
            gmail.login(user=my_email, password=password)
            gmail.sendmail(
                from_addr=my_email,
                to_addrs='',
                msg='Subject:ISS Above you\n\nLOOK UP!!!'
            )
# and it is dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.
