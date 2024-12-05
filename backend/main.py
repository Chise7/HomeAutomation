from fastapi import FastAPI
from pydantic import BaseModel
from api.laundry import router as laundry_router
from api.sensors import router as sensor_router 
from api.logs import router as logs_router 

app = FastAPI()


app.include_router(laundry_router, prefix="/laundry")
app.include_router(sensor_router, prefix="/sensor")
app.include_router(logs_router, prefix="/logs")

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

