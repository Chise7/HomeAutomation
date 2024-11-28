#Communication with Microcontrollers and Individual Systems

# To Do: All for communication with devices (think, POV Devices)
# 1. Websocket for system statuses?
# 2. SEND TEXT MESSAGE FOR LAUNDRY
# 3. Send Temperature and Moisture data to database
# 4. Send Logs to Database
# 5. 

from fastapi import APIRouter

router = APIRouter()

@router.post("/status")
async def post_status():
    return{"message":"My status is: ----"}

# @router.post("/laundry")
# def send_message():
#     send text!