from fastapi import FastAPI, HTTPException, status
from fastapi.responses import PlainTextResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import List
from pydantic import BaseModel, Characteristic


app = FastAPI()
#EXO a
@app.get("/ping", response_class=PlainTextResponse)
def ping():
    return "pong"

#EXO b
class Cars(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic

class Characteristic(BaseModel):
    max_speed:int
    max_fuel:int

cars_db = List[Cars] = []

@app.post("/cars", response_model=List[Cars], status_code=201)
def create_cars(new_cars: List[Cars]):
    cars_db.extend(new_cars)
    return new_cars

#EXO C
@app.get("/cars", response_model=List[Cars])
def get_cars():
    return cars_db

#EXO D
@app.get("/cars/{id}", response_model=Cars)
def get_cars_by_id(id: int):
    for cars in cars_db:
        if cars.id == id:
            return cars
    raise HTTPException(status_code=404, detail="Cars not found")


