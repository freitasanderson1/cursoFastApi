from pydantic import BaseModel
from fastapi import APIRouter
from datetime import datetime, UTC

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = True

router = APIRouter()

@router.get("/")
def read_root():
  return {"Hello": "World"}


@router.get("/items/{item_type}")
def read_item(item_type: int):
  return {"items": [{'title':f'Item {item_type}', 'date':datetime.now(UTC)}]}


@router.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
  return {"item_name": item.name, "item_id": item_id}