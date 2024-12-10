#This file will represent all of the API endpoints needed for the Laundry Project.

#TODO:
# 1. Basic Endpoint functionality
# 2. Edit laundry endpoint for error tracking
# 3. Laundry endpoint status sending

from fastapi import APIRouter
from backend.core.classes import laundry_device
from core import utils

router = APIRouter()

@router.post("/") #Device will POST to /laundry to initiate text
def message( ping: laundry_device ):
    utils.send_message(ping.message)
    utils.update_status(ping.device_id, ping.status)
    return


