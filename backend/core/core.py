#common functionalities

from settings.private import private
from email.message import EmailMessage
import datetime
import smtplib


def update_status(id,status):
    print("This will eventually send status updates to the DB.")
    return

def send_message(message):
    message = EmailMessage()
    message["From"] = private.sender
    message["To"] = private.reciever
    message["Subject"] = " "
    now = datetime.datetime.now().strftime("%H:%M:%S")
    msg = f"Laundry Has {message} At Time = {now}."
    message.set_content(msg)
    with smtplib.SMTP(private.host) as smtp:
        smtp.login(private.sender,private.sender_password)
        smtp.sendmail(private.sender,private.reciever,msg.as_string())
        #verification?
    return

