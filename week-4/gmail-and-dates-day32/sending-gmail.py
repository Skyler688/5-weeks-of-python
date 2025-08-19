import smtplib

my_gmail = "gmail-address"
password = "put-password-hear"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_gmail, password=password)
    connection.sendmail(
        from_addr=my_gmail,
        to_addrs="target-address",
        msg="Subject:Hello From Code\n\nHello i am robot"
    )

    