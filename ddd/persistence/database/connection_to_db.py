# from mongoengine import connect
# from sqlalchemy import create_engine
import pymongo
from pymongo import MongoClient


class ConnectionCreator:
    def __init__(self, db_path, db_name=None):
        # SQL
        """engine = create_engine(db_path, echo=True)
        self.conn = engine.connect()"""
        # MongoDB using MongoEngine
        "connect(host=db_path)"
        # MongoDB using PyMongo
        mongo_client = MongoClient(db_path)
        self.db = mongo_client[db_name]
