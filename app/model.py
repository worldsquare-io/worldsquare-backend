from datetime import datetime
from mongoengine import Document
from mongoengine.fields import *
from pydantic import BaseModel

class ItemModel(Document):
    oid         = StringField(primary_key=True)
    timestamp   = DateTimeField()
    location    = GeoPointField()
    message     = StringField()
    # image       = ImageField()
    variant     = StringField()
    root        = BooleanField()
    parent      = StringField()

class CreateRoot(BaseModel):
    timestamp: datetime
    location: list
    message: str
    variant: str

class CreateReply(BaseModel):
    timestamp: datetime
    location: list
    message: str
    parent: str