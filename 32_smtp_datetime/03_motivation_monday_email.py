
import datetime as dt
import smtplib
import random
now = dt.datetime.now()
day_of_week = now.weekday()


if day_of_week == 0:
    with open("quotes.txt", "r") as file:
        mail_content = file.readlines()
        content = random.choice(mail_content)

#The mail addresses and password
sender_address = 'colin.d.wagner@gmail.com'
sender_pass = '***'
receiver_address = 'colin.d.wagner@hotmail.com'
message = 'Subject: {}\n\n{}'.format("Quote of the day", content)

with smtplib.SMTP('smtp.gmail.com', 587) as session:
    session.starttls()
    session.login(sender_address, sender_pass) 
    session.sendmail(sender_address, receiver_address, f"Subject:Quote of the day\n\n {content}")
    session.quit()
    print('Mail Sent')