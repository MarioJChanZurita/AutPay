from src import db
from src.models import bill
from mongoengine import EmbeddedDocumentField


class Service(db.Document):
    company = db.StringField()
    list_of_bills = db.ListField(EmbeddedDocumentField(bill))
