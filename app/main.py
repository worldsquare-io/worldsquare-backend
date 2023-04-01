from fastapi import FastAPI
from mongoengine import connect
from app.model import ItemModel

connect('worldsquare')
app = FastAPI()

@app.get("/")
def index():
    return {"msg": "hello world"}

@app.get("/item/{id_}")
def get_item():
    # item = ItemModel.objects(pk=)
    ...

@app.post("/item/")
def post_item():
    item = ItemModel(
        message="test"
    )
    item.save()
    import pdb; pdb.set_trace()