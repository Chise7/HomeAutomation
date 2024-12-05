#This file will represent all of the API endpoints for sensor data.

from fastapi import APIRouter
from core import device
from core import utils
router = APIRouter()



@router.post("/") #Devices log readings
def sensor_data(ping: device):
    utils.create_weather_entry("weather",ping.message)
    utils.update_status(ping.id, ping.status)
    return

@router.get("/readings") #Server gets readings
def get_sensor_data():
    return

@router.get("/status") #Server gets device Statuses
def get_device_status():
    return