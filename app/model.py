from mongoengine import Document
from mongoengine.fields import *

class ItemModel(Document):
    timestamp   = DateTimeField()
    location    = GeoPointField()
    message     = StringField()
    image       = ImageField()
    variant     = StringField()
    root        = BooleanField()
    # in_response = ReferenceField(ItemModel)