from fastapi import FastAPI, HTTPException, Request, Depends
from typing import Union, List

from sqlalchemy.orm import Session

from .database import engine, Base, get_db
from .schema import ItemBase, ItemCreate, ItemResponse
from .models import Item

# create db
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
def helloWorld():
    return {
        "message" : "Hello World"
    }

# with parameter
@app.get('/items/{item_id}',response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    return db_item

@app.get('/items',response_model=List[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    db_item = db.query(Item).all()
    return db_item

# query string
@app.get('/products/{id}')
def read_product(id: int, search: Union[str, None] = None):
    return {
        "product_id" : id,
        "search" : search
    }

# @app.post('/items')
# async def create_item(request: Request):
#     body = await request.json() # Convert json to dictionary
#     # print(body["name"]) # like console.log in nodejs
#     return {
#         "request body" : body,
#         "product name" : body['name'],
#         "product price" : body['price']
#     }

@app.post('/items',response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    # print(item.name , item.price)
    # db_item = Item(title=item.title, description=item.description, price=item.price)
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item

# @app.put('/items/{item_id}')
# def update_item(item_id: int, item: ItemBase):
#     return {
#         "id" : item_id,
#         "request item": item
#     }

@app.put('/items/{item_id}', response_model=ItemResponse)
async def update_item(item_id: int, item: ItemBase, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        for key, value in item.model_dump().items():
            setattr(db_item, key, value) # Edit key value
        db.commit()
        db.refresh(db_item)

    return db_item


# @app.delete('/items/{item_id}')
# def delete_item(item_id: int):
#     return {"message" : f"Item {item_id} deleted"}

@app.delete('/items/{item_id}')
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()

    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        db.delete(db_item)
        db.commit()
        return {"message" : f"Item {item_id} deleted"}