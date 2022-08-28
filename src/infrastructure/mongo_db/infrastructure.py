# THIRD PART IMPORTS
from decouple import config
from pymongo import MongoClient


class MongoDBInfrastructure:

    client = None

    @classmethod
    def get_client(cls):
        if cls.client is None:
            url = config("MONGO_CONNECTION_URL")
            cls.client = MongoClient(url)
        return cls.client
