
import smtplib

mail_content = "Hello, This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.Thank You"

#The mail addresses and password
sender_address = 'colin.d.wagner@gmail.com'
sender_pass = '***'
receiver_address = 'colin.d.wagner@hotmail.com'

with smtplib.SMTP('smtp.gmail.com', 587) as session:
    session.starttls()
    session.login(sender_address, sender_pass) 
    session.sendmail(sender_address, receiver_address, mail_content)
    session.quit()
    print('Mail Sent')
