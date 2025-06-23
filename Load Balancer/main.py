from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": f"Hello, FastAPI from {os.getenv('APP_NAME')}"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q, 'server': os.getenv('APP_NAME')}
