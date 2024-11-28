from fastapi import FastAPI
from pydantic import BaseModel
from backend.api.devices import router as devices_router #Microcontrollers to Webserver
# from api.endpoints.user import router as user_router #User to Webserver

app = FastAPI()


app.include_router(devices_router, prefix="/devices")
# app.include_router(user_router, prefix="/user")


#Examples:

# class Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = None

# @app.get("/")
# def read_root():
#     return{"Hello":"World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return{"item_id":item_id,"q":q}

# @app.post("/items/")
# def create_item(item: Item):
#     return item

