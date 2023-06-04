import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create the "flaskmongodb" database
db = client["flaskmongodb"]

