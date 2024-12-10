#common functionalities

from fastapi import Depends
from typing import List, Annotated
from settings.private import private
from email.message import EmailMessage
import datetime #Pendulum eventually
import smtplib
from database import models
from database import database as _db
from sqlalchemy.orm import Session
from classes import device, laundry_device, sensor, err_log


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


#CREATE    
def create_weather_entry(data: sensor, session: Session):
    entry = models.Weather(
        timestamp=get_time(),
        temperature=data.temperature,
        moisture = data.moisture,
        cpu_temp=data.cpu_temp,
    )
    session.add(entry)
    session.commit()
    # Session.refresh()
    return

def create_error_log(log: err_log, session: Session):
    entry = models.ErrorLog(
        timestamp =get_time(),
        device_id = err_log.device_id,
        message= err_log.message,
    )
    session.add(entry)
    session.commit()
    return

#READ
def read_status(id):
    if id == "all":
        return() #all statuses
    return()#status of one id

def read_weather():
    return

def read_logs():
    return

#UPDATE
def update_weather_db(data):
    return

def update_status(device_id, device_status, session: Session): #updating db vs creating entry ***
    entry = models.Status(
        device_id = device_id,
        status = device_status,
        timestamp= get_time(),
    )
    # session.
    return

#DELETE
def delete_log(log_id):
    return