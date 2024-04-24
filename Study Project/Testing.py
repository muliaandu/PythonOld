import smtplib

GMAIL = "smtp.gmail.com"
HOTMAIL = "smtp.live.com"
YAHOO = "smtp.mail.yahoo.com"

my_email = "robinrobinary@gmail.com"
# appcode = "rssa rrkx llia djcf"
appcode = "bfqc mrzo vmid vdbk"
yuni_email = "ratriyuniantari@gmail.com"
testing_email = "robins.andu@gmail.com"

with smtplib.SMTP(GMAIL, 587) as connection:
    connection.starttls()
    connection.login(user = my_email, password = appcode)
    connection.sendmail(
        from_addr = my_email,
        to_addrs = testing_email,
        msg = f"subject : TESTING \n\n hello ini testing \n\nTEEESSSTTTTTT WOE"
    )