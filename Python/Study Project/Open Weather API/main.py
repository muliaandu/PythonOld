import requests
import smtplib
from twilio.rest import Client

account_sid = 'ACe1cf83113b39d9ec55460d546e08d331112'
auth_token = '9f0b82e3bfd7f0a67d8e6bec650d3f3bbbbc'

is_rain = False
password = "JKLCX7FQFNL1S7G3UWCXRBNT"

GMAIL = "smtp.gmail.com"
HOTMAIL = "smtp.live.com"
YAHOO = "smtp.mail.yahoo.com"
port = 587

my_email = "robinrobinary@gmail.com"
appcode = "rssa rrkx llia djcf"
yuni_email = "ratriyuniantari@gmail.com"
testing_email = "robins.andu@gmail.com"

def weather_info():
    key = "b28479007998a140bd7730337a69130d"
    endpoint = "https://api.openweathermap.org/data/2.5/forecast"
    lat = -6.339330
    lon = 106.856581

    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": key,
        "cnt": 4,
    }

    response = requests.get(endpoint, params=weather_params)
    response.raise_for_status()
    print(response.status_code)
    data = response.json()
    print(data)
    # weather_id = data['list'][0]['weather'][0]['id']
    # print(weather_id)
    for hour_data in data["list"]:
        condition = hour_data['weather'][0]['id']
        print(condition)
        if int(condition) < 700:
            is_rain = True
    
    if is_rain:
        print("Bring an Umbrella !!!")
        with smtplib.SMTP(GMAIL, port) as connection:
            connection.starttls()
            connection.login(my_email, appcode)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=testing_email,
                msg=f"subject: Testing \n\nBring an Umbrella."
            )
        # client = Client(account_sid, auth_token)
        # message = client.messages.create(
        #                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        #                     from_='+12243534575',
        #                     to='+12243534575'
        
weather_info()