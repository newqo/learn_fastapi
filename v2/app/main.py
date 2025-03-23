from fastapi import FastAPI
from .database import create_db_and_tables
from .routers import root
from .routers import items

app = FastAPI()

app.add_event_handler("startup", create_db_and_tables)

app.include_router(root.router)
app.include_router(items.router)