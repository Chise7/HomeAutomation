#This file will represent all of the API endpoints for sensor data.

from fastapi import APIRouter
from core import device
from core import utils
router = APIRouter()

@router.post("/") #Devices log readings
def sensor_data(ping: device):
    utils.create_weather_entry("weather",ping.message)
    return

@router.get("/") #Server gets readings
def get_sensor_data():
    return

