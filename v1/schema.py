from pydantic import BaseModel

# Pydantic Model
# Base Class

class ItemBase(BaseModel): # inheritant BaseModel
    title: str
    description: str
    price: float

#  Request - Inherit (Create)
class ItemCreate(ItemBase):
    pass

# Response
class ItemResponse(ItemBase):
    id: int # return form db
    class Config:
        form_attributes = True