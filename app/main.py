import datetime
import json
import nanoid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mongoengine import connect
from app.model import ItemModel, CreateRoot, CreateReply

connect('worldsquare')
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def index():
    return {"message": "You've found the worldsquare API endpoint! Maybe you are looking for https://worldsquare.io?"}

@app.post("/items")
def post_item(root: CreateRoot):
    item = ItemModel(
        oid = nanoid.generate(),
        root = True,
        **root.dict()
    )
    item.save()
    return json.loads(item.to_json())

@app.get("/items")
def get_items():
    items = ItemModel.objects(root=True)
    return [json.loads(i.to_json()) for i in items]

@app.get("/items/{oid}")
def get_item(oid):
    item = ItemModel.objects(pk=oid).first()
    return json.loads(item.to_json())

@app.post("/items/{oid}/replies")
def post_replies(oid, reply: CreateReply):
    print(reply.dict())
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
    items = ItemModel.objects(parent=oid).order_by("timestamp")
    return [json.loads(i.to_json()) for i in items]
