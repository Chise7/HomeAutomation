from pydantic import BaseModel

class device(BaseModel):
    id: str #EX: PiZero, LaundryC6
    message: str
    status: str #Online, Offline, Not In Use