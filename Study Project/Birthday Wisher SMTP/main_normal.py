##################### Normal Starting Project ######################
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
today = (now.month, now.day)

data = pandas.read_csv("Study Project\\Birthday Wisher SMTP\\birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    letter = random.randint(1,3)
    file_path = f"Study Project\\Birthday Wisher SMTP\\letter_templates\\letter_{letter}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        contents = contents.replace("Angela", "Tamandu GANTENG")
    
    with smtplib.SMTP(GMAIL) as connection:
        connection.starttls()
        connection.login(user = my_email, password = appcode)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = yuni_email,
            msg = f"subject : HBD \n\n {contents}"
        )