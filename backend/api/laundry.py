#This file will represent all of the API endpoints needed for the Laundry Project.

#TODO:
# 1. Basic Endpoint functionality
# 2. Edit laundry endpoint for error tracking
# 3. Laundry endpoint status sending

from fastapi import APIRouter
from core import device
from core import utils

router = APIRouter()


@router.post("/") #Device will POST to /laundry to initiate text
def message( ping: device ):
    utils.send_message(ping.message)
    utils.update_status(device.id,device.status)
    return


