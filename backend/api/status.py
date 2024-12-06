#dedicated endpoint for device statuses

from fastapi import APIRouter
from core import device
from core import utils
router = APIRouter()

@router.post("/") #Server gets device Statuses
def get_device_status():
    utils.update_status(device.id,device.status)
    return

@router.get("/all")
def get_status():
    return utils.read_status("all")

@router.get("/{device_id}")  #this will need checked
def get_id_status(device_id):
    return utils.read_status(device_id)