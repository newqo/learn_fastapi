from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def hello():
    return {"message" : "Hello World"}

@router.get("/hello/{name}")
def hello_name(name: str):
    return {"message" : f"Hello {name}"}

