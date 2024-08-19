from enum import Enum
from fastapi import FastAPI
from app.routers import pathparameter
from app.routers import pathparameter_with_enumclass




app = FastAPI()

app.include_router(pathparameter.router)
app.include_router(pathparameter_with_enumclass.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI project!"}
