from sqlmodel import Field, SQLModel

class ItemBase(SQLModel):
    name: str = Field(index=True)
    description: str | None = Field(default=None, index=True)
    price: float = Field(default=None,index=True)

class Item(ItemBase, table=True):
    id: int = Field(default=None, primary_key=True)
    secret_price: float | None = Field(default=None, index=True)

class ItemPublic(ItemBase):
    id: int

class ItemCreate(ItemBase):
    secret_price: float | None

class ItemUpdate(ItemBase):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    secret_price: float | None = None