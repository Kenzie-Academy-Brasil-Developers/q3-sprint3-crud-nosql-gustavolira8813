from flask import Flask
import pymongo
from app import views as routes


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["kenzie"]

def create_app():

    app = Flask(__name__, static_folder=None)
    routes.init_app(app)

    app.config["JSON_SORT_KEYS"] = False




    return app