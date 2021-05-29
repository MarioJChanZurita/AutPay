from src import db
from mongoengine import EmbeddedDocumentField
from src.models import service


class User(db.Document):
    username = db.StringField()
    password_hash = db.StringField()
    list_of_services = db.ListField(EmbeddedDocumentField(service))
