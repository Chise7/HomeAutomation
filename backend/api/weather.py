#This file will represent all of the API endpoints for weather data.

from fastapi import APIRouter, HTTPException, Request, Depends
from backend.core.classes import sensor, weather
from core import utils
from sqlalchemy.orm import Session
from database.database import get_db

router = APIRouter()

@router.post("/") #Devices log readings
async def sensor_data(ping: sensor, db: Session = Depends(get_db)):
    utils.create_weather_entry(ping, db)
    return

@router.get("/") #Server gets readings
def get_weather_data():

    return

