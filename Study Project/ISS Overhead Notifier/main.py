import requests
import datetime
import smtplib
import time

LATITUDE = -6.338780
LONGITUDE = 106.860950
FORMAT = 0

GMAIL = "smtp.gmail.com"
HOTMAIL = "smtp.live.com"
YAHOO = "smtp.mail.yahoo.com"

my_email = "robinrobinary@gmail.com"
password = "TryingCode1234"
appcode = "rssa rrkx llia djcf"
yuni_email = "ratriyuniantari@gmail.com"
testing_email = "robins.andu@gmail.com"



def is_iss_overhead():
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if LATITUDE-5 < iss_latitude < LATITUDE+5 and LONGITUDE-5 < iss_longitude < LONGITUDE+5:
        print("LOOK UP")
        return True


def is_night():    
    parameters = {
        "lat":LATITUDE,
        "lng":LONGITUDE,
        "formatted":FORMAT
    }
    time_now = datetime.datetime.now().hour
    response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    if time_now > sunset or time_now < sunrise:
        return True

while True:
    time.sleep(60)    
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP(GMAIL)
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
        from_addr = my_email,
        to_addrs = testing_email,
            msg = "Subject: Look UP. \n\nThe ISS is above you in the way."
        )
       