#Endpoint for error logging of all devices

from fastapi import APIRouter
from backend.core import utils
from backend.core.classes import err_log

router = APIRouter()

@router.post("/")
def error_log(ping: err_log):
    utils.create_error_log(ping)
    return

@router.get("/")
def get_logs():
    return

@router.delete("/{log}")
def remove_log():
    return

