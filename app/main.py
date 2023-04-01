import datetime
import json
import nanoid
from fastapi import FastAPI
from pydantic import BaseModel
from mongoengine import connect
from app.model import ItemModel, CreateRoot, CreateReply

connect('worldsquare')
app = FastAPI()

@app.get("/")
def index():
    return {"msg": "hello world"}

@app.post("/items/")
def post_item(root: CreateRoot):
    print(root)
    item = ItemModel(
        oid = nanoid.generate(),
        root = True,
        **root.dict()
    )
    item.save()
    return json.loads(item.to_json())

@app.get("/items/{oid}")
def get_item():
    item = ItemModel.objects(pk=oid).first()

@app.post("/items/{oid}/replies")
def post_resplies(reply: CreateResponse):
    ...
