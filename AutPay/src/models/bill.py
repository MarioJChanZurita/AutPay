from src import db
import datetime


class Bill(db.Document):
    charge = db.IntField()
    payment_date = db.DateTimeField(default=datetime.datetime.utcnow)
    total = db.IntField(min_value=0, max_value=None)
