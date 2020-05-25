import pymongo


class Mongo:

    def __init__(self, server = "localhost", port = 27017, database="systems", user = None, password = None):
        mongo = pymongo.MongoClient(server, port)
        self.db = mongo[database]


    def get_collections(self):
        return self.db.list_collection_names()


    def get_docs(self, collection):
        return self.db[collection].find({})
        

    def insert_docs(self, collection, docs):
        self.db[collection].insert_many(docs)


    def update(self, collection, query, doc):
        self.db[collection].update_one(query, {"$set": doc}, upsert=True)

