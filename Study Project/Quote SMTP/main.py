import smtplib
import datetime as dt
import random
import pandas

GMAIL = "smtp.gmail.com"
HOTMAIL = "smtp.live.com"
YAHOO = "smtp.mail.yahoo.com"
port = 587

my_email = "robinrobinary@gmail.com"
appcode = "rssa rrkx llia djcf"
yuni_email = "ratriyuniantari@gmail.com"
testing_email = "robins.andu@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 6:
    try:
        with open("Study Project\\Quote SMTP\\quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)
    except FileNotFoundError:
        print(f"\n\nFile quote.txt tidak tersedia.")
    else:
        print(f"\n\n{quote}")
        with smtplib.SMTP(GMAIL, port) as connection:
            connection.starttls()
            connection.login(user = my_email, password = appcode)
            connection.sendmail(
                from_addr = my_email,
                to_addrs = testing_email,
                msg = f"subject : TESTING \n\n hello ini testing \n\n{quote}"
            )