#Communication with Microcontrollers and Individual Systems

# To Do: All for communication with devices (think, POV Devices)
# 1. Websocket for system statuses?
# 2. SEND TEXT MESSAGE FOR LAUNDRY
# 3. Send Temperature and Moisture data to database
# 4. Send Logs to Database
# 5. 

from fastapi import APIRouter
from core.private import private
from email.message import EmailMessage
import datetime
import smtplib
from pydantic import BaseModel

router = APIRouter()

class device(BaseModel):
    id: str
    message: str
    status: str

class Pi(device):
    sensor_readings: dict


@router.post("/status")
async def post_status():
    return{"message":"My status is: ----"}

@router.post("/laundry") #Device will POST to /laundry with information about laundry status (started/ended)
def message( ping: device ):
    message = EmailMessage()
    message["From"] = private.sender
    message["To"] = private.reciever
    message["Subject"] = " "
    now = datetime.datetime.now().strftime("%H:%M:%S")
    msg = f"Laundry Has {ping.message} At Time = {now}. Device Status: {ping.status}."
    message.set_content(msg)
    with smtplib.SMTP(private.host) as smtp:
        smtp.login(private.sender,private.sender_password)
        smtp.sendmail(private.sender,private.reciever,msg.as_string())
        #verification?
    return

@router.post("/outside_sensor")
def sensor_readings(ping: Pi):
    print(" ")
    return