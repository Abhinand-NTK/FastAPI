from fastapi import APIRouter
from app.schemas.items import Item

router = APIRouter()

@router.get('/items/')
async def items(item:Item):
    return item