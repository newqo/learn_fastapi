from fastapi import APIRouter, HTTPException
from typing import Optional
from ..crud.items import *
from ..models.item import *
from ..database import SessionDep

router = APIRouter(
    prefix="/items",
)

# @router.get("/")
# def read_items_route():
#     return read_items()

# @router.get("/")
# def read_items_route():
#     return read_items()

@router.get("/",response_model=list[ItemPublic])
def read_items_route(session : SessionDep):
    return read_items(session)

@router.get("/{item_id}",response_model=ItemPublic)
def read_item_route(item_id: int, session: SessionDep):
    respone = read_item(item_id, session)
    if not respone:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return respone

# @router.get("/query/")
# def read_items_skip_limit_route(skip: int , limit: int):
#     return read_items_skip_limit(skip, limit)

@router.get("/query/")
def read_items_skip_limit_route(skip: int , limit: int, session: SessionDep):
    return read_items_skip_limit(skip, limit, session)

@router.get("/query/optional/")
def read_items_skip_limit_optional_route(skip: Optional[int] = 0, limit: Optional[int] = 10):
    return read_items_skip_limit_optional(skip,limit)

# @router.post("/")
# def add_item_route(item: Item, session: SessionDep) -> Item:
#     return add_item(item, session)

@router.post("/", response_model=ItemPublic)
def add_item_route(item: ItemCreate, session: SessionDep):
    return add_item(item, session)

@router.delete("/{item_id}")
def delete_item_route(item_id: int, session: SessionDep):
    response = delete_item(item_id, session)
    if not response:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return response
    
@router.put("/{item_id}", response_model=ItemPublic)
def update_item_route(item_id: int, item: ItemUpdate, session: SessionDep):
    response =  update_item(item_id, item, session)
    if not response:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return response
    
@router.patch("/{item_id}",response_model=ItemPublic)
def update_item_price_route(item_id: int, item: ItemUpdate, session: SessionDep):
    response = update_item_price(item_id, item, session)
    if not response:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return response