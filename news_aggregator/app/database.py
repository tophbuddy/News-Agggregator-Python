from pymongo import MongoClient

class Database:
    def __init__(self, uri, database_name):
        self.client = MongoClient(uri)
        self.db = self.client[database_name]
        self.news_collection = self.db['news']