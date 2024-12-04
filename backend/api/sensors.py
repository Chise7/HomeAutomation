#This file will represent all of the API endpoints for sensor data.

from fastapi import APIRouter
from classes import Pi

router = APIRouter()



@router.post("/sensor")
def sensor_data():
    return

# @router.post("/status")
# async def post_status():
#     return{"message":"My status is: ----"}