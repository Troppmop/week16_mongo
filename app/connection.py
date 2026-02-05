import json
from pymongo import MongoClient
from os import getenv


mongo_uri = getenv("MONGO_URI", "localhost:27017")
mongo_db = getenv("MONGO_DB", "testdb")
mongo_collection = getenv("MONGO_COLLECTION", "testcollection")


# Making Connection
myclient = MongoClient(mongo_uri)

# database
db = myclient[mongo_db]

# Created or Switched to collection
# names: GeeksForGeeks
Collection = db[mongo_collection]