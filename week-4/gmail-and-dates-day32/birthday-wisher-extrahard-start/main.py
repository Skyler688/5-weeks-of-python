##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import pandas
import datetime as dt
import smtplib
import random

sender = "mycodetesting86@gmail.com"
app_pass = "sfvzedzctdduuikp"

birthdays = pandas.read_csv("birthdays.csv")
# print(birthdays["name"][0])
now = dt.datetime.now()
month = now.month
day = now.day

birth_months = birthdays["month"].to_list()
birth_day = birthdays["day"].to_list()

birthday_index = -1
for index, birth_month in enumerate(birth_months):
    if birth_month == month and birth_day[index] == day:
        birthday_index = index # if the a birthday is found set the index to be able to find the other values neaded latter.

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if birthday_index != -1:
    print("Birthday found sending birthday message...")
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as file: # grab a random message letter 
        message_template = file.read() # read it into a string

    name = birthdays["name"][birthday_index] # grab the name using the found birthday_index
    message = message_template.replace("[NAME]", name) # replace the name in the message string

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=app_pass)
        connection.sendmail(
            from_addr=sender,
            to_addrs=birthdays["email"][birthday_index],
            msg=f"Subject:Happy Birthday!\n\n{message}"
        )
else:
    print("No birthdays found")





