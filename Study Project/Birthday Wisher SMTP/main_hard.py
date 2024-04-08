##################### Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas

GMAIL = "smtp.gmail.com"
HOTMAIL = "smtp.live.com"
YAHOO = "smtp.mail.yahoo.com"

my_email = "robinrobinary@gmail.com"
password = "TryingCode1234"
appcode = "rssa rrkx llia djcf"
yuni_email = "ratriyuniantari@gmail.com"
testing_email = "robins.andu@gmail.com"

now = dt.datetime.now()
month_day_now = (now.month, now.day)

birthdays = pandas.read_csv("Study Project\\Birthday Wisher SMTP\\birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()}

if month_day_now in birthday_dict:
    birthday_person = birthday_dict[month_day_now]
    file_path = f"Study Project\Birthday Wisher SMTP\letter_templates\letter_{random.randint(1,3)}.txt"
    with open(file_path) as data_birth:
        data = data_birth.read()
        data = data.replace("[NAME]", birthday_person["name"])
        data = data.replace("Angela", "Robin")

    with smtplib.SMTP(GMAIL) as connection:
        connection.starttls()
        connection.login(user = my_email, password = appcode)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = testing_email,
            msg = f"subject : HBD \n\n {data}"
        )