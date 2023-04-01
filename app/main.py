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
    return {"message": "You've found the worldsquare API endpoint! Maybe you are looking for https://worldsquare.io?"}

@app.post("/items/")
def post_item(root: CreateRoot):
    item = ItemModel(
        oid = nanoid.generate(),
        root = True,
        **root.dict()
    )
    item.save()
    return json.loads(item.to_json())

@app.get("/items/")
def get_items():
    items = ItemModel.objects()
    return [json.loads(i.to_json()) for i in items]

@app.get("/items/{oid}")
def get_item():
    item = ItemModel.objects(pk=oid).first()

@app.post("/items/{oid}/replies")
def post_replies(oid, reply: CreateReply):
    item = ItemModel(
        oid = nanoid.generate(),
        variant = "local",
        root = False,
        parent = oid,
        **reply.dict()
    )
    item.save()
    return json.loads(item.to_json())

@app.get("/items/{oid}/replies")
def get_replies(oid):
    ItemModel.objects(parent=oid)
