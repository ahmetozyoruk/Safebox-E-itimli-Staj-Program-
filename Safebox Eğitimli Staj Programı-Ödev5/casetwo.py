import pymongo

# Connect to MongoDB with authentication
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create the "flaskmongodb" database
db = client["flaskmongodb"]

# Create the "users" collection
users_collection = db["users"]

# 1. Query to find the person with the name "Ahmet" in the Users collection
ahmet_user = users_collection.find_one({"Name": "Ahmet"})
print("Person with name Ahmet:")
print(ahmet_user)
print()

# 2. Query to find people over 20 years old in the Users collection
users_over_20 = users_collection.find({"Age": {"$gt": 20}})
print("People over 20 years old:")
for user in users_over_20:
    print(user)
print()

# 3. Query to set the description to 0 for those over the age of 25 in the Users collection
users_over_25 = users_collection.find({"Age": {"$gt": 25}})
print("Updating description to 0 for users over 25:")
for user in users_over_25:
    users_collection.update_one({"_id": user["_id"]}, {"$set": {"Description": 0}})
print()

# 4. Query to delete people between the ages of 45-48 in the Users collection
users_between_45_48 = users_collection.delete_many({"Age": {"$gte": 45, "$lte": 48}})
print(f"Deleted {users_between_45_48.deleted_count} documents.")

