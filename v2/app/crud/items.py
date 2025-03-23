from fastapi import HTTPException
from typing import Optional
from ..models.item import *
from ..database import SessionDep
from sqlmodel import select

fake_items_db = [{"item_name": f"Item {i}"} for i in range(1, 16)]


# def read_items():
#     return {"items: abc"}

# def read_items(session: SessionDep) -> list[Item]:
#     items = session.exec(select(Item)).all()
#     return items

def read_items(session: SessionDep):
    items = session.exec(select(Item)).all()
    return items

# def read_item(item_id: int):
#     return {"item_id" : item_id}

# def read_item(item_id: int, session: SessionDep) -> Item | None:
#     items = session.exec(select(Item).where(Item.id == item_id)).first()
#     # print(items)
#     return items

def read_item(item_id: int, session: SessionDep):
    items = session.get(Item, item_id)
    # print(items)
    return items

# def read_items_skip_limit(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]

def read_items_skip_limit(skip: int = 0, limit: int = 10, session: SessionDep = None) -> list[Item]:
    items = session.exec(select(Item).limit(limit).offset(skip)).all()
    return items


def read_items_skip_limit_optional(skip: Optional[int] = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# def add_item(item: Item, session: SessionDep) -> Item:
#     session.add(item)
#     session.commit()
#     session.refresh(item)
#     return item

def add_item(item: ItemCreate, session: SessionDep):
    db_item = Item.model_validate(item)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item

def delete_item(item_id: int, session: SessionDep):
    item = session.get(Item, item_id)
    if not item:
        return None
    else:
        session.delete(item)
        session.commit()
        return {"message" : f"Item {item_id} deleted"}
    
def update_item(item_id: int, item: ItemUpdate, session: SessionDep):
    item_db = session.get(Item, item_id)
    
    if not item_db:
        return None
    else:
        item_data = item.model_dump(exclude_unset=True)
        item_db.sqlmodel_update(item_data)
        session.add(item_db)
        session.commit()
        session.refresh(item_db)
        return item_db
    
def update_item_price(item_id: int, item: ItemUpdate, session: SessionDep):
    item_db = session.get(Item, item_id)

    if not item_db: 
        return None
    else:
        item_data = item.model_dump(exclude_unset=True)
        item_db.sqlmodel_update(item_data)
        session.add(item_db)
        session.commit()
        session.refresh(item_db)
        return item_db
