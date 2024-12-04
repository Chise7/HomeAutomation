#This file will represent all of the API endpoints needed for the Laundry Project.

#TODO:
# 1. Basic Endpoint functionality
# 2. Edit laundry endpoint for error tracking
# 3. Laundry endpoint status sending

from fastapi import APIRouter
from classes import device
import core

router = APIRouter()


@router.post("/laundry") #Device will POST to /laundry with information about laundry status (started/ended)
def message( ping: device ):
    core.send_message(ping.message)
    core.update_status(device.id,device.status)
    return




