from pydantic import BaseModel
from core import utils

class device(BaseModel):
    device_id: str
    status: str

class laundry_device(device):
    message: str

class sensor(BaseModel):
    moisture: int
    temperature: int
    cpu_temp: int

class err_log(BaseModel):
    device_id: str
    message: str

