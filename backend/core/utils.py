#common functionalities

from settings.private import private
from email.message import EmailMessage
import datetime #Pendulum eventually
import smtplib

def get_time():
    return(datetime.datetime.now().strftime("%H:%M:%S"))

def send_message(message):
    message = EmailMessage()
    message["From"] = private.sender
    message["To"] = private.reciever
    message["Subject"] = " "
    now = get_time()
    msg = f"Time: {now}. Message: {message}"
    message.set_content(msg)
    with smtplib.SMTP(private.host) as smtp:
        smtp.login(private.sender,private.sender_password)
        smtp.sendmail(private.sender,private.reciever,msg.as_string())
        #verification?
    return

def create_weather_entry(data):
    get_time()
    return

def create_error_log(id,log):
    get_time()
    return

def read_status(id):
    if id == "all":
        return() #all statuses
    return()#status of one id

def read_weather():
    return

def read_logs():
    return

def update_weather_db(data):
    return

def update_status(id, status):
    return

def delete_log(log_id):
    return