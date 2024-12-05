#Endpoint for error logging of all devices

from fastapi import APIRouter
from backend.core import utils
from core import device
router = APIRouter()

@router.post("/")
def error_log(ping: device):
    utils.create_error_log(ping.id,ping.message)
    return

@router.get("/")
def get_logs():
    return