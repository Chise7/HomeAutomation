from fastapi import FastAPI
from pydantic import BaseModel
from api.laundry import router as laundry_router
from api.weather import router as weather_router 
from api.logs import router as logs_router 
from api.status import router as status_router 

app = FastAPI()

app.include_router(laundry_router, prefix="/laundry")
app.include_router(weather_router, prefix="/weather")
app.include_router(logs_router, prefix="/logs")
app.include_router(status_router, prefix="/status")

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

