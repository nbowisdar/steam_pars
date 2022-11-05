from pymongo import MongoClient
from steam_pars.src.config.config import MONGO_HOST, MONGO_PORT


client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client.steam


class MongoQueriesBase:
    def __init__(self, collection):
        self.collection = collection

    def prune_collection(self):
        self.collection.drop()

    def insert_many(self, items: list):
        self.collection.insert_many(items)

    def get_all(self) -> list:
        # bellow I can change retrieved data, by passing argument
        # example: find( {}, {name: 1, age: 1}... )
        query = self.collection.find()
        return [item for item in query]


