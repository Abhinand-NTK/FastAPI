from fastapi import APIRouter

router = APIRouter()


@router.get("/items/{items_id}")
async def pathparameter(item_id):
    return {"item_id":item_id}