from fastapi import APIRouter
from app.schemas.items import Item

router = APIRouter()

@router.get('/items/')
async def items(item:Item):
    return item
@router.post('/items_details/')
async def item_details(item:Item):
    return item