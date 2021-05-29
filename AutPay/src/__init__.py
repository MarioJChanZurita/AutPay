from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)  # File name
db = MongoEngine()

app.config['MONGODB_SETTINGS'] = {
    'db': 'AutPayDB',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


from src.controllers import bill_controller