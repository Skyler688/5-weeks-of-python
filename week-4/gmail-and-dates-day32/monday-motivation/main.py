# CHALANGE -> Check if it is monday and send a motivational quote to your email.

import smtplib
import datetime as dt
import random
from email.message import EmailMessage # had to use a alternate method to the lesson, was getting errors sending the raw string.

sender = "placholder@gmail.com"
app_pass = "app_password"
receiver = "placholder86@yahoo.com"

# Read the quotes file into a list
with open("quotes.txt", "r") as file:
    quotes = file.readlines()

# Check the day of the week
day_of_week = dt.datetime.now().weekday() # 0 is monday
if day_of_week == 0:
    quote = random.choice(quotes) # pick random quote
    msg = EmailMessage()
    msg['Subject'] = "Monday Modivation"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=app_pass)
        connection.send_message(msg) # used send_message instead of sendmail, was getting an error because of invalid ASCII