#This file will represent all of the API endpoints needed for the Laundry Project.

#TODO:
# 1. Basic Endpoint functionality
# 2. Edit laundry endpoint for error tracking
# 3. Laundry endpoint status sending

from fastapi import APIRouter
from core import device
from core import utils

router = APIRouter()


@router.post("/") #Device will POST to /laundry with information about laundry status (started/ended)
def message( ping: device ):
    utils.send_message(ping.message)
    utils.update_status(device.id,device.status)
    return

@router.get("/status/all")
def get_status():
    return utils.read_status("all")

@router.get("/status/{device_id}")  #this will need checked
def get_id_status(device_id):
    return utils.read_status(device_id)
