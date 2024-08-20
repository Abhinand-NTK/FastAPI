from fastapi import APIRouter
from typing import List

router = APIRouter()


fake_items_db = [
    {
        "item_name":"Foo",
        "item_name":"Bar",
        "item_name":"Baz",
    }
]

@router.get("/path/")
async def read_items(skip: int = 0, limit:int = 10):
    return fake_items_db[skip: skip + limit]