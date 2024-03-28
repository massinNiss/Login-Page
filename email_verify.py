import os
from email.message import EmailMessage
import ssl
import smtplib
import random
import time

def email_verification(email, verify_as_list):

    num = random.randrange(1, 10**3)
    verify = str(num).zfill(3)
    verify_as_list.append(verify)

    email_sender = 'niharminemassine@gmail.com'
    email_password = os.environ.get("EMAIL_CODE")
    email_receiver = email

    subject = 'verification'
    body = f'your verification code is {verify}. please insert this code.'


    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context= context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())


    time.sleep(120)

    verify_as_list.remove(verify)
    num = random.randrange(1, 10 ** 3)
    verify = str(num).zfill(3)
    verify_as_list.append(verify)
