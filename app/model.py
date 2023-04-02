from datetime import datetime
import json
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
    distance    = FloatField()

    def json(self):
        dic = json.loads(self.to_json())
        dic['timestamp'] = dic['timestamp']['$date']
        return dic

class CreateRoot(BaseModel):
    timestamp: datetime
    location: list
    message: str
    variant: str

class CreateReply(BaseModel):
    timestamp: datetime
    location: list
    message: str