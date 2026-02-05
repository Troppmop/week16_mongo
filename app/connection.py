import json
from pymongo import MongoClient
from os import getenv


mongo_uri = getenv("MONGO_URI", "mongo://mongo.mopthetrop-dev.svc.cluster.local:30000")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")


# Making Connection
myclient = MongoClient(mongo_uri)

# database
db = myclient[mongo_db]

# Created or Switched to collection
# names: GeeksForGeeks
Collection = db[mongo_collection]