from fastapi import FastAPI
from app.routers.pathparameter import pathparameter

app = FastAPI()

# Include routers
app.include_router(pathparameter.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI project!"}
