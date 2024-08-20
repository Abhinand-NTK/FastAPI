from enum import Enum
from fastapi import FastAPI
from app.routers import pathparameter
from app.routers import pathparameter_with_enumclass
from app.routers import query_parameter
from app.routers import request_body_ex
from app.routers import query_parameter_with_sting_validation


app = FastAPI()

app.include_router(pathparameter.router)
app.include_router(pathparameter_with_enumclass.router)
app.include_router(query_parameter.router)
app.include_router(request_body_ex.router)
app.include_router(query_parameter.router)
app.include_router(query_parameter_with_sting_validation.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI project!"}
